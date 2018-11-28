#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <deque>
#include <bitset>

#define sqr(x) ((x) * (x))
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define y0 ywuerosdfhgjkls
#define y1 hdsfjkhgjlsdfhgsdf
#define j1 j924
#define j0 j2834
#define sqrt(x) (sqrt(abs(x)))
#define re return
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end()
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rrep(i, n) for (int i = ((n) - 1); i >= 0; i--)
#define fill(a, x) memset(a, x, sizeof(a))

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair <int, int> ii;
typedef vector <int> vi;
typedef vector <ii> vii;
typedef vector <vi> vvi;
typedef double D;
typedef vector <string> vs;

template <class T> inline T abs(T a) {
	return a > 0 ? a : -a;
}

int w, l;
int n;
int m;

int r[1000], p[1000];

int xx[1000], yy[1000];

const int dx[3] = {-1, 0, 1};
const int dy[3] = {-1, 0, 1};

bool Try(int X, int Y, int num) {
	if (X < 0 || Y < 0 || X > w || Y > l)
		re false;
	int cur = p[num];
	int Lx = X - r[cur];
	int Ly = Y - r[cur];
	int Rx = X + r[cur];
	int Ry = Y + r[cur];
	rep(i, num) {
		int gom = p[i];
		int lx = xx[gom] - r[gom];
		int ly = yy[gom] - r[gom];
		int rx = xx[gom] + r[gom];
		int ry = yy[gom] + r[gom];
		if (max(lx, Lx) < min(rx, Rx) && max(ly, Ly) < min(ry, Ry))
			re false;
	}
	re true;
}

int main() {
	int T;
	cin >> T;
	rep(I, T) {
		cerr << I << endl;
		cin >> n;
		cin >> w >> l;
		rep(i, n) {
			cin >> r[i];
			p[i] = i;
		}
		while (1) {
			set <int> X;
			set <int> Y;
			X.insert(0);
			X.insert(w);
			Y.insert(0);
			Y.insert(l);
			bool kpyto = true;
			rep(i, n) {
				kpyto = false;
				int cur = p[i];
				for (set <int> :: iterator x = X.begin(); x != X.end(); x++) {
					for (set <int> :: iterator y = Y.begin(); y != Y.end(); y++) {
						rep(p, 3)
						rep(q, 3)
							if (Try(*x + r[cur] * dx[p], *y + r[cur] * dy[p], i)) {
								xx[cur] = *x + r[cur] * dx[p];
								yy[cur] = *y + r[cur] * dy[p];
								X.insert(xx[cur] - r[cur]);
								X.insert(xx[cur] + r[cur]);
								Y.insert(yy[cur] - r[cur]);
								Y.insert(yy[cur] + r[cur]);
								kpyto = true;
								goto HAX;
							}
					}
				}
				HAX:
				//cerr << i << ' ' << kpyto << ' ' << n << endl;
				if (!kpyto)
					break;
			}
//			cerr << kpyto << endl;
			if (kpyto) {
				break;
			}
			random_shuffle(p, p + n);
		}
		cout << "Case #" << I + 1 << ":";
		rep(i, n)
			cout << ' ' << xx[i] << ' ' << yy[i];
		cout << endl;
//		re 0;
	}
	return 0;
}
