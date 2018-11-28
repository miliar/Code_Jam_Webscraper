#include <cstdio>
#include <algorithm>
using namespace std;

const int maxn = 510;
const int m = 19;
const char w[m + 1] = "welcome to code jam";

char st[maxn];
int s[maxn][m + 1];

const int mod = 10000;

int work()
{
	fgets(st, maxn, stdin);
	fill_n(s[0], m, 0);
	int i;
	for (i = 1; st[i-1]; i++)
	{
		for (int j = 0; j < m; j++)
		{
			s[i][j] = s[i-1][j];
			if (st[i-1] == w[j]) 
			{
				if (j == 0) 
					s[i][j]++;
				else
					s[i][j] += s[i-1][j-1];
			}
			if (s[i][j] >= mod) s[i][j] %= mod;
		}
	}
	return s[i-1][m-1];
}

int main()
{
	int n;
	scanf("%d\n", &n);
	for (int i = 0; i < n; i++)
	{
		printf("Case #%d: %04d\n", i + 1, work());
	}
	return 0;
}
