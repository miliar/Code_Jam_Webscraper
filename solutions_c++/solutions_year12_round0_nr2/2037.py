#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define all(a) (a).begin(),(a).end()
#define UN(a) sort(all(a)),(a).resize(unique(all(a))-(a).begin())
#define sz(a) ((int) (a).size())
#define pb push_back
#define CL(a,b) memset ((a), (b), sizeof (a))
#define X first
#define Y second

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;

int surp(int x) {
		return (x + 4) / 3;
}

int notsurp(int x) {
		return (x + 2) / 3;
}

int main () {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
		int t;
		cin >> t;
		REP (i, t) {
				int n, s, p;
				cin >> n >> s >> p;
				vi a(n);
				REP (i, n) {
						cin >> a[i];
				}
				sort(all(a));
				reverse(all(a));
				int res = 0;
				REP (i, sz (a)) {
						int q = surp(a[i]);
						int w = notsurp(a[i]);
						if (w >= p) ++res; else {
								if (q >= p && s && a[i] >= 2) {
										--s;
										++res;
								}
						}
				}
				cout << "Case #" << (i+1) << ": ";
				cout << res << endl;
		}
    return 0;
}
