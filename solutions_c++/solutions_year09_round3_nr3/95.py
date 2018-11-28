#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

const int INF = 1<<30;

int P,Q;
int dp[102][102];
int v[102];

int get(int l, int r) {
	if (l+1==r) return 0;
	if (dp[l][r]==-1) {
		dp[l][r]=INF;
		for (int i=l+1;i<r;++i) {
			dp[l][r]=min(dp[l][r],v[r]-v[l]-2+get(l,i)+get(i,r));
		}
	}
	return dp[l][r];
}

int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;++t) {
		cin >> P >> Q;
		v[0]=0;
		for (int i=0;i<Q;++i) cin >> v[i+1];
		v[Q+1]=P+1;
		memset(dp,-1,sizeof(dp));
		cout << "Case #" << t << ": " << get(0,Q+1) << endl;
	}
}
