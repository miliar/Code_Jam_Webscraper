#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <iostream>
#include <cmath>
#include <set>
#include <ctime>
#include <algorithm>
#define min(a,b)	((a)<(b)?(a):(b))
#define max(a,b)	((a)>(b)?(a):(b))
#define abs(a)	((a)<0?-(a):(a))
#define inf 214748364
#define pi 3.141592653589793
using namespace std;
typedef long long ll;

const int maxn = 1000001;
int tim,n,f[maxn],l[maxn],d[maxn];

bool work()
{
	f[1]=d[1];
	for(int i=2;i<=n;++i)
	{
		f[i]=-1;
		for(int j=i-1;j>=1;--j)
		if(f[j]>=d[i]-d[j])
			f[i]=max(f[i],min(d[i]-d[j],l[i]));
	}
	return f[n]>=0;
}


int main()
{
	#ifndef ONLINE_JUDGE
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	#endif
	scanf("%d",&tim);
	for(int tt=1;tt<=tim;++tt)
	{
		printf("Case #%d: ",tt);
		scanf("%d",&n);
		for(int i=1;i<=n;++i)
			scanf("%d%d",&d[i],&l[i]);
		n++;
		scanf("%d",&d[n]);
		l[n]=0;
		if(work())
			printf("YES\n");else
			printf("NO\n");
	}
	return 0;
}

