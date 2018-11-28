#include <iostream>
#include <string>
#include <vector>

using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)

const int INF=1000000000;

vector<int> dat;
int D,I,M,N;

int dp[200][300];

int doit(int i, int c) {
	if(i==N) return 0;
	int& ret=dp[i][c];
	if(ret+1) return ret;

	ret = INF;

	ret = min(ret, abs(c-dat[i]) + doit(i+1,c));
	fu(d,0,256) if(abs(c-d)<=M) ret = min(ret, abs(d-dat[i]) + doit(i+1, d));
	if(M) fu(d,0,256) {
		int hm = max(0, (abs(d-c)-1)/M);
		//int c2 = c + (d>c?1:-1) * hm * M;
		ret = min(ret, I*hm + abs(dat[i]-d) + doit(i+1,d));
	}
	ret = min(ret, D + doit(i+1,c));
	return ret;
}

int main(void) {
	int T;
	cin >> T;
	fu(tc,1,T+1) {
		cin >> D >> I >> M >> N;
		memset(dp,-1,sizeof(dp));
		dat = vector<int>(N);
		fu(i,0,N) cin >> dat[i];
		int best = INF;
		fu(c,0,256) best = min(best, doit(0,c));
		cout << "Case #" << tc << ": " << best << endl;
	}
}
