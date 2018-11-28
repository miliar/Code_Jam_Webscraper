#include <cstdio>
#include <algorithm>
using namespace std;

int n, a[850], b[850];
long long ans;

int main ()
{
	int t, i;
	scanf ("%d", &t);
	for (int cnt = 1; cnt <= t; cnt++){
		scanf ("%d", &n);
		for (i = 0; i < n; i++)
			scanf ("%d", &a[i]);
		for (i = 0; i < n; i++)
			scanf ("%d", &b[i]);
		sort (a, a+n);
		sort (b, b+n);
		ans = 0;
		for (i = 0; i < n; i++)
			ans += (long long)(a[i] * b[n-1-i]); 
		printf ("Case #%d: %I64d\n", cnt, ans);
	}
}
