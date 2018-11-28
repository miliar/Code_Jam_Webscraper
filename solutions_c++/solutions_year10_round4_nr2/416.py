#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

const int inf=200000000;
int d[17];
int p,n,T;
int M[1027];
bool b[2051][2051];
long long f[2051][2051];
int price[2051];

int lowbit(int x)
{
	return (x&(-x));
}
void init()
{
	d[0]=1;
	for(int i=1;i<=15;i++)
		d[i]=d[i-1]<<1;
}

int dep(int now)
{
	for(int i=0;;i++)
		if(d[i]>now)
			return i-1;
}

long long dp(int now,int pre)
{
	if(dep(now)==p)
	{
		int tmp=0;
		while(pre)
		{
			tmp++;
			pre-=lowbit(pre);
		}
		if(M[now-d[p]]<p-tmp)
			return inf;
		return 0;
	}
	if(!b[now][pre])
	{
		b[now][pre]=true;
		f[now][pre]=min(dp(now*2,pre)+dp(now*2+1,pre),price[now]+dp(now*2,pre|(1<<dep(now)))+dp(now*2+1,pre|(1<<dep(now))));
	}
	return f[now][pre];
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	init();
	int test=0;
	while(T--)
	{
		memset(f,0,sizeof(f));
		memset(b,0,sizeof(b));
		scanf("%d",&p);
		for(int i=0;i<(1<<p);i++)
			scanf("%d",&M[i]);
		for(int i=p-1;i>=0;i--)
			for(int j=d[i];j<d[i+1];j++)
				scanf("%d",&price[j]);
		printf("Case #%d: %I64d\n",++test,dp(1,0));
	}
	return 0;
}
