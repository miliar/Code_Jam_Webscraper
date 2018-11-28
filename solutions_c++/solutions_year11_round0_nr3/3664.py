#include <stdio.h>
#include <algorithm>
using namespace std;

int n,a[1100];
int cs,cn = 1;

int main()
{
	int i,j;
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&cs);
	while(cs--)
	{
		scanf("%d",&n);
		int sum1 = 0,sum2 = 0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			sum1 ^= a[i];
			sum2 += a[i];
		}
		if(sum1 != 0)
		{
			printf("Case #%d: NO\n",cn++);
		}
		else
		{
			sort(a,a+n);
			printf("Case #%d: %d\n",cn++,sum2-a[0]);
		}
	}
	return 0;
}
