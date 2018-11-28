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

long long cnt[3][3];

#define NMAX 100005

int x[NMAX], y[NMAX];

void solve(int tc)
{
	memset(cnt, 0, sizeof(cnt));
	int n;
	long long A, B, C, D, x0, y0, M;
	cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
	x[0] = (int)x0;
	y[0] = (int)y0;
	for1(i, n - 1)
	{
		x0 = (A * x0 + B) % M;
		y0 = (C * y0 + D) % M;
		x[i] = (int)x0;
		y[i] = (int)y0;
	}	
	forn(i, n)
	{
		cnt[x[i] % 3][y[i] % 3]++;
	}
	long long ans = 0;
	forn(x1, 3)
	{
		forn(y1, 3)
		{
			forn(x2, 3)
			{
				forn(y2, 3)
				{
					forn(x3, 3)
					{
						forn(y3, 3)
						{
							if ((x1 + x2 + x3) % 3) continue;
							if ((y1 + y2 + y3) % 3) continue;
							long long c1 = cnt[x1][y1];
							if (c1 == 0) continue;
							long long c2 = cnt[x2][y2];
							if (x1 == x2 && y1 == y2) --c2;
							if (c2 == 0) continue;
							long long c3 = cnt[x3][y3];
							if (x1 == x3 && y1 == y3) --c3;
							if (x2 == x3 && y2 == y3) --c3;
							if (c3 == 0) continue;
							ans += c1 * c2 * c3;
						}
					}
				}
			}
		}
	}
	printf("Case #%d: %I64d\n", tc, ans / 6);
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
         	
