// fc_stat.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
using namespace std;

int main(int argc, char* argv[])
{
	int num_tests = -1;

	long long max_num_games_today;
	int pct_today;
	int pct_overall;

	printf("Running\n");

	FILE * fin = fopen(argv[1], "r");
	if (!fin)
	{
		printf("Couldn't open input file\n");
		return 1;
	}
	FILE * fout = fopen(argv[2], "w");
	if (!fout)
	{
		printf("Couldn't open output file\n");
		return 2;
	}

	fscanf(fin,"%d",&num_tests);
	printf("Number of tests = %d\n", num_tests);

	// read in the data and process for each goal
	for (int i = 0; i < num_tests; i++)
	{
		bool broken = false;
		fscanf(fin,"%lld %d %d",&max_num_games_today,&pct_today,&pct_overall);

		if ((pct_overall == 100) && (pct_today != 100))
			broken = true;
		else if ((pct_overall == 0) && (pct_today != 0))
			broken = true;
		else if (max_num_games_today < 100)
		{
			bool pct_ok = false;
			int pct_prod;
			for (int j = 1; j < 100 && j <= max_num_games_today; j++)
			{
				pct_prod = j * pct_today;
				if ((pct_prod % 100) == 0)
					pct_ok = true;
			}
			if (pct_ok == false)
				broken = true;
		}
		
		fprintf(fout, "Case #%d: %s\n", i+1, broken ? "Broken" : "Possible");
	}

	fclose(fout);
	fclose(fin);

    return 0;
}