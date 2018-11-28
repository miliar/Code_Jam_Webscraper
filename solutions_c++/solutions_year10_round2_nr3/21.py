
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<cstring>
#include<stack>
#include<sstream>
#include<complex>
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define DEBU true
#define debug(x) { if (DEBU) cerr << #x << " = " << x << "\n"; }
#define debugv(x) { if (DEBU) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; } }
#define fup(i,a,b) for(int i=(a);i<=(b);i++)
#define fdo(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset((x),0,sizeof (x))
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) ((int)a.size())
#define inf 1000000000
#define SQR(a) ((a)*(a))

using namespace std;
typedef long long lli;
typedef double ld;

const lli mod = 100003;
#define maxn 505
lli dp[maxn][maxn];

lli binom[maxn][maxn];

void doit(int n) {
	fup(pop, 2, n - 1) {
		fup(nile, 1, pop - 1) {
			int sr = (n - pop - 1);
			fup(srile, 0, sr) {
				if (srile + nile + 1 == pop); else continue;
				dp[n][nile + srile + 1] += dp[pop][nile] * binom[sr][srile];
				dp[n][nile + srile + 1] %= mod;
			}
		}
	}
	dp[n][1] += 1;
	dp[n][1] %= mod;
}

void goBinom() {
	binom[0][0] = 1;
	fup(i, 1, maxn - 1) {
		binom[i][0] = 1;
		fup(j, 1, i) {
			binom[i][j] = (binom[i - 1][j] + binom[i - 1][j - 1]) % mod;
		}
	}
}
lli getWyn(int n) {
	lli sum = 0;
	fup(i, 1, n) {
//		cout << "IL " << n << " " << i << " " << dp[n][i] << endl;
		sum += dp[n][i];
	}
	sum %= mod;
	return sum;
}
int main() {
	goBinom();
	int n;
	n = 500;
	fup(i, 2, n) {
		doit(i);		
	}
	int cas;
	cin >> cas;
	int c = 0;
	while (cas--) {
		++c;
		int n;
		cin >> n;
		lli w = getWyn(n);
		w %= mod;
		printf("Case #%d: %lld\n", c, w);
		
	}
	return 0;
}


