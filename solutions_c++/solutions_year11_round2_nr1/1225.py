#include<stdio.h>
#include <string.h>

int r[120][120];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	int Case=1;
	scanf("%d", &T);
	while (T--)
	{
		int n, i, j;
		int win[120]={0};
		int lose[120]={0};
		int sum[120]={0};
		long double wp[120]={0.0};
		long double owp[120]={0.0};
		long double oowp[120]={0.0};
		char tmp[200];
		scanf("%d", &n);
		getchar();
		memset(r, -1, sizeof(r));
		for (i=0; i<n; i++)
		{
			gets(tmp);
			for (j=0; j<n; j++)
			{
				if(tmp[j]=='1') { r[i][j]=1; win[i]++; sum[i]++; }
				if(tmp[j]=='0') { r[i][j]=0; lose[i]++; sum[i]++; }
			}
		}
		
		//WP
		for(i=0; i<n; i++)
		{
			wp[i]=win[i]*1.0/sum[i];
		}

		//OWP
		for (j=0; j<n; j++) //ап
		{
			long double mm=0;
			for (i=0; i<n; i++)
			{
				if(r[i][j]==-1) continue;
				if(r[i][j]==1) { mm+=(win[i]-1.0)*1.0/(sum[i]-1.0); }
				if(r[i][j]==0) { mm+=(win[i])*1.0/(sum[i]-1.0); }
				owp[j]=mm/sum[j];
			}
		}

		//OOWP
		for (i=0; i<n; i++)
		{
			long double gg=0;
			for (j=0; j<n; j++)
			{
				if(r[i][j]!=-1) { gg+=owp[j]; }
			}
			oowp[i]=gg/sum[i];
		}

		printf("Case #%d:\n", Case++);
		for (i=0; i<n; i++)
		{
			printf("%.16lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
		}
	}
	return 0;
}