#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int T,n;
char s[105][105];
int w[105];
int a[105];
double wp[105];
double owp[105];
double oowp[105];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		printf("Case #%d:\n",test);
		memset(wp,0,sizeof(wp));
		memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));
		memset(a,0,sizeof(a));
		memset(w,0,sizeof(w));
		memset(s,0,sizeof(s));
		scanf("%d\n",&n);
		for(int i=0;i<n;i++)
			gets(s[i]);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(s[i][j]=='1')
					w[i]++;
				if(s[i][j]!='.')
					a[i]++;
			}
			wp[i]=(double)w[i]/a[i];
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(s[i][j]=='.')
					continue;
				owp[i]+=(w[j]-s[j][i]+'0')/((double)(a[j])-1);
			}
			owp[i]/=a[i];
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
				if(s[i][j]!='.')
					oowp[i]+=owp[j];
			oowp[i]/=a[i];
		}
		for(int i=0;i<n;i++)
			printf("%.10f\n",wp[i]*0.25+owp[i]*0.5+oowp[i]*0.25);
	}
	return 0;
}
