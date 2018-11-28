#include<cstdio>
char f[105][105];
double wp[105],owp[105],oowp[105];
int win[105],sum[105];
int t,mt,i,j,n;
int main()
{
	freopen("Al.in","r",stdin);
	freopen("Al.out","w",stdout);
	scanf("%d",&t);
	for(mt=1;mt<=t;mt++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		scanf("%s",f[i]);
		printf("Case #%d:\n",mt);
		for(i=0;i<n;i++)
		{
			int w=0,c=0;
			for(j=0;j<n;j++)
			{
				if (f[i][j]=='1') 
				{
					w++;
					c++;
				}
				if (f[i][j]=='0')
				{
					c++;
				}
			}
			win[i]=w;
			sum[i]=c;
			wp[i]=1.0*w/c;
		}
		for(i=0;i<n;i++)
		{
			double c=0;int cc=0;
			for(j=0;j<n;j++)
			{
				if(f[i][j]=='1')
				{
					c+=1.0*win[j]/(sum[j]-1);
					cc++;
				}
				if(f[i][j]=='0')
				{
					c+=1.0*(win[j]-1)/(sum[j]-1);
					cc++;
				}
			}
			owp[i]=c/cc;
		}
		for(i=0;i<n;i++)
		{
			double c=0;
			int cc=0;
			for(j=0;j<n;j++)
			{
				if(f[i][j]=='1'||f[i][j]=='0')
				{
					c+=owp[j];
					cc++;
				}
			}
			oowp[i]=c/cc;
		}
		for(i=0;i<n;i++)
		{
			printf("%.12f\n",wp[i]*0.25+owp[i]*0.5+oowp[i]*0.25);
		}
	}
	
}
