#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
#include <cstring>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) ((int)(x).size())

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

int N, M;
int u[20000], v[20000];
vector<vi> l;

int ass[20000];
int max_catnip;

bool possible(int i) {
	if (i == N) {
		bool result = true;
		for (int catnip = 1; catnip <= max_catnip; catnip++) {
			REP(j, SZ(l)) {
				bool valid = false;
				REP(k, SZ(l[j])) if (ass[l[j][k]-1] == catnip) valid = true;
				if (!valid) return false;
			}
		}
		return true;
	} else {
		for (ass[i] = 1; ass[i] <= max_catnip; ass[i]++) if (possible(i+1)) return true;
	}
	return false;
}

int main() {
	int casos, res;
	cin >> casos;
	REP(caso, casos) {
		cin >> N >> M;
		vi first;
		for (int i = 1; i <= N; i++) first.pb(i);
		l.clear();
		l.pb(first);
		REP(i, M) cin >> u[i];
		REP(i, M) cin >> v[i];
		REP(i, M) {
			vi result;
			REP(j, SZ(l)) if (find(all(l[j]), u[i]) != l[j].end() && find(all(l[j]), v[i]) != l[j].end()) {
				result = l[j];
				swap(l[j], l[SZ(l)-1]);
				l.pop_back();
				break;
			}
			//if (find(all(result), u) - result > find(all(result),v) - result) reverse(all(result));
			vi piece1, piece2;
			bool state = true;
			REP(j, SZ(result)) {
				if (result[j] == u[i] || result[j] == v[i]) {
					state = !state;
					piece1.pb(result[j]);
					piece2.pb(result[j]);
				} else {
					if (state) {
						piece1.pb(result[j]);
					} else {
						piece2.pb(result[j]);
					}
				}
			}
			l.pb(piece1); l.pb(piece2);
		}
		/*REP(i, SZ(l)) {
			REP(j, SZ(l[i])) cout << l[i][j] << " ";
			cout << endl;
		}*/
		if (SZ(l) == 1) {
			cout << "Case #" << caso+1 << ": " << N << endl;
			REP(i, N) {
				cout << i+1;
				if (i == N-1) cout << endl; else cout << " ";
			}
			continue;
		}
		max_catnip = 999;
		REP(i, SZ(l)) if (SZ(l[i]) < max_catnip) max_catnip = SZ(l[i]);
		while (!possible(0)) max_catnip--;
		cout << "Case #" << caso+1 << ": " << max_catnip << endl;
		REP(i, N) {
			cout << ass[i];
			if (i == N-1) cout << endl; else cout << " ";
		}
	}
	return 0;
}
