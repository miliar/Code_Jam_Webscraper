#pragma warning (disable:4786) 
#pragma warning (disable:4996) 
#include <time.h>
#include <algorithm> 
#include <iostream>  
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <stack>
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <cassert>
using namespace std;

#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) REP(i,SZ(v))
typedef long long ll; 
const double EPS = 1e-7;

void openfiles() {
	#ifndef ONLINE_JUDGE
		freopen("test.in","rt",stdin);
		freopen("test.out","wt",stdout);   
	#endif
}

const int INF = 0x7ffffff0;
int ntest = 0;
void solve() {
	int m, r;
	scanf("%d %d",&m,&r);
	vector<int> v(m+1);
	vector<int> c(m+1);
	vector<vector<int> > num(m+1, vector<int>(2, INF));
	FORE(i,1,m) {
		if (i <= (m - 1) / 2) {
			int a, b;
			scanf("%d %d",&a,&b);
			v[i] = a;
			c[i] = b;
		}
		else {
			int a; scanf("%d",&a);
			v[i] = a;
			c[i] = 0;
			if (v[i] == 0) {
				num[i][0] = 0;
			}
			if (v[i] == 1) {
				num[i][1] = 0;
			}
		}
	}

	for (int i = (m - 1) / 2; i > 0; i--) {
		int l = i * 2;
		int r = i * 2 + 1;
		
		REP(k,2) REP(lu,4) {
			// k - operation
			// l - last result
			if (c[i] == 0 && k != v[i]) continue;
			int left = lu % 2;
			int right = lu / 2;
			int res = (k == 1 ? left & right : left | right);
			if (num[l][left] != INF && num[r][right] != INF) {
				num[i][res] = min(num[i][res], num[l][left] + num[r][right] + (k == v[i] ? 0 : 1) );
			}
		}
		//cout << i << endl;
		//cout << num[i][0] << " " << num[i][1] << endl;
	}
	if (num[1][r] >= INF) {
		printf("Case #%d: IMPOSSIBLE\n",++ntest);
		return;
	}
	printf("Case #%d: %d\n",++ntest,num[1][r]);
}

int main() {
	openfiles();
	int n; scanf("%d", &n);
	REP(i,n) solve();

	return 0;
}