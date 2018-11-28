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

int main()
{
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);

	int tc; cin >> tc;
	for1(it, tc) {
		int a, n, m;
		cin >> n >> m >> a;
		bool f = false;
			
		forn(x1, n+1) {
			if (f) break;
			forn(y1, m+1) {
				if (f) break;
				forn(x2, n+1) {
					if (f) break;
					forn(y2, m+1) {
			            if (abs(x1 * y2 - x2 * y1) != a) continue;
						f = true;
						printf("Case #%d: %d %d %d %d %d %d\n", it, 0, 0, x1, y1, x2, y2);
						break;
					}
				}
			}	
		}
		if (!f) {
			printf("Case #%d: IMPOSSIBLE\n", it);
		}
	}

	return 0;
}
