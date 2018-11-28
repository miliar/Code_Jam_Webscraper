#include <stdio.h>
#include <algorithm>

struct node 
{
	int a, b;
	bool operator < (const node &big) const
	{
		return a<big.a;
	}
} a[1010];


int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);	
	
	int T, ti, i, j, ans, n;
	scanf("%d", &T);
	for (ti=1; ti<=T; ti++)
	{
		scanf("%d", &n);
		for (i=0; i<n; i++)
		  scanf("%d%d", &a[i].a, &a[i].b);
		sort(a, a+n);
		ans=0;
		for (i=0; i<n; i++)
		 for (j=i+1; j<n; j++) 
		   if (a[i].b>a[j].b) ans++;
		printf("Case #%d: %d\n", ti, ans);    
	}
	return 0;
}
