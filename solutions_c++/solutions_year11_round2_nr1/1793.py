#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <list>
#include <stack>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <memory.h>
#include <cstdio>
#include <cstdlib>
        
using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = n - 1 ; i >= 0 ; i--)
#define forv(i, a) for (int i = 0; i < (int)(a.size()); i++)
#define forab(i, a, b) for (int i = a; i < (int)(b); i++)
#define fordab(i, a, b) for (int i = b - 1; i >= (int)(a); i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define pi 3.1415926535897932
#define all(a) a.begin(), a.end()

typedef long long int64;       
typedef long double ld;

vector<string> a;
vector<int> w, s;
vector<ld> wp, owp;

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout.precision(10);
	int t;
	cin >> t;
	forn (q, t) {
		int n;
		cin >> n;
		a.resize(n);
		forn (i, n) {
			cin >> a[i];
		}
		cout << "Case #" << q + 1 << ":" << endl;
		w.assign(n, 0);
		s.assign(n, 0);
		wp.assign(n, 0);
        owp.assign(n, 0);
		forn (i, n) {
			forn (j, n) {
				w[i] += (a[i][j] == '1');
				s[i] += (a[i][j] != '.');
			}
		}
		forn (i, n) {
			wp[i] = ld(w[i]) / ld(s[i]);
			owp[i] = 0;
			forn (j, n) {
				if (a[i][j] == '.') {
					continue;
				}
				owp[i] += ld(w[j] - (a[i][j] == '0')) / ld(s[j] - 1);
			}
			owp[i] /= ld(s[i]);
		}
		forn (i, n) {
			ld oowp = 0;
			forn (j, n) {
				if (a[i][j] == '.') {
					continue;
				}
				oowp += owp[j];
			}
			oowp /= ld(s[i]);
//			cout << wp[i] << " " << owp[i] << " " << oowp << endl;
			cout << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp << endl;
		}
	}
}
