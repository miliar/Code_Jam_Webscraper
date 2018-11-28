#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>


 
using namespace std;
 
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
 
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

int P;
int M[2<<11];
int cost[11][2<<11];
ll dp[11][11][2<<11];//verpasste Spiele, Runde
ll loo;
ll getVal(int R, int missed, int pos){
	if(dp[R][missed][pos]!=-1)return dp[R][missed][pos];
//	if(R==0)cout << "EROOR\n";
	ll ret = min(loo,min(getVal(R-1,missed,pos<<1)+getVal(R-1,missed,(pos<<1)+1)+cost[R-1][pos],
		getVal(R-1,missed+1,pos<<1)+getVal(R-1,missed+1,(pos<<1)+1)));
	dp[R][missed][pos]=ret;
	
//	cout << R << " " << missed << " " << pos << ": " << cost[R-1][pos];
//	cout << " result: " << ret << endl;
	return ret;
}
int main(){
	int tc;
	loo = oo;
	loo *= oo;
	cin >> tc;
	FOR(tcc,1,tc+1){
		cin >> P;
		FOR(i,0,1<<P)cin >> M[i];
		FOR(i,0,P){
			FOR(j,0,1<<(P-i-1)){
				cin >> cost[i][j];
			}
		}
		memset(dp,-1,sizeof(dp));
		FOR(i,0,1<<P){
			FOR(k,0,P+1){
				dp[0][k][i]=((M[i]>=k)?0:loo);
			}
		}
		int erg = getVal(P,0,0);
		printf("Case #%d: %lld\n",tcc,erg);
	}
	return 0;
}
