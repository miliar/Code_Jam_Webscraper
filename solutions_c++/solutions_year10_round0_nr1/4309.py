#include<iostream>
#include<bitset>

using namespace std;
int main()
{
	FILE *in;
	FILE *out;

	in = fopen("input.txt", "r");
	out = fopen("output.txt", "w");

	int num = 0;
	fscanf(in, "%d", &num);
	int caseno = 1;
	while (num--)
	{
		int n,k;
		fscanf(in, "%d %d", &n, &k);
		bitset<30> plug;
		plug.reset();
		for (int i = 0; i < k; i++)
		{

			for (int j = 0; j < n; j++)
			{
				
				bool power = !plug.at(j);
				plug.flip(j);

				if (power)
					break;
			}
		}
		
		bool check;
		for (int i = 0; i < n; i++)
		{
			check = plug.at(i);
			if (!check)
				break;
		}
		
		if (check)
			fprintf(out, "Case #%d: ON\n", caseno++);
		else
			fprintf(out, "Case #%d: OFF\n", caseno++);
	}

	fclose(in);
	fclose(out);
	return 0;
}
