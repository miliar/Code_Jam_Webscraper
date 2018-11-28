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
typedef pair<int, int> P;
typedef vector<int> vi;

string wel="!welcome to code jam",in;
int T,dp[507][20];

int main(){
	cin >> T; getline(cin,in);
	FOR(cas,1,T){
		CLR(dp);
		getline(cin,in);
		in="!"+in;
		int n=in.size();
//		cout << in << endl;
		dp[0][0]=1;
		FOR(i,1,n-1){
			dp[i][0]=1;
			FOR(j,1,19) dp[i][j]=(dp[i-1][j]+(in[i] == wel[j]? dp[i-1][j-1] : 0))%10000;
//			cout << "i " << in[i] << " " << dp[i][17] << " " << dp[i][18] << " " << wel[18] << endl;
		}
		cout << "Case #" << cas << ": ";
		int res=dp[n-1][19];
		if(res<10) cout << "0";
		if(res<100) cout << "0";
		if(res<1000) cout << "0";
		cout << res << endl;
	}
	return 0;
}
