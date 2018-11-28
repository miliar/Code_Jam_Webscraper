#include <fstream.h>
#define FAIL -1
#define DONE -2
using namespace std;

int main()
{
	int T, N, Pd, Pg;
	long long sum, min, read, xorsum;

	fstream fin("freecell.txt",ios::in);
	FILE *fout = fopen("freecell_out.txt","w");

	fin >> T;
	for (int t=0; t<T; t++)
	{
		fin >> N >> Pd >> Pg;

		if ((Pg == 100 && Pd < 100) ||
		        (Pd == 0 && Pg != 0) ||
			(Pg == 0 && Pd != 0))
		{
				fprintf(fout, "Case #%d: Broken\n", t + 1);
				goto next;
		} else {
			for (int i = 1; i <= N; i++)
			{
				if (((Pd * i)%100 == 0) && ((Pd * i / 100) <= N))
				{
					fprintf(fout, "Case #%d: Possible\n", t + 1);
					goto next;
				}
			}

			fprintf(fout, "Case #%d: Broken\n", t + 1);
		}
next:
	int a = 1;
	}
	fin.close();
	fclose(fout);

	return 0;
}
