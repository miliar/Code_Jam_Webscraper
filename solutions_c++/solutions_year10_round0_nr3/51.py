#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define pb push_back
#define mp make_pair

typedef long long li;
typedef pair<int, int> pt;
typedef long double ld;

const ld PI = 2 * acos(0.0);
const int N = 1100;
const int Z = 1000;

int a[N], to[N], c[N], bto[N];
li bc[N];

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("outp.txt", "wt", stdout);

	int t;
	scanf("%d", &t);
	for1(it, t)
	{
		memset(a, 0, sizeof a);
		memset(to, 0, sizeof to);
		memset(c, 0, sizeof c);
		memset(bto, 0, sizeof bto);
		memset(bc, 0, sizeof bc);
		int r, k, n;
		scanf("%d%d%d", &r, &k, &n);
		forn(i, n)
			scanf("%d", &a[i]);

		li ans = 0;

		bool flag = true;

		forn(i, n)
		{
			int j;
			for(j = 0; j < n; ++j)
			{
				int id = (i + j) % n;
				if(a[id] <= k)
					break;
			}
			if(j >= n)
			{
				flag = false;
				break;
			}

			int cost = 0;
			for(; j < n; ++j)
			{
				int id = (i + j) % n;
				if(cost + a[id] <= k)
					cost += a[id];
				else
					break;
			}
			to[i] = (i + j) % n;
			c[i] = cost;
		}
		
		forn(i, n)
			bto[i] = i;

		forn(ir, Z)
		{
			forn(i, n)
			{
				bc[i] += c[bto[i]];
				bto[i] = to[bto[i]];
			}
		}
		
		int cur = 0;
		if(flag)
		{
			for(int i = 0, end = r / Z; i < end; ++i)
			{
				ans += bc[cur];
				cur = bto[cur];
			}
			for(int i = 0, end = r % Z; i < end; ++i)
			{
				ans += c[cur];
				cur = to[cur];
			}
		}

		cout << "Case #" << it << ": " << ans << endl;
	}

	return 0;
}
