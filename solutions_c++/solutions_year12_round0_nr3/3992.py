#include <iostream>
#include <cstdio>
#include <vector>
#include <deque>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <complex>
#include <map>
#include <set>
#include <queue>
#include <ctime>

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define FORN(i, k, n) for(int i = (int)(k); i <= (int)(n); i++)
#define FORD(i, n, k) for(int i = (int)(n); i >= (int)(k); i--)

#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define fi first
#define se second

using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef pair<int, int> pii;

const long double pi = 3.1415926535897932384626433832795;
const long double eps = 0.0000000001;
const int INF = 1E9;
const int MAXN = 10000000;

int t, a, aa, b, len, ppw, ans;
bool used[MAXN];

int main() {

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	cin >> t;
	FORN(i, 1, t) {
		ans = 0;
		cin >> a >> b;
		a = max(a, 10);
		ppw = 1;
		len = 1;
		while (ppw * 10 <= a) {
			ppw *= 10;
			len++;
		}

		FORN(k, a, b) {
			if (k == 10 * ppw) {
				ppw *= 10;
				len++;
			}
			aa = k;
			forn(i, len - 1) {
				aa = (aa % ppw) * 10 + (aa / ppw);
				if (!used[aa] && ppw <= aa && a <= aa && aa <= b && k < aa) {
					ans++;
					used[aa] = 1;
				}
			}

			aa = k;
			forn(i, len - 1) {
				aa = (aa % ppw) * 10 + (aa / ppw);
				used[aa] = 0;
			}
		}
		cout << "Case #" << i << ": " << ans << '\n';
	}

    return 0;
}