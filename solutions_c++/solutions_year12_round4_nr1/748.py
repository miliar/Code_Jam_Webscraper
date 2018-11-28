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

int n;
int m;

int l[100000];
int x[100000];

int h[100000];

int main() {
	int T;
	cin >> T;
	rep(I, T) {
		cerr << I << endl;
		int L;
		cin >> n;
		rep(i, n) {
			cin >> x[i] >> l[i];
			h[i] = 0;
		}
		cin >> L;
		h[0] = x[0];
		bool kpyto = false;		
		for (int i = 0; i < n; i++) {
			for (int j = 1; j < n; j++) {
				if (x[j] - x[i] <= h[i]) {
					h[j] = max(h[j], min(l[j], x[j] - x[i]));
				} else
					break;
			}
			if (L - x[i] <= h[i]) {
				kpyto = true;
				break;
			}
		}
		
		cout << "Case #" << I + 1 << ": " << (!kpyto ? "NO" : "YES") << endl;
		//re 0;
	}
	return 0;
}
