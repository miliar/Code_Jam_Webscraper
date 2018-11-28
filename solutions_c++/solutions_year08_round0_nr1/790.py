#include <stdio.h>
#include <string.h>

const int MAXC = 104;
const int MAXS = 104;
const int MAXQ = 1004;
const int INF = 1000000;

int brt;
int s;
int q;
char names[MAXS][MAXC];
short dp[MAXQ][MAXS];
short mindp[MAXQ];
char sename[MAXC];

int getIndex(char* str)
{
	for (int i = 0; i < s; i++)
	{
		if (strncmp(names[i], str, MAXC) == 0)
			return i;
	}

	return -1;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("task1.out", "w", stdout);

	scanf("%d", &brt);

	memset(dp, 0, sizeof(dp));
	memset(mindp, 0, sizeof(mindp));

	for(int gi = 1; gi <= brt; gi++)
	{
		scanf("%d\n", &s);
		for(int i=0;i<s;i++)
		{
			fgets(names[i], MAXC, stdin);
		}

		scanf("%d\n", &q);
		for(int i=1;i<=q;i++)
		{
			fgets(sename, MAXC, stdin);
			int ind = getIndex(sename);
			if (ind == -1)
				printf("error\n");
			mindp[i] = INF;

			for(int j=0;j<s;j++)
			{
				if (ind == j)
				{
					dp[i][j] = -1;
				}
				else
				{
					dp[i][j] = mindp[i-1] + 1;
					if (dp[i-1][j] != -1 && dp[i-1][j] < dp[i][j])
						dp[i][j] = dp[i-1][j];
					if (mindp[i] > dp[i][j])
						mindp[i] = dp[i][j];
				}
				
			}
		}

		printf("Case #%d: %d\n", gi, mindp[q]);
	}

	return 0;
}
