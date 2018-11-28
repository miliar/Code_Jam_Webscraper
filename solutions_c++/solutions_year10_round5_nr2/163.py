#include <iostream>
#include <string>
#include <vector>
using namespace std;
typedef long long i64;

#define fu(i,m,n) for(int i=m; i<n; i++)

int INF=1000000000;

int dp[100000];

int main(void) {
	int T;
	cin >> T;
	fu(tc,1,T+1) {
		i64 L;
		int N;
		cin >> L >> N;
		vector<int> boards(N);
		fu(i,0,N) cin >> boards[i];
		sort(boards.begin(),boards.end());
		reverse(boards.begin(),boards.end());
		int g = 0;
		fu(i,0,N) g=__gcd(g,boards[i]);
		if(g>1 && L%g) {
			cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
		}
		else {
		if(g>1) {
			L/=g;
			fu(i,0,N) boards[i]/=g;
		}
		memset(dp,100,sizeof(dp));
		INF=dp[0];
		dp[0]=0;
		int cons = 0;
		int l;
		for(l=0; l<80000; l++) {
			fu(b,0,N) {
				dp[l+boards[b]] = min(dp[l+boards[b]], dp[l]+1);
			}
			//if(dp[l]==INF) cons=0;
			//else cons++;
			//if(cons>=boards[0]) break;
		}
		l--;
		i64 ret = 0;
		if(L>l) {
			ret += (L-l)/boards[0];
			L -= ret*boards[0];
		}
		while(L>l) { ret++; L-=boards[0]; }
		cout << "Case #" << tc << ": " << ret+dp[L] << endl;
		}
	}
}
