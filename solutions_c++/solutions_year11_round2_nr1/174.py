#include <cstdio>
#include <cstring>

#define maxn 205

int n;
double WP[maxn],OWP[maxn],OOWP[maxn];
char s[maxn][maxn];

int main()
{
	freopen("A_large.in","r",stdin);
	freopen("A_large.out","w",stdout);
	
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test)
	{
		scanf("%d",&n);
		for (int i=0;i<n;++i)
			scanf("%s",s[i]);
		
		for (int i=0;i<n;++i)
		{
			int cnt=0,win=0;
			for (int j=0;j<n;++j)
			if (s[i][j]!='.')
			{
				++cnt;
				win+=s[i][j]=='1';
			}
			WP[i]=(double)win/(double)cnt;
		}
		
		for (int i=0;i<n;++i)
		{
			double avg=0,tot=0;
			for (int j=0;j<n;++j)
			if (s[i][j]!='.')
			{
				int cnt=0,win=0;
				for (int k=0;k<n;++k)
				if (s[j][k]!='.' && i!=k)
				{
					++cnt;
					win+=s[j][k]=='1';
				}
				tot+=1;
				avg+=(double)win/(double)cnt;
			}
			avg/=tot;
			OWP[i]=avg;
		}
		
		for (int i=0;i<n;++i)
		{
			double avg=0,tot=0;
			for (int j=0;j<n;++j)
			if (s[i][j]!='.')
			{
				tot+=1;
				avg+=OWP[j];
			}
			OOWP[i]=avg/tot;
		}
		
		printf("Case #%d:\n",test);
		for (int i=0;i<n;++i)
		{
			double rpi=0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i];
			//printf("	%lf %lf %lf\n",WP[i],OWP[i],OOWP[i]);
			printf("%.10f\n",rpi);
		}
	}
	return 0;
}
