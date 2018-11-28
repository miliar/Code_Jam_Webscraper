#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <cstring>
using namespace std;
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (int i=(a); i>=(b); --i)
#define FORE(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n";
#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset(x,0,sizeof x)
#define xx first
#define yy second
typedef long long int lli;
typedef vector<int> vi;

#define MAXN 5007
#define INF ((lli)1E9)

lli T,P,N,M[MAXN],koszt[MAXN],dp[MAXN][17];

int main(){
	cin >> T;
	FOR(cas,1,T){
        //in
        cin >> P;
        N = (1 << P);
        REP(i,N) cin >> M[i];
        FORD(p,P-1,0)
            REP(i,1<<p)
               cin >> koszt[(1<<p)+i];
        //rozw
        REP(i,2*N) REP(j,17) dp[i][j] = INF;
        REP(i,N) FOR(j,0,M[i])
            dp[N+i][j] = 0;
        FORD(i,N-1,1) REP(j,P+1)
            dp[i][j] = min(dp[i*2][j+1] + dp[i*2+1][j+1], dp[i*2][j]+dp[i*2+1][j]+koszt[i]);
        //out
		cout << "Case #" << cas << ": " << dp[1][0] << endl;
	}
	return 0;
}
