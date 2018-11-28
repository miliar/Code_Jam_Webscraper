#include <stdio.h>
#include <string.h>

double wp[128], owp[128], oowp[128];
int team[128][128], win[128], ng[128];

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		printf("Case #%d:\n", t);
		memset(team, 0, sizeof(team));
		memset(win, 0, sizeof(win));
		memset(ng, 0, sizeof(ng));

		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
		{
			char ent[128];
			scanf("%s", ent);
			for(int j = 0; ent[j]; j++)
			{
				if(ent[j] == '0')
				{
					team[i][j] = -1;
					ng[i]++;
				}
				else if(ent[j] == '1')
				{
					team[i][j] = 1;
					win[i]++;
					ng[i]++;
				}
			}
			wp[i] = ((double)win[i])/ng[i];
		}
		for(int i = 0; i < n; i++)
		{
			double s = 0;
			for(int j = 0; j < n; j++)
			{
				if(!team[i][j]) continue;
				if(team[i][j] == 1)
					s += ((double)win[j])/(ng[j]-1);
				else s += ((double)(win[j]-1))/(ng[j]-1);
			}
			owp[i] = s/ng[i];
		}
		for(int i = 0; i < n; i++)
		{
			double s = 0;
			for(int j = 0; j < n; j++)
			{
				if(!team[i][j]) continue;
				s += owp[j];
			}
			oowp[i] = s/ng[i];
		}
		for(int i = 0; i < n; i++)
			printf("%.9lf\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
	}
	return 0;
}
