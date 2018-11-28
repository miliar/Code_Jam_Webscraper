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

int R, C, opt;
int A[100][100];
bool take[100][100];

int dx[] = {0, 0, 1, -1, 1, 1, -1, -1, 0};
int dy[] = {1, -1, 0, 0, 1, -1, 1, -1, 0};

bool cool(int x, int y) {
	return x >= 0 && x < R && y >= 0 && y < C;
}

void bt(int cx, int cy) {
	if (cx == R) {
		bool ok = false;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (A[i][j]) {
					ok = false;
					break;
				}
			}
		}
		int cur = 0;
		for (int i = 0; i < C; i++) {
			if (take[R / 2][i]) cur++;
		}
		opt = max(opt, cur);
		return;
	}
	if (cy == C) {
		bt(cx + 1, 0);
		return;
	}
	if (!cool(cx - 1, cy - 1) || !A[cx - 1][cy - 1]) {
		bt(cx, cy + 1);
	}
	bool ok = true;
	for (int i = 0; i < 9; i++) {
		int nx = cx + dx[i];
		int ny = cy + dy[i];
		if (!cool(nx, ny)) continue;
		if (!A[nx][ny]) {
			ok = false;
			break;
		}
	}
	if (!ok) return;
	take[cx][cy] = true;
	for (int i = 0; i < 9; i++) {
		int nx = cx + dx[i];
		int ny = cy + dy[i];
		if (!cool(nx, ny)) continue;
		A[nx][ny]--;
	}
	if (!cool(cx - 1, cy - 1) || !A[cx - 1][cy - 1]) {
		bt(cx, cy + 1);
	}
	for (int i = 0; i < 9; i++) {
		int nx = cx + dx[i];
		int ny = cy + dy[i];
		if (!cool(nx, ny)) continue;
		A[nx][ny]++;
	}
	take[cx][cy] = false;
}

void solve(int it) {
	cin >> R >> C;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cin >> A[i][j];
		}
	}
	opt = 0;
	bt(0, 0);
	printf("Case #%d: %d\n", it, opt);
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
