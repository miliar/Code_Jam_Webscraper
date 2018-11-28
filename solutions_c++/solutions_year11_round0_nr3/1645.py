#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<string>
#include<queue>
#include<stack>

using namespace std;

#define inf (1<<29)
#define mem(a,b) memset(a,(b),sizeof(a))
#define Max(a,b) ((a) > (b) ? (a) : (b))
#define Min(a,b)  ((a) < (b) ? (a) : (b))

int a[1005];

int main()
{
	freopen("candy2.in","r",stdin);
	freopen("candy2.out","w",stdout);
	int t,cs=0,n,i,ans,mn,sum;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		sum = ans = 0;
		mn = inf;
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			ans ^= a[i];
			mn = Min(a[i],mn);
			sum += a[i];
		}
		if(ans)
			printf("Case #%d: NO\n",++cs);
		else
			printf("Case #%d: %d\n",++cs,sum-mn);
	}
	return 0;
}