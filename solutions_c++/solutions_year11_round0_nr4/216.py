#include <stdio.h>
#include <algorithm>

using namespace std;

struct node
{
	int v, i;
	bool operator < (const node &o) const
	{
		return v<o.v;
	}
} a[1010];

int t, ans;

int main()
{
	int T, n, i, ans, cas=0;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d", &n);
		for (i=0; i<n; i++)
		{
			 scanf("%d", &a[i].v);
			 a[i].i=i;
		}
		sort(a, a+n);
		ans=0;
		for (i=0; i<n; i++)
		  if (a[i].i!=i) ans++;
		printf("Case #%d: %.8lf\n", ++cas, (double)ans);
	}
	return 0;
}