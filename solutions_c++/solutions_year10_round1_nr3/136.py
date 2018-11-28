#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i = 0,_n = (n);i < _n;++i)
#define FOR(i,a,b) for(int i = (a),_n = (b);i <= _n;++i)
#define FORD(i,a,b) for(int i = (a),_n = (b);i >= _n;--i)
#define FORE(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define ALL(c) (c).begin(),(c).end()
#define SIZE(c) ((int)(c).size())
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

const int INF = 1000000000;

int lef[1000000], righ[1000000];

void testcase(int nr) {
	int a1,a2,b1,b2;
	cin >> a1 >> a2 >> b1 >> b2;
	LL res = 0;
	FOR(i,a1,a2) res += max(0, min(b2,righ[i])-max(b1,lef[i])+1);
	cout << "Case #" << nr << ": " << 1LL*(a2-a1+1)*(b2-b1+1) - res << endl;
}

int main() {
	lef[1] = 1, righ[1] = 1;
	lef[2] = 2, righ[2] = 3;
	int cur = 1;
	FOR(i,3,1000000) {
		while (righ[cur] < i) ++cur;
		lef[i] = cur;
		righ[i] = lef[i]+i-1;
	}

	int T;
	cin >> T;
	REP(i,T) testcase(i+1);
}
