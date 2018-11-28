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
const int NMAX = 200;
int d[NMAX][NMAX];
bool a[NMAX][NMAX];
const int MOD = 10007;
int h, w, r;

bool inside(int x, int y) {
	return x >= 0 && y >= 0 && x < h && y < w && a[x][y] == false;
}

int main()
{
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);
	int tc; cin >> tc;
	for1(it, tc) {
		cin >> h >> w >> r;
		memset(a, 0, sizeof a);
		forn(i, r) {
			int x, y;
			scanf("%d %d", &x, &y);
			x--;
			y--;
			a[x][y] = true;
		}
		d[0][0] = 1;
		forn(i, h) {
			forn(j, w) {
				if (i == 0 && j == 0) continue;
				d[i][j] = 0;
				if (a[i][j]) continue;
				if (inside(i-1, j-2)) d[i][j] += d[i-1][j-2];
				if (inside(i-2, j-1)) d[i][j] += d[i-2][j-1];
				d[i][j] %= MOD;
			}
		}

		printf("Case #%d: %d\n", it, d[h-1][w-1]);
	}

	return 0;
}
