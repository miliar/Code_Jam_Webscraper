#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long ll;
#define REP(i,a)for(int i=0;i<(a);i++)

int T,n,x[800],y[800];

int main()
{
	freopen("A.in","r",stdin);freopen("A.out","w",stdout);
	scanf("%d",&T);
	REP(t,T)
	{
		scanf("%d",&n);
		REP(i,n)scanf("%d",x+i);
		REP(i,n)scanf("%d",y+i);
		sort(x,x+n);
		sort(y,y+n);
		int a=0,b=n-1,c=0,d=n-1;
		ll ans=0;
		while(a<=b&&c<=d)
		{
			if(x[a]<0&&y[d]>0)
			{
				ans+=(ll)x[a]*y[d];
				a++;d--;
				continue;
			}
			if(y[c]<0&&x[b]>0)
			{
				ans+=(ll)y[c]*x[b];
				c++;b--;
				continue;
			}
			break;
		}
		for(int i=a,j=d;i<=b;i++,j--)
			ans+=(ll)x[i]*y[j];
		printf("Case #%d: %I64d\n",t+1,ans);
	}
	return 0;
}
