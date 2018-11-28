#include<stdio.h>

const int N=2048;

int  t, r, kk, n;

long long cots, v[N], k[N], finres;

int Find(int start)
{
	int i, step;
	for( step=1; step<=n; step<<=1);
	for( i=start; step; step>>=1)
		if( i+step<start+n && v[i+step]-v[start-1]<=kk )
			i+=step;
	cots+=v[i]-v[start-1];
	return (i%n)+1;
}

void solve(int tmr)
{
	int x;
	
	cots=0;
	
	scanf("%d%d%d",&r,&kk,&n);
	
	for( int i=1; i<=n; ++i) {
		scanf("%d",&x);
		v[i]=v[i-1]+x;
	}
	
	for( int i=n+1; i<=2*n; ++i)
		v[i]=v[i-1]+v[i-n]-v[i-n-1];
	
	int begin=1, nrstep=0, act;
	
	begin=Find(begin);
	
	finres=cots;
	
	if(r==1)
	{
		printf("Case #%d: %lld\n",tmr,cots);
		return;
	}
	
	r--;
	
	cots=0;
	
	act=Find(begin);
	
	++nrstep;
	
	if(nrstep==r)
	{
		printf("Case #%d: %lld\n",tmr,cots+finres);
		return;
	}
	
	k[nrstep]=cots;
	
	while(act!=begin && nrstep<r )
	{
		++nrstep;
		act=Find(act);
		k[nrstep]=cots;
	}
	
	if(nrstep==r)
	{
		printf("Case #%d: %lld\n",tmr,cots+finres);
		return;
	}
	else
	{
		finres+= cots*(r/nrstep) + k[r%nrstep];
		printf("Case #%d: %lld\n",tmr,finres);
	}
}

int main()
{
	freopen("rc.in","r",stdin);
	freopen("rc.out","w",stdout);
	
	scanf("%d",&t);
	
	for( int i=1; i<=t; ++i)
		solve(i);
	
	return 0;
}
