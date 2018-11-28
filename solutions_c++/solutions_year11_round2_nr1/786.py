#include <iostream>
using namespace std;

int n;
char a[110][110];
double wp[110],owp[110],oowp[110];
int sum[110],tsum[110],win[110],twin[110];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("2.out","w",stdout);
	int T,cas;
	scanf("%d",&T);
	for(cas=1;cas<=T;++cas)
	{
		scanf("%d",&n);
		int i,j;
		memset(sum,0,sizeof(sum));
		memset(win,0,sizeof(win));
		for(i=1;i<=n;++i)
		{
	
			scanf("%s",a[i]+1);
			for(j=1;j<=n;++j)
			{
				if(a[i][j]!='.')
				{
					sum[i]++;
					if(a[i][j]=='1')
						win[i]++;
				}
			}
		}
		for(i=1;i<=n;++i)
		{
			wp[i]=1.0*win[i]/sum[i];
		}
		for(i=1;i<=n;++i)
		{
			owp[i]=0;
			for(j=1;j<=n;++j) 
			{
				tsum[j]=sum[j];
				twin[j]=win[j];
			}
			for(j=1;j<=n;++j)
			{
				if(a[j][i]=='1')
				{
					twin[j]--;
					tsum[j]--;
				}
				else if(a[j][i]=='0')
				{
					tsum[j]--;
				}
			}
			for(j=1;j<=n;++j)
			{
				if(j==i) continue;
				if(a[i][j]=='.') continue;
				if(tsum[j]!=0)
					owp[i]=owp[i]+1.0*twin[j]/tsum[j]/sum[i];	
			}
		}
		for(i=1;i<=n;++i)
		{
			oowp[i]=0;
			for(j=1;j<=n;++j)
			{
				if(j==i) continue;
				if(a[i][j]=='.') continue;
				oowp[i]=oowp[i]+owp[j]/sum[i];
			}
		}
		printf("Case #%d:\n",cas);
		for(i=1;i<=n;++i) printf("%.8lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}

	return 0;
}