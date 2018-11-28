#include <stdio.h>
#include <string.h>
int f[600][30];
int main()
{
	int N;
	freopen("clin.txt", "r", stdin);
	freopen("clout.txt", "w", stdout);
	scanf("%d", &N);
	getchar();
	char s[600];
	char t[] = "welcome to code jam";
	for(int tcase = 1; tcase <= N; tcase++)
	{
		gets(s);
		int m = strlen(s);
		int n = strlen(t);
		memset(f, 0, sizeof(0));
		if(s[0] == t[0]) f[0][0] = 1;
		for(int i = 1; i < m; i++)
			f[i][0] = f[i-1][0]+(s[i] == t[0]);

		for(int i = 1; i < m; i++)
		{
			for(int j = 1; j < n; j++)
			{
				f[i][j] = f[i-1][j] % 10000;
				if(s[i] == t[j]) f[i][j] += f[i-1][j-1];
				f[i][j] %= 10000;
			}
		}
		printf("Case #%d: %04d\n", tcase, f[m-1][n-1] % 10000);
	}
	return 0;
}
