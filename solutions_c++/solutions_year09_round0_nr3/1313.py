#include <algorithm>
#include <stdio.h>

#define MAX 1024
#define restRez 10000

using namespace std;

int testCases;
char strInit[MAX], wtcj[MAX];
int sol[MAX][32];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	scanf("%d\n", &testCases);

	sprintf(wtcj, " welcome to code jam");

	for (int test = 1; test <= testCases; test++)
	{
		fgets(strInit + 1, MAX, stdin);
		int n = strlen(strInit + 1) - 1, rez = 0;
		memset(sol, 0, sizeof(sol));

		for (int i = 1; i <= n; i++)
		{
			if (strInit[i] == 'w')
				sol[i][1] = 1;
			else for (int j = 2; j <= 19; j++)
				if (strInit[i] == wtcj[j])
				{
					for (int h = i - 1; h; h--)
						sol[i][j] = (sol[i][j] + sol[h][j - 1]) % restRez;
				}

			rez = (rez + sol[i][19]) % restRez;
		}

		printf("Case #%d: %04d\n", test, rez);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
