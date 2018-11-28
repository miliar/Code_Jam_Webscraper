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

int card[3000];
vector<vi> s;

int main() {
	int casos;
	cin >> casos;
	REP(caso, casos) {
		int N;
		cin >> N;
		REP(i, N) cin >> card[i];
		sort(card, card+N);
		int res = N;
		s.clear();
		REP(cont, N) {
			int val = card[cont];
			vector<vi> ns;
			REP(i, SZ(s)) if (s[i].back() + 1 < val) {
				res = min(res, SZ(s[i]));
			} else {
				ns.pb(s[i]);
			}
			s.swap(ns);
			int bestindex = -1;
			REP(i, SZ(s)) {
				if (s[i].back() + 1 == val) {
					if (bestindex == -1 || SZ(s[i]) < SZ(s[bestindex])) bestindex = i;
				}
			}
			if (bestindex == -1) {
				vi v;
				v.pb(val);
				s.pb(v);
			} else {
				s[bestindex].pb(val);
			}
		}
		REP(i, SZ(s)) res = min(res, SZ(s[i]));
		cout << "Case #" << caso+1 << ": " << res << endl;
	}
	return 0;
}
