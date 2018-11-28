#include <cstdio>
#include <cstdlib>
#include <cstring>

int N;
char str[1024];
char ptn[20] = "welcome to code jam";

// suffCount[i][j]: how many variations of RIGHT("welcome to code jam", j) found in SUBSTRING(str, i, oo)
int suffCount[1024][20];

int main(int argc, char *argv[])
{
	scanf("%d", &N);
	for (int i = 0; i < N; ++i)
	{
		// Some C compilers skip thought the CR/LF after the number, some don't
		gets(str);
		if (str[0] == 0)
			gets(str);

		int L = strlen(str);
		for (int j = 0; j <= 19; ++j)
		{
			suffCount[L][j] = (j == 0) ? 1 : 0;
		}

		for (int k = L - 1; k >= 0; --k)
		{
			suffCount[k][0] = 1;
			for (int j = 1; j <= 19; ++j)
			{
				if (str[k] == ptn[19 - j])
				{
					suffCount[k][j] = (suffCount[k + 1][j] + suffCount[k + 1][j - 1]) % 10000;
				}
				else
				{
					suffCount[k][j] = suffCount[k + 1][j];
				}
			}
		}

		printf("Case #%d: %04d\n", i + 1, suffCount[0][19] % 10000);
	}

	return 0;

}





/*

int T, H, W;

int myMap[128][128];
int isSink[128][128];
int myBasin_U[128][128];
int myBasin_V[128][128];

int main(int argc, char *argv[])
{
	scanf("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf("Case #%d:\n", i + 1);
		
		scanf("%d %d", &H, &W);
		for (int v = 0; v < H; ++v)
		{
			for (int u = 0; u < W; ++u)
			{
				scanf("%d", &myMap[v][u]);
			}
		}

		// Find all sinks and initial flow directions
		for (int v = 0; v < H; ++v)
		{
			for (int u = 0; u < W; ++u)
			{
				bool isBasin = true;
				int alt = myMap[v][u];
				int bU = u, bV = v, bA = alt;

				if (v > 0 && myMap[v - 1][u] < bA) { isBasin = false; bV = v - 1; bU = u; bA = myMap[bV][bU]; }
				if (u > 0 && myMap[v][u - 1] < bA) { isBasin = false; bV = v; bU = u - 1; bA = myMap[bV][bU]; }
				if (u < W - 1 && myMap[v][u + 1] < bA) { isBasin = false; bV = v; bU = u + 1; bA = myMap[bV][bU]; }
				if (v < H - 1 && myMap[v + 1][u] < bA) { isBasin = false; bV = v + 1; bU = u; bA = myMap[bV][bU]; }

				isSink[v][u] = -1;
				myBasin_U[v][u] = bU;
				myBasin_V[v][u] = bV;
			}
		}

		// 32 iteration should be enough: basin[y][x] = basin[basin[y][x]]
		for (int k = 0; k < 32; ++k)
		{
			for (int v = 0; v < H; ++v)
			{
				for (int u = 0; u < W; ++u)
				{
					int bU = myBasin_U[v][u], bV = myBasin_V[v][u];
					myBasin_U[v][u] = myBasin_U[bV][bU];
					myBasin_V[v][u] = myBasin_V[bV][bU];
				}
			}
		}

		// Find basin for each cell (brute force should be enought for 100 x 100 x 10000 altitudes).
		char nextSink = 'a';
		for (int v = 0; v < H; ++v)
		{
			for (int u = 0; u < W; ++u)
			{
				int bU = myBasin_U[v][u], bV = myBasin_V[v][u];
				if (isSink[bV][bU] == -1)
					isSink[bV][bU] = nextSink++;
				if (u)
					putchar(' ');
				putchar(isSink[bV][bU]);
			}
			printf("\n");
		}
	}

	return 0;
}
*/



/*
int L, D, N;

char W[6000][32];
char P[256];



int main(int argc, char *argv[])
{
	scanf("%d %d %d", &L, &D, &N);
	for (int i = 0; i < D; ++i)
		scanf("%s", &W[i][0]);

	for (int i = 0; i < N; ++i)
	{
		scanf("%s", P);
		int wCnt = 0;
		for (int j = 0; j < D; ++j)
		{
			char *cP = P;
			bool isOK = true;
			for (int k = 0; isOK && k < L; ++k)
			{
				if (*cP == '(')
				{
					bool isMOK = false;
					cP++;
					while (*cP != ')')
					{
						if (*cP == W[j][k])
							isMOK = true;
						cP++;
					}
					cP++;
					isOK &= isMOK;
				}
				else
				{
					isOK &= *cP++ == W[j][k];
				}
			}
			if (isOK)
				wCnt++;
		}
		printf("Case #%d: %d\n", i + 1, wCnt);
	}

	return 0;

}
*/
