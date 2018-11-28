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

vector<pair<int, int> > x, y;

int main() { 
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	forn (q, t) {
		int n;
		cin >> n;
		x.clear();
		y.clear();
		forn (i, n) {
			char c;
			cin >> c;
			int f;
			cin >> f;
			if (c == 'O') {
				x.pb(mp(i, f));
			} else {
				y.pb(mp(i, f));
			}
		}
		int i = 0, j = 0, a = 0, b = 0, ans = 0, xs = x.size(), ys = y.size();
		x.pb(mp(10000, 0));
		y.pb(mp(10000, 0));
		while (a < xs || b < ys) {
			ans++;
			if (x[a].fs < y[b].fs) {
				if (i < x[a].sc) {
					i++;
				} else if (i > x[a].sc) {
					i--;
				} else {
					a++;
				}
				if (j < y[b].sc) {
					j++;
				} else if (j > y[b].sc) {
					j--;
				}
			} else {
				if (j < y[b].sc) {
					j++;
				} else if (j > y[b].sc) {
					j--;
				} else {
					b++;
				}
				if (i < x[a].sc) {
					i++;
				} else if (i > x[a].sc) {
					i--;
				}
			}
		}
		cout << "Case #" << q + 1 << ": " << ans - 1 << endl;
	}
}
