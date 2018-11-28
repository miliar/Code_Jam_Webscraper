#include<cstdio>
#include<algorithm>
using namespace std;
int t,n;
int x[800], y[800];
long long res;
int main()
{
	freopen ("A-small-attempt0.in", "r", stdin);
	freopen ("output.txt", "w", stdout);
	scanf("%d",&t);
	for (int k = 1; k <= t; ++ k)
	{
		scanf("%d",&n);
		for(int i = 0; i < n; ++ i)
		{
			scanf ("%d", &x[i]);	
		}
		for (int i = 0; i < n; ++ i)
		{
			scanf ("%d", &y[i]);
		}
		sort(x, x + n);
		sort(y, y + n);
		reverse (y, y + n);
		res = 0;
		for (int i = 0; i < n; ++ i)
			res += x[i] * y[i];
		printf ("Case #%d: %I64d\n", k, res);
	}
}
