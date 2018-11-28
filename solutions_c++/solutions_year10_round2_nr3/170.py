#include <algorithm>
#include <cstring>
#include <set>
#include <cmath>
using namespace std;
#include <iostream>
#include <string>
#include <cstdio>
#include <bitset>
#include <map>

//By chyx111
typedef long long ll;
#define two(x) (1<<(x))
#define DBG(a) cerr << #a << ": " << (a) << endl
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)

const int MAXN = 512;
ll dp[MAXN][MAXN];
ll C[MAXN][MAXN];
int ans[MAXN];
const int P = 100003;

int main() {
	// c
	Rep(i,MAXN) C[0][i] = 0;
	Rep(i,MAXN) C[i][0] = 1;
	for(int i = 1; i < MAXN; ++i){
		for(int j = 1; j < MAXN; ++j){
			C[i][j] = C[i-1][j] + C[i-1][j-1];
			C[i][j] %= P;
		}
	}
//	DBG(C[10][5]);


	memset(dp,0,(sizeof dp));
	
	Rep(i,MAXN)dp[1][i] = 1;

	for(int i = 3; i < 512; ++i){
		dp[1][i] = 1;
		for(int j = i-1; j >= 2; --j){
			for(int k = j-1; k >= 1; --k){
				dp[j][i] += dp[k][j] * C[i-j-1][j-k-1];
				dp[j][i] %= P;
			}
		}
		ans[i] = 0;
		Rep(j,i) ans[i] += dp[j][i], ans[i] %= P;
//		printf("%d %d\n", i, ans[i]);
	}

	int ca; cin>>ca;
	Rep(ica,ca){
		int n; cin>>n;
		printf("Case #%d: %d\n", ica+1, ans[n] % 100003 );
	}
	return 0;
}

