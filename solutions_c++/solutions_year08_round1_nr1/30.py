#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cassert>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for (int i = 1; i <= int(n); i++)

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

typedef pair<int, int> pii;
typedef vector<int> VI;

#define NMAX 1005

int n;
int x[NMAX], y[NMAX];

void solve(int test)
{
    scanf("%d", &n);
    forn(i, n)
    {
    	scanf("%d", &x[i]);
    }
    forn(i, n)
    {
    	scanf("%d", &y[i]);
    }

    sort(x, x + n);
    sort(y, y + n);
    reverse(y, y + n);

    long long ans = 0;
    forn(i, n)
    {
    	ans += (long long)(x[i]) * (long long)(y[i]);
    }

	printf("Case #%d: %I64d\n", test, ans);
}
int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc; scanf("%d\n", &tc);
	forn(it, tc)
	{
		solve(it + 1);
	}

	return 0;
}
