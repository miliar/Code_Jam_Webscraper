#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:64000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<bool> vb;
typedef double D;

template<class T> T sqr(T x) { return x * x;            }
template<class T> T abs(T x) { return (x > 0) ? x : -x; }

struct P {
	D x, y;

	P() {}
	P(D x, D y): x(x), y(y) {}

	P operator + (P a) { return P(x + a.x, y + a.y); }
	P operator - (P a) { return P(x - a.x, y - a.y); }
	P operator * (D a) { return P(x * a, y * a); }
	D operator * (P a) { return x * a.y - y * a.x;   }
	D operator ^ (P a) { return x * a.x + y * a.y;   }

	D len2() { return sqr(x) + sqr(y); }
	D len()  { return sqrt(len2());    }
	P orth() { return P(y, -x);        }
};

struct L {
	D a, b, c;

	L() {}
	L(D a, D b, D c): a(a), b(b), c(c) {}
	L(P p1, P p2) {
		a = p1.y - p2.y;
		b = p2.x - p1.x;
		c = -p1.x * a - p1.y * b;
	}
};

struct C {
	P c;
	D r;

	C() {}
	C(P c, D r): c(c), r(r) {}
};

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)((x).size()))

int W, H;
int DX1, DY1, DX2, DY2, X0, Y0;
queue<ii> q;
bool was[110][110];

bool cool(int x, int y) {
	return x >= 0 && x < W && y >= 0 && y < H;
}

void relax(int x1, int y1, int x2, int y2) {
	if (!cool(x2, y2)) return;
	if (was[x2][y2]) return;
	was[x2][y2] = true;
	q.push(mp(x2, y2));
}

void solve(int it) {
	cin >> W >> H;
	cin >> DX1 >> DY1 >> DX2 >> DY2 >> X0 >> Y0;
	memset(was, 0, sizeof(was));
	was[X0][Y0] = true;
	int cur = 0;
	q.push(mp(X0, Y0));
	while (!q.empty()) {
		ii cp = q.front();
		q.pop();
		cur++;
		relax(cp.first, cp.second, cp.first + DX1, cp.second + DY1);
		relax(cp.first, cp.second, cp.first + DX2, cp.second + DY2);
	}
	printf("Case #%d: %d\n", it, cur);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nt;
	cin >> nt;
	for (int it = 1; it <= nt; it++) {
		solve(it);
	}
	return 0;
}
