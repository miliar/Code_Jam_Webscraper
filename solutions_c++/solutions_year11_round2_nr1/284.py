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

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define clr(a) memset(a, 0, sizeof(a))
#define fil(a, b) memset(a, b, sizeof(a));
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define se(x) cout<<#x<<" = "<<x<<endl

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair <int, int> pii;

const int N = 110;
char tab[N][N];
int win[N], m[N];
double owp[N];
int n;

void solve(int cas) {
	printf("Case #%d:\n", cas);
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%s", tab[i]);
	}
	memset(win, 0, sizeof(win));
	memset(m, 0, sizeof(m));
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			if (tab[i][j] == '.') continue;
			m[i]++;
			win[i] += tab[i][j] == '1';
		}
	}
	for (int i = 0; i < n; ++i) {
		owp[i] = 0;
		for (int j = 0; j < n; ++j) {
			if (tab[i][j] == '.') continue;
			int a = win[j] - (tab[j][i] == '1');
			int b = m[j] - 1;
			owp[i] += a * 1.0 / b;
		}
		owp[i] /= m[i];
	}
	for (int i = 0; i < n; ++i) {
		double rpi = 0.25 * win[i] / m[i] + 0.5 * owp[i];
//		printf("%lf,%lf,", win[i] * 1.0 / m[i], owp[i]);
//		rpi = 0;
		for (int j = 0; j < n; ++j) {
			if (tab[i][j] == '.') continue;
			rpi += owp[j] * 0.25 / m[i];
		}
		printf("%.9lf\n", rpi);
	}
}

int main() {
//	freopen("in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int cas;
	scanf("%d", &cas);
	for (int i = 1; i <= cas; ++i) {
		solve(i);
	}
	return 0;
}
