#include <stdio.h>
#include <string.h>

#define N 120
char map[N][N];
int n;
double calc_owp(int t, int x)
{
	int tot = 0; 
	int win = 0;
	for (int i = 0; i < n; ++i)
	{
		if (i == x) continue;
		else
		{
			if (map[t][i] != '.')
				tot++;
			if (map[t][i] == '1')
				win++;
		}
	}
	return win * 1.0 / tot;
}
int main()
{
	freopen("a.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int cas = 1;
	while (t--)
	{
		
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
		{
			scanf("%s", map[i]);
		}
		double wp[N], owp[N], oowp[N];
		int tot;
		int win;
		for (int i = 0; i < n; ++i)
		{
			tot = 0; 
			win = 0;
			for (int j = 0; j < n; ++j)
			{
				if (map[i][j] != '.')
					tot++;
				if (map[i][j] == '1')
					win++;
			}
			wp[i] = win * 1.0 / tot;
		}
		for (int i = 0; i < n; ++i)
		{
			int num = 0;
			double fen = 0;
			for (int j = 0; j < n; ++j)
			{
				if (map[i][j] != '.')
				{
					num ++;
					fen += calc_owp(j, i); 
				}
			}
			owp[i] = fen / num;
		}

		for (int i = 0; i < n; ++i)
		{
			int num = 0;
			double fen = 0;
			for (int j = 0; j < n; ++j)
				if (map[i][j] != '.')
				{
					num ++; 
					fen += owp[j];
				}
			oowp[i] = fen / num;
		}

		printf("Case #%d:\n", cas++);
		char s[100];
		for (int i = 0; i < n; ++i)
		{
			double p = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			printf("%g\n", p);
			/*fscanf(s, "%.12lf", p);
			int len = strlen(s);
			for (int j = len - 1; j >= 0; --j)
			{
				if (s[j] == '0') continue;
				else 
				{
					s[j] = 0;
					break;
				}
			}
			printf("%s\n", s);*/
		}

	}
	return 0;
}