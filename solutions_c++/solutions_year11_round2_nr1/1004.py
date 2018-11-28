#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <complex>

#define pb push_back
#define mp make_pair
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define tr(c, i) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define rtr(c, i) for (typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); --i)
#define contains(c, x) ((c).find(x) != (c).end())
#define Contains(c, x) (find(all(c), x) != (c).end())
#define REP(i, a, b) for (int i = (a); i < (b); ++i)
#define rep(i, n) REP(i, 0, (n))
#define To_String to_string< char,std::char_traits<char>,std::allocator<char> >

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	int T; cin >> T;
	REP(X, 1, T+1) {
		int n; cin >> n;
		vector<string> a(n);
		vector<double> rpi(n, 0), wp(n, 0), owp(n, 0), oowp(n, 0);
		vector<int> m(n, 0);
		rep(i, n) {
			cin >> a[i];
			m[i] = n - count(all(a[i]), '.');
			wp[i] = (double)count(all(a[i]), '1') / m[i];
		}
		rep(i, n) {
			vector<double> w(n, 0);
			rep(j, n) if (a[i][j] != '.') {
				int c = 0;
				rep(k, n) if (i != k && a[j][k] == '1') c++;
				w[j] = (double)c / (m[j] - 1);
			}
			owp[i] = accumulate(all(w), 0.0) / m[i];
		}
		rep(i, n) {
			double t = 0;
			rep(j, n) if (a[i][j] != '.') t += owp[j];
			oowp[i] = t / m[i];
		}
		rep(i, n) rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
		cout << "Case #" << X << ":" << endl;
		rep(i, n) cout << setprecision(10) << rpi[i] << endl;
	}
	return 0;
}
