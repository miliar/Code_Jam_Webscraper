#include <stdio.h>
#include <algorithm>
using namespace std;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int n;
	scanf("%d", &n);
	int now=1;
	while (now<=n)
	{
		int p,k,l;
		scanf("%d",&p);
		scanf("%d",&k);
		scanf("%d",&l);
		int f[1010], i;
		for (i=0; i<l; i++)
		{
			scanf("%d", &f[i]);
		}
		sort(f, f+l);
		int sum=0;
		for(i=l-1; i>=0; i--)
		{
			int t = (l-i-1)/k+1;
			sum += t*f[i];
		}
		printf("Case #%d: %d\n", now, sum);
		now++;
	}
	return 0;
}