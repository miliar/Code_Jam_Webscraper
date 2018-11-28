#include <iostream>
#include <algorithm>
using namespace std;

const int maxn=1000+10;
int tot,n;
long long a[maxn],g,ans;

long long gcd(long long x,long long y)
{
	if (y==0) return x;
	return gcd(y,x%y);
}

bool cmp(long long x,long long y)
{
	return (x<y);
}

void init()
{
	scanf("%d",&n);
	for (int i=1;i<=n;++i)
		scanf("%I64d",&a[i]);
	sort(a+1,a+1+n,cmp);
}

void work()
{
	g=a[2]-a[1];
	for (int i=3;i<=n;++i)
		g=gcd(g,a[i]-a[i-1]);
	if (a[1]%g==0) ans=0;
		else       ans=g-(a[1]%g);
}

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&tot);
    for (int tc=1;tc<=tot;++tc)
    {
    	init();
    	work();
    	printf("Case #%d: %I64d\n",tc,ans);
    }
    return 0;
}
