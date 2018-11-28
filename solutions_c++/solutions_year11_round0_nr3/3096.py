#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void main()
{
	FILE *In, *Out;
	In = fopen("in.txt", "a+");
	Out = fopen("out.txt", "w");

	int NumCases; 
	fscanf(In, "%d", &NumCases);
	int Res = 0;

	int Candy;
	int PatricSum1;
	int PatricSum2;
	int SeanSum1;
	int SeanSum2;

	for (int Case=1; Case <= NumCases; Case++)
	{
		Res = 0;
		PatricSum1 = 0;
		PatricSum2 = 0;
		SeanSum1 = 0;
		SeanSum2 = 0;
		fscanf(In, "%d", &Candy);
		int* Candies = new int [Candy];
		for (int i=0; i<Candy; i++)
			fscanf(In, "%d", &Candies[i]);

		for (int i=1; i<pow(2.0, Candy)-1; i++)
		{
			PatricSum1 = 0;
			PatricSum2 = 0;
			SeanSum1 = 0;
			SeanSum2 = 0;
			for (int j=0; j<Candy; j++)
			{
				if (i&(1<<j))
				{
					PatricSum1 ^= Candies[j];
					SeanSum1 += Candies[j];
				}
				else
				{
					PatricSum2 ^= Candies[j];
					SeanSum2 += Candies[j];
				}
			}
			if (PatricSum1 == PatricSum2)
			{
				if (SeanSum1>Res) 
					Res = SeanSum1;
				if (SeanSum2>Res)
					Res = SeanSum2;
			}
		}

		if (Res == 0)
			fprintf(Out, "Case #%d: NO\n", Case);
		else
			fprintf(Out, "Case #%d: %d\n", Case, Res);

		delete Candies;
	}

	fclose(In);
	fclose(Out);
}
