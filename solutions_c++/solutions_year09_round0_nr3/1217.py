// Headers {{{
#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,j,k) for(int i=(j); i<=(k); ++i)
#define FORD(i,j,k) for(int i=(j); i>=(k); --i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ST first
#define ND second
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define SQR(a) ((a)*(a))
#define debug(x) cerr << #x << " = " << x << '\n'
template<typename Q> inline int size(Q a) { return a.size(); }
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<pair<int,int> > VPII;
typedef unsigned long long ULL;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
const int INF=1000000000;
// }}}

char bla[20]="welcome to code jam";

char text[505];

int dp[505][19];

int main() {
	int ntc;
	scanf("%d\n",&ntc);
	FOR(tc,1,ntc) {
		printf("Case #%d: ",tc);
		gets(text);
		memset(dp,0,sizeof(dp));
		int n=strlen(text);
		REP(i,n) if(text[i]==bla[0]) dp[i][0]=1;
		FOR(i,1,18) {
			REP(j,n) if(text[j]==bla[i]) {REP(k,j) dp[j][i] += dp[k][i-1];
			dp[j][i]%=10000;}
		}
		int res=0;
		REP(i,n) res+=dp[i][18];
		res%=10000;
		if(res<1000) printf("0");
		if(res<100) printf("0");
		if(res<10) printf("0");
		printf("%d\n",res);
	}
	return 0;
}
