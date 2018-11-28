#include<cstdio>

int map[100][100];
double WP[100], OWP[100], OOWP[100];
double Cnt[100];

int main()
{
	int cas, T;
	scanf("%d", &T);
	for(cas = 1; cas <= T; cas ++)
	{
		int i, j, k;
		int n, m;
		scanf("%d", &n);
		for(i = 0; i < n; i ++)
		{
			char ch[4];
			WP[i] = Cnt[i] = 0;
			for(j = 0; j < n; j ++)
			{
				scanf("%1s", ch);
				if(ch[0] == '.')
				{
					map[i][j] = -1;
				}
				if(ch[0] == '0')
				{
					Cnt[i] += 1;
					map[i][j] = 0;
				}
				if(ch[0] == '1')
				{
					WP[i] += 1;
					Cnt[i] += 1;
					map[i][j] = 1;
				}
			}
			WP[i] /= Cnt[i];
		}
		
		for(i = 0; i < n; i ++)
		{
			OWP[i] = 0;
			for(j = 0; j < n; j ++)
			if(map[i][j] != -1)
			{
				if(map[i][j] == 0)
				{
					OWP[i] += (WP[j]*Cnt[j]-1)/(Cnt[j]-1);
				}
				else {
					OWP[i] += (WP[j]*Cnt[j])/(Cnt[j]-1);
				}
			}
			OWP[i] /= Cnt[i];
		}
		printf("Case #%d:\n", cas);
		for(i = 0; i < n; i ++)
		{
			OOWP[i] = 0;
			for(j = 0; j < n; j ++)
			if(map[i][j] != -1)
			{
				OOWP[i] += OWP[j];
			}
			OOWP[i] /= Cnt[i];
			//printf("%lf %lf %lf\n", WP[i], OWP[i], OOWP[i]);
			printf("%.9lf\n", 0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
		}
	}
	return 0;
} 
