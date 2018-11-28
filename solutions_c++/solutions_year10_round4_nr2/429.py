#include <cstdio>
#include <memory>

int M[2000];

int costIn[2000][2000];

int cost[2000][2000][15];

int mmin(int a, int b)
{
	if (a < b)
		return a;
	return b;
}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		fprintf(stderr, "%d\n", t);
		int P;
		scanf("%d", &P);
		for (int i=0; i<(1<<P); i++)
		{
			scanf("%d", &M[i]);
		}
		int cc = 0;
		for (int i=0; i<P; i++)
		{
			for (int j=0; j<(1<<(P-(i+1))); j++)
			{
				scanf("%d", &costIn[i][j]);
				cc++;
			}
		}
		memset(cost,-1,sizeof(cost));
		for (int i=0; i<P; i++)
		{
			for (int j=0; j<(1<<(P-(i+1))); j++)
			{
				if (i == 0)
				{
					int scoreL = M[2*j];
					int scoreR = M[2*j+1];
					int newScore = mmin(scoreL, scoreR);
					cost[i][j][newScore] = costIn[i][j];
					if (newScore != 0)
					{
						cost[i][j][newScore-1] = 0;
					}
				}
				else
				{
					for (int left=0; left<=P; left++)
					{
						if (cost[i-1][2*j][left] == -1)
							continue;
						for (int right=0; right<=P; right++)
						{
							if (cost[i-1][2*j+1][right] == -1)
								continue;
							int newScore = mmin(left, right);
							int newCost = cost[i-1][2*j][left]+cost[i-1][2*j+1][right];
							int newCost2 = costIn[i][j]+newCost;
							if (cost[i][j][newScore] == -1 || cost[i][j][newScore] > newCost2)
								cost[i][j][newScore] = newCost2;
							if (newScore != 0)
							{
								if (cost[i][j][newScore-1] == -1 || cost[i][j][newScore-1] > newCost)
									cost[i][j][newScore-1] = newCost;
							}
						}
					}
				}
			}
		}
		int res = 1000000000;
		for (int i=0; i<=P; i++)
		{
			if (cost[P-1][0][i] != -1)
			{
				if (res > cost[P-1][0][i])
					res = cost[P-1][0][i];
			}
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}