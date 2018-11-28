#include<stdio.h>
char c[201][201];
double WP[201];
double OWP[201];
double OOWP[201];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int tt;
	int n;
	scanf("%d",&tt);
	for(int t=1;t<=tt;t++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%s",c[i]);
		for(int i=0;i<n;i++)
		{
			double base=0.0;
			WP[i]=0.0;
			for(int j=0;j<n;j++)
			{
				base+=(c[i][j]=='0' || c[i][j]=='1');
				WP[i]+=(c[i][j]=='1');
			}
			WP[i]/=base;
		}
		for(int i=0;i<n;i++)
		{
			double base=0.0;
			OWP[i]=0.0;
			for(int j=0;j<n;j++)
			{
				if(i==j || c[i][j]=='.') continue;
				base++;
				double tmp_WP=0.0;
				double tmp_base=0.0;
				for(int k=0;k<n;k++)
				{
					if(k==i) continue;
					tmp_base+=(c[j][k]=='0' || c[j][k]=='1');
					tmp_WP+=(c[j][k]=='1');
				}
				tmp_WP/=tmp_base;
				OWP[i]+=tmp_WP;
			}
			OWP[i]/=base;
		}
		for(int i=0;i<n;i++)
		{
			double base=0.0;
			OOWP[i]=0.0;
			for(int j=0;j<n;j++)
			{
				if(c[i][j]=='.') continue;
				OOWP[i]+=OWP[j];
				base++;
			}
			OOWP[i]/=base;
		}
		printf("Case #%d:\n",t);
		for(int i=0;i<n;i++) printf("%.10lf\n",WP[i]/4+OWP[i]/2+OOWP[i]/4);
	}
	return 0;
}
