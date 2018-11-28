#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
using namespace std; 

#define REP(i,n) for(int i=0;i<(n);++i) 
#define FOR(i,a,b) for(int i=(a);i<=(b);++i) 
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i) 
#define FOREACH(it,c) for(typeof((c).begin())it=(c).begin();it!=(c).end();++it) 
#define CLR(x) memset((x),0,sizeof((x))) 
typedef long long LL; 
typedef vector<int> VI; 
typedef vector<string> VS; 

#define INF 2000000000

int M, V;
int n, m;
int gate[10005];
int chan[10005];
int leaf[10005];
int mm[10005][2];

int dp(int idx, int v) {
	int& ret = mm[idx][v];
	if (ret != -1) return ret;

	if (idx == 1 && v == 1) {
		int c = 1;
	}
	if (idx >= n) {
		if (leaf[idx] == v) ret = 0;
		else ret = -2;
		return ret;
	}

	ret = INF;

	int ll = idx * 2 + 1, rr = idx * 2 + 2;

	int t1 = dp(ll, 0);
	int t2 = dp(rr, 0);
	int t3 = dp(ll, 1);
	int t4 = dp(rr, 1);

	int add;
	if (v == 0) {
		if (gate[idx] == 1) add = 0;
		else add = 1;

		if ((add == 1 && chan[idx] == 1) || add == 0) {
			if (t1 != -2 && t2 != -2) ret = min(ret, t1 + t2 + add);
			if (t1 != -2 && t4 != -2) ret = min(ret, t1 + t4 + add);
			if (t3 != -2 && t2 != -2) ret = min(ret, t3 + t2 + add);
		}
		
		if (gate[idx] == 1) add = 1;
		else add = 0;

		if ((add == 1 && chan[idx] == 1) || add == 0) {
			if (t1 != -2 && t2 != -2) ret = min(ret, t1 + t2 + add);
		}
	} else {
		if (gate[idx] == 1) add = 0;
		else add = 1;

		if ((add == 1 && chan[idx] == 1) || add == 0) {
			if (t3 != -2 && t4 != -2) ret = min(ret, t3 + t4 + add);
		}

		if (gate[idx] == 1) add = 1;
		else add = 0;

		if ((add == 1 && chan[idx] == 1) || add == 0) {
			if (t3 != -2 && t4 != -2) ret = min(ret, t3 + t4 + add);
			if (t3 != -2 && t2 != -2) ret = min(ret, t3 + t2 + add);
			if (t1 != -2 && t4 != -2) ret = min(ret, t1 + t4 + add);
		}
	}

	if (ret == INF) ret = -2;

	return ret;
}

void run() {
	cin >> M >> V;
	n = (M - 1) / 2;
	m = M - n;
	REP(i,n) {
		cin >> gate[i] >> chan[i];
	}
	FOR(i,n,M-1) {
		cin >> leaf[i];
	}
	memset(mm, -1, sizeof(mm));
	int res = dp(0, V);
	if (res == -2) cout << "IMPOSSIBLE" << endl;
	else cout << res << endl;
}

int main() {
	int kase;
	cin >> kase;
	REP(k,kase) {
		cout << "Case #" << k + 1 << ": ";
		run();
	}
	return 0;
}
