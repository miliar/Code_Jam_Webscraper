#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>

#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <list>

#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) a.size() - 1
#define all(a) a.begin(), a.end()
#define I (int)
#define I64 (long long)
#define LD (long double)
#define VI vector<int>
#define pti pair<int, int>
#define ptd pair<long double, long double>
#define sqr(x) ((x) * (x))

const long double EPS = 1E-9;
const int INF = (int)1E9;
const long long INF64 = (long long)1E18;
const long double PI = 2 * acos(.0);

typedef long double ld;
typedef long long ll;

int sq (int x1, int y1, int x2, int y2, int x3, int y3)
{
	return (x1*y2-x1*y3)+(x2*y3-x2*y1)+(x3*y1-x3*y2);
}

struct segment {
	int x1,y1,x2,y2;
	segment(){}
	segment(int x1, int y1, int x2, int y2):x1(x1), y1(y1), x2(x2), y2(y2) {
	}
};

bool cross (segment a, segment b)
{
	__int64
		sq11=sq(a.x1,a.y1,a.x2,a.y2,b.x1,b.y1),
		sq12=sq(a.x1,a.y1,a.x2,a.y2,b.x2,b.y2),
		sq21=sq(b.x1,b.y1,b.x2,b.y2,a.x1,a.y1),
		sq22=sq(b.x1,b.y1,b.x2,b.y2,a.x2,a.y2);
	if (sq11==0 && sq12==0 && sq21==0 && sq22==0)
		return max(b.x1,b.x2) >= min(a.x1,a.x2) && min(b.x1,b.x2) <= max(a.x1,a.x2) &&
			max(b.y1,b.y2) >= min(a.y1,a.y2) && min(b.y1,b.y2) <= max(a.y1,a.y2);
	return (sq11*sq12<=0) && (sq21*sq22<=0);
}

int n, k;
int a[100][100];
bool g[100][100];

int d[100500];
bool can[100500];

bool isGood(int x) {
	forn(i, n) {
		forn(j, n) {
			if (i != j && ((1 << i) & x) != 0 &&
				((1 << j) & x) != 0 && !g[i][j]) {
					return false;
			}
		}
	}

	return true;
}

void solve(int test) {
	scanf("%d%d", &n, &k);
	memset(g, 0, sizeof(g));
	memset(d, 60, sizeof(d));

	forn(i, n)
		forn(j, k)
		scanf("%d", &a[i][j]);
	

	forn(i, n) {
		forn(j, n) {
			g[i][j] = true;
			forn(t1, k - 1) {
				forn(t2, k - 1) {
					if (cross(segment(t1, a[i][t1], t1 + 1, a[i][t1 + 1]), 
						segment(t2, a[j][t2], t2 + 1, a[j][t2 + 1]))) {
							g[i][j] = false;
							break;
					}
				}
			}
		}
	}

	forn(i, (1 << n))
		can[i] = isGood(i);

	d[0] = 0;
	queue<int> q;
	q.push(0);

	while (!q.empty()) {
		int cur = q.front();
		q.pop();
		int dx = (1 << n) - 1;
		dx ^= cur;

		for (int msk = dx; msk != 0; msk = (msk - 1) & dx) {
			if (can[msk] && d[cur] + 1 < d[cur + msk]) {
				d[cur + msk] = d[cur] + 1;
				q.push(cur + msk);
			}
		}
	}

	printf("Case #%d: %d\n", test, d[(1 << n) - 1]);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int t;
	scanf("%d", &t);
	forn(i, t)
		solve(i + 1);
	
    return 0;
}
