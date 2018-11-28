
#include <iostream>
#include <vector>
#include <map>
using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)
typedef long long i64;

i64 dp[2000][20];
char gr[200][200];
int M,N;

i64 doit(int msk, int m) {
	if(m==M) return 0;
	i64& ret = dp[msk][m];
	if(ret+1) return ret;
	ret=0;
	fu(i,0,(1<<N)) {
		bool good=true;
		if(msk&(i<<1)) good=false;
		if((msk<<1)&i) good=false;
		if(i&(i<<1)) good=false;
		int cnt=0;
		fu(j,0,N) if(i&(1<<j)) {
			if(gr[m][j]=='x') good=false;
			cnt++;
		}
		if(good) ret>?=doit(i, m+1)+cnt;
	}
	return ret;
}

int main(void) {
	int C;
	cin >> C;
	fu(ts,1,C+1) {
		memset(dp,-1,sizeof(dp));
		cout << "Case #" << ts << ": ";
		cin >> M >> N;
		fu(m,0,M) fu(n,0,N) cin >> gr[M-1-m][n];
		if(0) fu(m,0,M) {
			fu(n,0,N) cout << gr[m][n];
			cout << endl;
		}
		cout << doit(0,0) << endl;
	}
}
