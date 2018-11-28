#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define foreach(i, n) for (__typeof(n.begin()) i = n.begin(); i != n.end(); ++i)
#define sqr(x) ((x)*(x))
#define clr(a, b) memset(a, b, sizeof(a))
#define MP make_pair
#define PB push_back
#define SZ(a) ((int)a.size())
#define all(a) (a).begin(),(a).end()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const double eps = 1e-9;
const double pi = acos(-1.0);
const int inf = 0x3f3f3f3f;
int dcmp(double x) { if (x < -eps) return -1; else return x > eps;}
#define se(x) cout<<#x<<" = "<<x<<endl

const int N = 2010;
int y[N];
int x[N];
int n;

bool chk(int bg, int ed) {
	for (int i = bg + 1; i < ed; ++i) {
		if (x[i] > ed) {
			return false;
		}
		if (!chk(i, x[i])) {
			return false;
		}
	}
	return true;
}

bool check() {
	for (int i = 1; i < n; ++i) {
		if (y[i] < 0 || y[x[i]] < 0) continue;
		double d = (y[x[i]] - y[i]) * 1.0 / (x[i] - i);
		for (int j = i + 1; j <= n; ++j) {
			if (y[j] < 0) continue;
			double f = (y[j] - y[i]) * 1.0 / (j - i);
			if (dcmp(f - d) > 0) return false;
		}
	}
	return true;
}


void solve() {
	scanf("%d", &n);
	clr(y, -1);
	for (int i = 1; i < n; ++i) {
		scanf("%d", x + i);
	}
	if (!chk(0, n)) {
		puts("Impossible");
		return;
	}
	for (int i = 1; i < n; ++i) {
		if (y[i] < 0) {
			y[i] = 0;
		}
		forn (j, 12000) {
			if (check()) break;
			y[i]++;
		}


		int s = x[i];
		if (y[s] < 0) {
			y[s] = y[i] + 40 * (x[i] - i);
		}
		forn (j, 12000) {
			if (check()) break;
			y[s]++;
		}
		if (!check()) {
			y[s] -= 12000;
			forn (j, 12000) {
				if (check()) break;
				y[s]--;
			}
		}
	}
	for (int i = 1; i <= n; ++i) {
		if (i != 1) printf(" ");
		printf("%d", y[i]);
	}
	printf("\n");

}

int main() {
//	freopen("in","r",stdin);
//	freopen("in.txt","r",stdin);
//	freopen("C-small-practice.in","r",stdin);freopen("C-small-practice.out","w",stdout);
//	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
	freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
//	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int cas;
	scanf("%d", &cas);
	for (int i = 1; i <= cas; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
