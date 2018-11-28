#include<cstdio>

const int mx=110;

int n;
char s[mx][mx];
double wp[mx],owp[mx],oowp[mx];
double win[mx],total[mx];

int main()
{
	int i,j;
	int t;
	int ca=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%s",s[i]);
		for(i=0;i<n;i++)
		{
			win[i]=total[i]=0;
			for(j=0;j<n;j++)
			{
				if(s[i][j]!='.')
					total[i]++;
				if(s[i][j]=='1')
					win[i]++;
			}
			wp[i]=(win[i]+0.0)/total[i];
		}
		for(i=0;i<n;i++)
		{
			owp[i]=0;
			for(j=0;j<n;j++)
			{
				if(s[i][j]!='.')
				{
					owp[i]+=(win[j]-(s[j][i]=='1'?1:0)+0.0)/(total[j]-1);
				}
			}
			owp[i]/=total[i];
		}
		for(i=0;i<n;i++)
		{
			oowp[i]=0;
			for(j=0;j<n;j++)
			{
				if(s[i][j]!='.')
				{
					oowp[i]+=owp[j];
				}
			}
			oowp[i]/=total[i];
		}
		printf("Case #%d:\n",ca++);
		for(i=0;i<n;i++)
		{
			printf("%.15lf\n",wp[i]*0.25+owp[i]*0.5+oowp[i]*0.25);
		}
	}
	return 0;
}
