#include <iostream>
#include <string>
#include <vector>
using namespace std;
#define fu(i,m,n) for(int i=m; i<(n); i++)
#define fd(i,m,n) for(int i=n-1; i>=m; i--)

vector<int> prices[20];
vector<int> Cs[20];
typedef long long i64;
const i64 INF=1000000000000LL;

i64 dp[20][2000][20];

i64 doit(int P, int w, int s) {
	i64& ret=dp[P][w][s];
	if(ret+1) return ret;
	if(s>Cs[P][w]) return INF;
	if(P==0) return 0;
	ret = min(doit(P-1, 2*w, s+1)+doit(P-1,2*w+1,s+1),
		 doit(P-1, 2*w, s+0)+doit(P-1,2*w+1,s+0)+prices[P][w]);
	//cout << P << " " << w << " " << s << " " << ret << endl;
	return ret;
}

int main(void) {
	int T;
	cin >> T;
	fu(tc,1,T+1) {
		memset(dp,-1,sizeof(dp));
		int P;
		cin >> P;
		vector<int> C(1<<P);
		fu(i,0,1<<P) cin >> C[i];
		int p;
		fu(i,0,P) {
			prices[i+1].clear();
			fu(j,0,1<<(P-1-i)) {
				cin >> p;
				prices[i+1].push_back(p);
			}
		}
		Cs[0]=C;
		fu(p,1,P+1) {
			Cs[p] = vector<int>(1<<(P-p));
			fu(i,0,1<<P-p)
				Cs[p][i]=min(Cs[p-1][2*i],Cs[p-1][2*i+1]);
		}
		cout << "Case #" << tc << ": " << doit(P, 0, 0) << endl;
	}
}
