#include<ctime>
#include<cstdio>
#include<vector>
#include<string>
#include<climits>
#include<cstdlib>
#include<cstddef>
#include<string.h>
#include<iostream>
#include<algorithm>
#define LL long long
#define _max(a, b) ((a) > (b) ? (a) : (b))
#define _min(a, b) ((a) < (b) ? (a) : (b))
#define mp make_pair
using namespace std;

int b[111], n, s, p, x;
pair<int, pair<int, int> > a[111];

int main()
{
//*
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
//*/
	int T;
	cin>> T;
	for (int test = 1; test <= T; ++test)
	{
		int ans = 0;
		cin>> n>> s>> p;
		for (int i = 0; i < n; i++)
		{
			cin>> x;
			if (x % 3 == 0) a[i] = mp(x / 3, mp(x / 3, x / 3));
			if (x % 3 == 1) a[i] = mp(x / 3, mp(x / 3, x - x / 3 * 2));
			if (x % 3 == 2) a[i] = mp(x / 3, mp((x - x / 3) / 2, (x - x / 3) / 2));
			b[i] = x;
		}
		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++)
				if (a[i].second.second > a[j].second.second)
				{
					swap(a[i], a[j]);
					swap(b[i], b[j]);
				}
		a[n].second.second = p;
		for (int j = 0; j <= n; j++) if (a[j].second.second >= p)
		{
			ans = n - j;
			for (int i = j - 1; i >= 0; i--)
			{
				if (!s || b[i] < 2) break;
				if (b[i] % 3 == 0 && a[i].second.second + 1 >= p) ++ans, --s;
				if (b[i] % 3 == 2 && a[i].second.second + 1 >= p) ++ans, --s;
			}
			break;
		}
		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}
