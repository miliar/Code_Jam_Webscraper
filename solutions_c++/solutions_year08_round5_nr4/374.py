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
#define MOD 10007

int mat[105][105];
LL mm[105][105];
int height, width, rocks;

LL dp(int r, int c) {
	LL& res = mm[r][c];
	if (res != -1) return res;

	if (r == height && c == width) return res = 1;

	res = 0;

	int tr = r + 2, tc = c + 1;

	if (tr <= height && tc <= width && mat[tr][tc] == 0) {
		LL t = dp(tr, tc) % MOD;
		res = (res + t) % MOD;
	}

	tr = r + 1, tc = c + 2;
	if (tr <= height && tc <= width && mat[tr][tc] == 0) {
		LL t = dp(tr, tc) % MOD;
		res = (res + t) % MOD;
	}

	res %= MOD;

	return res;
}

void run() {
	cin >> height >> width >> rocks;
	memset(mat, 0, sizeof(mat));
	REP(i,rocks) {
		int h, w;
		cin >> h >> w;
		mat[h][w] = 1;
	}
	memset(mm, -1, sizeof(mm));
	LL res = dp(1, 1) % MOD;
	cout << res << endl;
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
