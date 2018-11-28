#include<cstdio>
#include<cstring>
#define N 1024
#define ll long long 
int r,k,n;
int g[N];
ll a[N];
int next[N];
ll rez;
inline bool citire()
{
	scanf("%d%d%d",&r,&k,&n);
	ll aux=0;
        for(int i=1; i<=n; ++i)
	{
		scanf("%d",&g[i]);
		aux+=(ll)g[i];
	}

	if(aux<=k)
	{
        	printf("%lld\n",aux*(ll)r);
		return true;
	}
	return false;
}
inline void rezolva()
{
	int v[N+N];
	rez=0;
	for(int i=1; i<=n; ++i)
		v[i]=i;
	for(int i=n+1; i<=n+n; ++i)
		v[i]=i-n;

	int k1;
	int j,lim;
	for(int i=1; i<=n; ++i)
	{
		k1=k;
		a[i]=0;
		for(j=i,lim=i+n; j<lim && k1>=g[v[j]]; ++j)
		{
                	a[i]+=g[v[j]];
			k1-=g[v[j]];
		}
                next[i]=v[j];
	}

	int x=1;
	while(r!=0)
	{
		--r;
		rez+=a[x];
		x=next[x];
	}

	printf("%lld\n",rez);
}
int main()
{
	freopen("park.in","r",stdin);
	freopen("park.out","w",stdout);

	int T;
	scanf("%d",&T);
	for(int i=1; i<=T; ++i)
	{
		printf("Case #%d: ",i);
		if(citire())
			continue;
		rezolva();
	}

	return 0;
}

