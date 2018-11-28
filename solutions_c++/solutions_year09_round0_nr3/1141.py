#include <cstdio>
#include <cstring>

int n, m;
char str[505];
const char *welcome = " welcome to code jam";

int d[505][25];

int main()
{
	m = strlen(welcome) - 1;

	int r;
	scanf("%d", &r);
	gets(str);
	for(int t = 1; t <= r; ++t)
	{
		gets(str + 1);
		n = strlen(str + 1);
		memset(d, 0, sizeof(d));

		int i, j;
		for(i = 0; i <= n; ++i)
			for(j = 0; j <= m; ++j)
			{
				if( j == 0 ){ d[i][j] = 1; continue; }
				if( i < j ) continue;
				
				d[i][j] = d[i - 1][j];
				if( str[i] == welcome[j] )
				{
					d[i][j] += d[i - 1][j - 1];
					if( d[i][j] >= 10000 ) d[i][j] -= 10000;
				}
			}

		printf("Case #%d:\n", t);
		printf("%04d\n", d[n][m]);
	}
	return 0;
}

