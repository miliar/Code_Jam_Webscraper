#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
typedef __int64 int64;

int T,n,i,j,k,cas;
int64 x[1000],y[1000],ans;

int main()
{
	scanf("%d",&T);
	cas = 0;
	while (T--)
	{
		ans = 0;
		scanf("%d",&n);
		for (i=0;i<n ;i++ )
		{
			scanf("%I64d",&x[i]);
		}
		sort(x,x+n);
		for (i=0;i<n ;i++ )
		{
			scanf("%I64d",&y[i]);
		}
		sort(y,y+n);

		for (i=0;i<n ;i++)
		{
			ans+=x[i]*y[n-i-1];
		}
		printf("Case #%d: ",++cas);
		printf("%I64d\n",ans);
	}

	return 0;
}
