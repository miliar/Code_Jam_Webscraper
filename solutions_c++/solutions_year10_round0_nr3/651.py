#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdio>
#include<iomanip>
#include<map>
#include<set>
#include<vector>
#include<list>
#include<deque>
#include<cstdlib>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

const long N=1010*2;

long gk,m,n;
long cy,bgn;
long vis[N];
LL g[N],sum;

struct NEXT
{
	long id;
	LL val;
}next[N];

void myin()
{
	long i;
	cin>>gk>>m>>n;
	for(i=1;i<=n;i++)
	{
		cin>>g[i];
		g[n+i]=g[i];
	}
}

void pre_set()
{
	long i,j;
	for(i=1;i<=n;i++)
	{
		next[i].val=0;
		for(j=i;j<i+n;j++)
		{
			if(next[i].val+g[j]>m)
				break;
			next[i].val+=g[j];
		}
		next[i].id=j;
		if(next[i].id>n)
			next[i].id-=n;
	}

	memset(vis,0,sizeof(vis));
	for(i=1,j=1;;i++,j=next[j].id)
	{
		if(vis[j])
			break;
		vis[j]=i;
	}

	cy=i-vis[j];
	bgn=vis[j];

	sum=0;
	i=j;
	do
	{
		sum+=next[i].val;
		i=next[i].id;
	}while(i!=j);
}

void work()
{
	long i,j;
	LL ans=0;
	pre_set();
	if(gk>=bgn)
	{
		ans=sum*((gk-bgn)/cy);
		gk=(gk-bgn)%cy+bgn;
	}
	for(i=1,j=1;i<=gk;i++,j=next[j].id)
	{
		ans+=next[j].val;
	}
	cout<<ans<<endl;
}

int main()
{
	long i,tests;
	freopen("t1.in","r",stdin);
	freopen("tt.out","w",stdout);
	cin>>tests;
	for(i=1;i<=tests;i++)
	{
		cout<<"Case #"<<i<<": ";
		myin();
		work();
	}
return 0;
}