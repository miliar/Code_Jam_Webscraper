#include "stdio.h"
#include "algorithm"
using namespace std;


int main()
{
	freopen("CA-small.in","r",stdin);
	freopen("CA-small.out","w",stdout);
	int t;
	scanf("%d", &t);
	int now = 1;
	while (now <= t)
	{
		int x[900];
		int y[900];
		int n;
		scanf("%d", &n);
		int i;
		for (i=1; i<=n; i++)
		{
			scanf("%d", &x[i]);
		}
		for (i=1; i<=n; i++)
		{
			scanf("%d", &y[i]);
		}
		sort(x+1, x+n+1);
		sort(y+1, y+n+1);
		__int64 sum = 0;
		for (i=1; i<=n; i++)
		{
			sum += x[i]*y[n-i+1];
		}
		printf("Case #%d: %I64d\n", now, sum);
		now++;
	}
}