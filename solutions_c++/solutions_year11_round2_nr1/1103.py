#include <cstdio>
#include <cstring>

char team[200][200];
double owp[200][200];
int games[200];
int win[200];
double wp[200];
double mowp[200];
double moowp[200];

int main()
{
	int cases;
	scanf("%d", &cases);
	for (int T = 1; T <= cases; T++)
	{
		int n;
		scanf("%d", &n);
		memset(games, 0, sizeof(int)*200);
		memset(win, 0, sizeof(int)*200);
		for (int i = 0; i < n; i++)
		{
			scanf("%s", team[i]);
			for (int j = 0; j < n; j++)
			{
				if (team[i][j] == '0')
					games[i]++;
				else if (team[i][j] == '1')
				{
					games[i]++; win[i]++;
				}
			}
			wp[i] = ((double)win[i])/games[i];
			for (int j = 0; j < n; j++)
			{	
				if (team[i][j] == '0')
				{
					owp[i][j] = ((double)win[i])/(games[i]-1);
				}
				else if (team[i][j] == '1')
				{
					owp[i][j] = ((double)(win[i] - 1))/(games[i]-1);
				}
			}
		}
		for (int i = 0; i < n; i++)
		{
			mowp[i] = 0.0;
			for (int j = 0; j < n; j++)
			{
				if (team[i][j] != '.')
					mowp[i] += owp[j][i];
				
			}
			mowp[i] = mowp[i]/games[i];
		}
		for (int i = 0; i < n; i++)
		{
			moowp[i] = 0.0;
			for (int j = 0; j < n; j++)
			{
				if (team[i][j] != '.')
					moowp[i] += mowp[j];
			}
			moowp[i] = moowp[i]/games[i];
		}
		printf("Case #%d:\n", T);
		for (int i = 0; i < n; i++)
			printf("%.12lf\n", wp[i] * 0.25 + mowp[i]*0.5 + moowp[i]*0.25);
		
	}
	return 0;
}