#include <cstdio>
#include <cstring>

const int maxn = 500;

char a[maxn + 2];
char b[20] = "welcome to code jam";
int opt[19][maxn];
int n, m;

int main()
{
	int testnumber, testcount;
	int i, j;
	
//	freopen("C-large.in", "r", stdin);
//	freopen("c.out", "w", stdout);
	scanf("%d", &testnumber);
	m = 19;
	while (getchar() == '\n');
	for (testcount = 0; testcount < testnumber; testcount++)
	{
		gets(a);
		n = strlen(a);
		for (i = 0; i < m; i++)
		{
			int now;
			if (i) now = 0; else now = 1;
			for (j = 0; j < n; j++)
			{
				if (a[j] == b[i]) opt[i][j] = now;
				else opt[i][j] = 0;
				if (i) now = (now + opt[i - 1][j]) % 10000;
			}
		}
		int now = 0;
		for (i = 0; i < n; i++)
			now = (now + opt[18][i]) % 10000;
		printf("Case #%d: %04d\n", testcount + 1, now);
	}
	
	return 0;
}
