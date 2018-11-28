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

#define NMAX 1005

#define EPS 1e-9

struct Rec
{
	int l, r, w;
};

inline bool operator<(const Rec& r1, const Rec& r2)
{
	return r1.w < r2.w;
}

ld R, S, X;
ld t;
Rec a[NMAX];
int n;

void solve(int tc)
{
	printf("Case #%d: ", tc);
	cin >> X >> S >> R >> t >> n;
	forn(i, n)
	{
		cin >> a[i].l >> a[i].r >> a[i].w;
		X -= (a[i].r - a[i].l);
	}
	sort(a, a + n);

	ld ans = 0;

	ld trun = X / R;
	if (trun < t + EPS)
	{
		ans += trun;
		t -= trun;
	}
	else
	{
		X -= t * R;		
		ans += t;
		t = 0;
		ans += X / S;
	}

	forn(i, n)
	{
		ld len = a[i].r - a[i].l;		

		ld trun = len / (a[i].w + R);

		if (trun < t + EPS)
		{
			ans += trun;
			t -= trun;	
		}
		else
		{
			len -= t * (a[i].w + R);
			ans += t;
			t = 0;
			ans += len / (a[i].w + S);
		}
	}

	printf("%.8lf\n", (double)ans);
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
            
