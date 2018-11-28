#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

#pragma comment(linker,"/STACK:10000000")

const char t[] = " welcome to code jam";
const int m = strlen(t) - 1;

const int P = 10000;
const int MaxL = 1000;

char s[MaxL];

int res[MaxL][30];

int main()
{
	int tt;
	scanf("%d\n", &tt);
	for (int ii = 1; ii <= tt; ++ii)
	{
		gets(s+1);
		int n = strlen(s+1);
		memset(res, 0, sizeof(res));
		res[0][0] = 1;
		for (int i = 1; i <= n; ++i)
			for (int j = 0; j <= m; ++j)
			{
				res[i][j] = res[i-1][j];
				if (j != 0 && s[i] == t[j])
					res[i][j] += res[i-1][j-1];
				res[i][j] %= P;
			}

		printf("Case #%d: %04d\n", ii, res[n][m]);
	}

	return 0;
}