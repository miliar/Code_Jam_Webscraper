#include <iostream>
#include <algorithm>


using namespace std;


int a[10146];


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for(int _ = 0; _ < t; _++)
	{
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		sort(a, a + n);
		int res = 0;
		for(int i = 0; i < n; i++)
			res ^= a[i];
		int ans = 0;
		for(int i = 1; i < n; i++)
			ans += a[i];
		if(res != 0)
			printf("Case #%d: NO\n", _ + 1);
		else
			printf("Case #%d: %d\n", _ + 1, ans);
	}
}