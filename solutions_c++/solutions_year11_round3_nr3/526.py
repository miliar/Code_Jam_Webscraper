#include<cstdio>
#include<vector>
#include<cstdlib>
#include<climits>
#include<iostream>
#include<memory.h>
#include<algorithm>
#define LL long long
#define _min(a, b) ((a) < (b) ? (a) : (b))
#define _max(a, b) ((a) > (b) ? (a) : (b))
using namespace std;

int l, r, n, T, x, a[1111], f;

int main()
{
//*
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
//*/
	cin>> T;
	for (int tt = 1; tt <= T; tt++)
	{
		int A;
		cin>> n>> l>> r;
		for (int i = 1; i <= n; i++) cin>> a[i];
		for (int ans = l; ans <= r; ans++)
		{
			f = 0;
			for (int i = 1; i <= n; i++) if (ans % a[i] && a[i] % ans)
			{
				f = 1;
				break;
			}
			if (f == 0)
			{
				A = ans;
				break;
			}
		}
		if (f) printf("Case #%d: NO\n", tt);else printf("Case #%d: %d\n", tt, A);
	}
	return 0;
}
