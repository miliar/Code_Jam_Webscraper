#include <cstdio>
using namespace std;
const int maxn=105;
double wp[maxn],owp[maxn],oowp[maxn],w[maxn],tot[maxn];
int test,n;
char map[maxn][maxn],s[maxn];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&test);
	for (int kase=1;kase<=test;kase++)
	{
		printf("Case #%d:\n",kase);
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%s",s+1);
			tot[i]=wp[i]=w[i]=0.0;
			for (int j=1;j<=n;j++)
			{
				map[i][j]=s[j];
				if (s[j]!='.') tot[i]+=1.0;
				if (s[j]=='1') w[i]+=1.0;
			}
			wp[i]=w[i]/tot[i];
		}
		for (int i=1;i<=n;i++)
		{
			owp[i]=0;
			for (int j=1;j<=n;j++)
			if (map[i][j]=='0') owp[i]+=(w[j]-1)/(tot[j]-1); else
			if (map[i][j]=='1') owp[i]+=w[j]/(tot[j]-1);
			owp[i]/=tot[i];
		}
		for (int i=1;i<=n;i++)
		{
			oowp[i]=0;
			for (int j=1;j<=n;j++)
			if (map[i][j]!='.') oowp[i]+=owp[j];
			oowp[i]/=tot[i];
		}
		for (int i=1;i<=n;i++)
			printf("%.6lf\n",0.25*wp[i]+0.50*owp[i]+0.25*oowp[i]);
	}
	
	return 0;
}
