#include <stdio.h>
#include <algorithm>

using namespace std;

int a[1010];
int n, tot, s;

int main()
{
	int T, i, cas=0;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d", &n);
		tot=s=0;
		for (i=0; i<n; i++)
		{
		  scanf("%d", &a[i]);
		  s^=a[i];
		  tot+=a[i];
		}
		sort(a, a+n);  	
		if (s!=0) printf("Case #%d: NO\n", ++cas);
		else printf("Case #%d: %d\n", ++cas, tot-a[0]);
	}
	return 0;
}