#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <numeric>
#include <sstream>
#include <ctime>

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

ll pg, pd, n;

long long ee(long long a, long long b, long long &x, long long &y)
{
	if(b == 0)
	{
		x = 1;
		y = 0;
		return a;	
	}
	long long x1, y1;
	long long d = ee(b, a % b, x1, y1);
	x = y1;
	y = x1 - (a / b) * y1;
	return d;
} 

void solve(int tc)
{
	printf("Case #%d: ", tc);
	cin >> n >> pd >> pg;

	int cnt = 1000;

	for (ll d = 1; d <= n && cnt >= 0; d++)
	{
		if ((pd * d) % 100) continue;
		ll wd = pd * d / 100;
		cnt--;

		for (ll g = d; g <= d * 100; g++)
		{
			if ((pg * g) % 100) continue;
			ll wg = (pg * g) / 100;
			if (wg >= wd && g - wg >= d - wd)
			{
				printf("Possible\n");
				return;
			}
		}
	}

	printf("Broken\n");
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);
    int tc;
    cin >> tc;
    forn(it, tc) solve(it + 1);
    return 0;
}
            
