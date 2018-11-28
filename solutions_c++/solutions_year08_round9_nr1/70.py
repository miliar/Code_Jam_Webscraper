#pragma comment(linker, "/STACK:128000000")
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

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define VI vector<int>
#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef long long ll;

#define NMAX 105

int n;

struct Node
{
	int a, b, c;
};
Node a[NMAX];

void solve(int test)
{
	scanf("%d", &n);
	forn(i, n)
	{
		scanf("%d %d %d", &a[i].a, &a[i].b, &a[i].c);
	}
	int A, B, C;
	int ans = 0;
	forn(i, n)
	{
		forn(j, n)
		{
			A = a[i].a;
			B = a[j].b;
			C = 10000 - A - B;
			int cnt = 0;
			forn(k, n)
			{
				if (A >= a[k].a && B >= a[k].b && C >= a[k].c)
				{
					++cnt;
				}
			}
			ans = max(ans, cnt);
		}
	}
	printf("Case #%d: ", test);
	printf("%d\n", ans);
}
int main()
{
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);

	int tc; scanf("%d\n", &tc);
	forn(it, tc)
	{
		solve(it + 1);
	}
	return 0;
}
         	
