#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <sstream>
#include <cstdlib>
#include <cassert>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)

#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair

typedef  vector<int> VI;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"
long long cc[9];

long long add(int x, int y, int z) {
	int a = (x / 3) + (y / 3) + (z / 3);
	int b = x % 3 + y % 3 + z % 3;
	if (a % 3 || b % 3) return 0;
	if (x > y) swap(x, y);
	if (x > z) swap(x, z);
	if (y > z) swap(y, z);

	if (x != y) {
		if (y != z) {
			return cc[x] * cc[y] * cc[z];
		} else {
			return cc[x] * cc[y] * (cc[y] - 1) / 2;
		}	
	} else {
		if (x == z) {
			return cc[x] * (cc[x]-1) * (cc[x]-2) / 6;
		} else {
			return cc[z] * cc[x] * (cc[x] - 1) / 2;
		}
	}
} 


int main()
{
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);

	int tc; cin >> tc;
	forn(it, tc) {
		long long a, b, c, d, x0, y0, x, y, m;
		int n;
		cin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
		x = x0;
		y = y0;
		forn(i, 9) cc[i] = 0;
		forn(i, n) {
			cc[(x%3)*3+y%3]++;
			x = (a * x + b) % m;
			y = (c * y + d) % m;
		}



		long long ans = 0;

		forn(i, 9) {
			forn(j, i + 1) {
				forn(k, j + 1)  {
					ans += add(i, j, k);
				}
			}
		}

		printf("Case #%d: %I64d\n", it + 1, ans);

	}

	return 0;
}
