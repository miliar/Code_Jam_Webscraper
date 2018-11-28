#include <cstdio>
#include <cmath>

const int MAXN=1000005;

typedef long long s64;

s64 N;

int prime[MAXN],tot;
bool flag[MAXN];
void getprime()
{
	int M=sqrt(N);
	tot=0;
	for(int i=2;i<=M;i++)
		flag[i]=true;
	for(int i=2;i<=M;i++)
		if (flag[i])
		{
			prime[tot++]=i;
			for(int j=i+i;j<=M;j+=i)
				flag[j]=false;
		}
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		printf("Case #%d: ",tt);
		scanf("%lld",&N);
		getprime();
		int ans1;
		if (N==1)
			ans1=1;
		else
			ans1=tot;
		int ans2=1;
		for(int i=0;i<tot;i++)
		{
			for(int j=prime[i];j<=N;j*=prime[i])
				ans2++;
		}
		printf("%d\n",ans2-ans1);
	}
	return 0;
}

