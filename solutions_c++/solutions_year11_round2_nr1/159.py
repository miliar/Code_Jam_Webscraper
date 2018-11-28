#include <stdio.h>
#include <string.h>

const int maxn = 110;

int n;
int win[maxn], tot[maxn];
double wp[maxn], owp[maxn], oowp[maxn];
char sch[maxn][maxn];

int main()
{
	int T, cas, i, j, num;
	int x, y;
	scanf("%d", &T);
	for (cas=1; cas<=T; cas++)
	{
		scanf("%d", &n);
		for (i=0; i<n; i++)
		  scanf("%s", sch[i]);
		memset(win, 0, sizeof(win));
		memset(tot, 0, sizeof(tot));  
		for (i=0; i<n; i++)
		{
			for (j=0; j<n; j++)
			  if (sch[i][j]!='.')
			  {
			  	tot[i]++;
			  	if (sch[i][j]=='1') win[i]++;
			  }
			wp[i]=(double)win[i] / (double)tot[i];  
		}
		
		memset(owp, 0, sizeof(owp));
		for (i=0; i<n; i++)
		{
			num=0;
			for (j=0; j<n; j++)
			  if (sch[i][j]!='.')
			  {
			  	x=win[j];
			  	if (sch[j][i]=='1') x--;
			  	y=tot[j]-1;
			  	owp[i]+=(double)x/(double)y;
			  	num++;
			  }
			owp[i]/=(double)num;
		}
		
		memset(oowp, 0, sizeof(oowp));
		for (i=0; i<n; i++)
		{
			num=0;
		 	for (j=0; j<n; j++)
		 	  if (sch[i][j]!='.')
		 	  {
		 	  	num++;
		 	  	oowp[i]+=owp[j];
		 	  }
		 	oowp[i] /= (double) num;
		}
		
		printf("Case #%d:\n", cas);
		for (i=0; i<n; i++)
		{
			printf("%.12lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
		}
		
	}
	return 0;
}
/*
2
4
.11.
0.00
01.1
.10.

*/