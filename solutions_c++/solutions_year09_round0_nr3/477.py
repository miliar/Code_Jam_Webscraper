/* Rajat Goel [C++] */
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<sstream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;
const int    INF =     0x7FFFFFFF;
const double EPS =     1e-7;
typedef pair<int,int>  pii;
typedef long long      int64;
#define loop(i,n)      for(int i=0;i<n;i++)
#define foreach(i,a)   for(typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define present(x,in)  (find((in).begin(),(in).end(),x) != (in).end())
#define all(a)         (a).begin(),(a).end()
#define cast(a,b)      { ostringstream myOut; myOut << a ; istringstream myIn ( myOut.str() ); myIn >> b; }
inline int fCMP(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

int dp[501][501];

int main() {
	int T;
	string cS = "welcome to code jam";
	scanf(" %d",&T);
	loop(cas, T) {
		int ans = 0;
		char st[1000];
		scanf(" %[^\n]", st);
		string s = st;
		memset(dp, 0, sizeof(dp));
		loop(i, 501) dp[0][i] = 1;
		for(int i=1;i<=cS.size();i++) {
			for(int j=1;j<=s.size();j++) {
				dp[i][j] = dp[i][j-1];
				if (s[j-1]==cS[i-1]) {
					dp[i][j]+=dp[i-1][j-1];
				}
				dp[i][j]%=10000;
			}
		}
/*		loop(i, cS.size()+1) {
			loop(j, s.size()+1) {
				cout << dp[i][j] << " ";
			}
			cout << endl;
		}
*/
		printf("Case #%d: %04d\n", cas+1, dp[cS.size()][s.size()]);
	}
	return 0;
}
