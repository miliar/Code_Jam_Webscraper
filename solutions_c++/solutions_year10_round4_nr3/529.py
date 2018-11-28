#include <cstdio>
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

bool X[1000][1000], Y[1000][1000];

void testcase(int zest) {
	int R;
	scanf("%d",&R);
	REP(i,R) {
		int x1,x2,y1,y2;
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		FOR(a,x1,x2) FOR(b,y1,y2) X[450+a][450+b] = true;
	}
	
	int res = 0;
	while (true) {
		bool ok = true;
		REP(i,1000) REP(j,1000) if(X[i][j]) { ok = false; goto here; }

		printf("Case #%d: %d\n",zest,res);
		return;

here:
		;
		REP(i,1000) REP(j,1000) {
			Y[i][j] = X[i][j];
			if (X[i][j]) {
				Y[i][j] = i > 0 && X[i-1][j] || j > 0 && X[i][j-1];
			} else {
				Y[i][j] = i > 0 && X[i-1][j] && j > 0 && X[i][j-1];
			}
		}
		REP(i,1000) REP(j,1000) X[i][j] = Y[i][j];
		
		++res;
	}
}

int main() {
	int z;
	scanf("%d",&z);
	REP(i,z) testcase(i+1);
}
