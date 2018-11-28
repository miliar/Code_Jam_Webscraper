#include <cstdio>
#include <cmath>	
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN=505;

typedef long long s64;

s64 sum1[MAXN][MAXN],sum2[MAXN][MAXN],sum3[MAXN][MAXN];
int w[MAXN][MAXN];

inline  int cmp(double x)
{
	if (fabs(x)<1e-8)
		return 0;
	return 1;
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		printf("Case #%d: ",tt);
		int N,M,D;
		scanf("%d%d%d",&N,&M,&D);
		for(int i=1;i<=N;i++)
		{
			char str[MAXN];
			scanf(" %s",str+1);
			for(int j=1;j<=M;j++)
				w[i][j]=str[j]-'0'+D;
		}
		memset(sum1,0,sizeof(sum1));
		memset(sum2,0,sizeof(sum2));
		memset(sum3,0,sizeof(sum3));
		for(int i=1;i<=N;i++)
			for(int j=1;j<=M;j++)
			{
				sum1[i][j]=sum1[i-1][j]+sum1[i][j-1]-sum1[i-1][j-1]+w[i][j]*i;
				sum2[i][j]=sum2[i-1][j]+sum2[i][j-1]-sum2[i-1][j-1]+w[i][j]*j;
				sum3[i][j]=sum3[i-1][j]+sum3[i][j-1]-sum3[i-1][j-1]+w[i][j];
			}
		int ans=-1;
		for(int i=1;i<=N;i++)
			for(int j=1;j<=M;j++)
			{
				int maxk=min(N-i+1,M-j+1);
				for(int k=max(ans+1,3);k<=maxk;k++)
				{
					int a=i+k-1,b=j+k-1;
					s64 tot=sum3[a][b]-sum3[i-1][b]-sum3[a][j-1]+sum3[i-1][j-1]-(w[i][j]+w[i][b]+w[a][j]+w[a][b]);
					double x=((double)sum1[a][b]-sum1[i-1][b]-sum1[a][j-1]+sum1[i-1][j-1]
							-(w[i][j]*i+w[i][b]*i+w[a][j]*a+w[a][b]*a))/tot;
					double y=((double)sum2[a][b]-sum2[i-1][b]-sum2[a][j-1]+sum2[i-1][j-1]
							-(w[i][j]*j+w[a][j]*j+w[i][b]*b+w[a][b]*b))/tot;
					if (cmp(x-(i+a)/2.0)!=0)
						continue;
					if (cmp(y-(j+b)/2.0)!=0)
						continue;
					ans=k;
				}
			}
		if (ans==-1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",ans);
	}
	return 0;
}
