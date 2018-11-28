#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cmath>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define FORD(i,a,b) for(int i=(a),_b(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define SZ(a) ((int) a.size())
#define pb push_back

#define VAR(a,b) __typeof(b) a=(b)
#define FORE(it,a) for(VAR(it,(a).begin());it!=(a).end();it++)
#define X first
#define Y second
#define DEBUG(x) cout << #x << " = " << x << endl;

#define INF 1000000000

typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef pair <int, VI> PIVI;
typedef long long ll;

int parse (string s) {
	return ((s[0] - '0') * 10 + (s[1] - '0')) * 60 + ((s[3] - '0') * 10 + (s[4] - '0'));
}

VI leave[2][3600];
int av[2][3600];
int cur[2];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int test, t;
	int n, m;
	string s1, s2;
	cin >> test;	
	FOR (ntest, 1, test + 1) {
		int span;
		cin >> span;
		cin >> n >> m;

		REP (q, 2)	
			REP (w, 3600)
				leave[q][w].clear();
				
		REP (i, n) {
			cin >> s1 >> s2;
			leave[0][parse (s1)].pb (parse (s2));				
		}
		REP (i, m) {
			cin >> s1 >> s2;
			leave[1][parse (s1)].pb (parse (s2));				
		}
		
		VI res (2);
		memset (av, 0, sizeof (av));
		memset (cur, 0, sizeof (cur));
		REP (t, 3600) {
			cur[0] += av[0][t];
			cur[1] += av[1][t];
			REP (k, 2)
				REP (i, SZ (leave[k][t])) {
					if (!cur[k]) {
						cur[k]++;
						res[k]++;
					}	
					cur[k]--;				
					if (leave[k][t][i] + span < 3600)
						av[1-k][leave[k][t][i] + span]++;
				}
		}
		printf ("Case #%d: %d %d\n", ntest, res[0], res[1]);
	}
	return 0;
}
