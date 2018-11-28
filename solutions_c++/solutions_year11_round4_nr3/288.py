#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

bool prime[1000015];
int T;
long long n;
long long p[500005];
int cnt;


void init()
{
	for(int i=2;i<=1000005;i++)
	{
		if(!prime[i])
		{
			p[++cnt]=i;
			if(i>1001)
				continue;
			for(int j=i*i;j<=1000005;j+=i)
				prime[j]=true;
		}
	}
	return;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	init();
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		scanf("%lld",&n);
		int ans=0;
		for(int i=1;p[i]*p[i]<=n;i++)
		{
			long long tmp=1;
			int j;
			for(j=-1;tmp<=n;j++)
				tmp*=p[i];
			ans+=j-1;
		}
		printf("Case #%d: %d\n",test,ans+(n>1));
	}
	return 0;
}

		
