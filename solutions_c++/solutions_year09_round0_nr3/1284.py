#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <bitset>
#include <sstream>
#include <cmath>
#include <ctime>

#define WR printf
#define RE scanf
#define FOR(i,Be,En) for(i=(Be);i<=(En);++i)
#define DFOR(i,Be,En) for(i=(Be);i>=(En);--i)
#define PB push_back
#define SZ(a) (int)((a).size())
#define FIT(i,v) for(i=(v).begin();i!=(v).end();i++)
#define RFIT(i,v) for(i=(v).rbegin();i!=(v).rend();i++)
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define SE second
#define FI first
#define CLR(a) memset(a,0,sizeof(a))
#define LL long long
using namespace std;
typedef vector<int>    VI;
typedef vector<string> VS;
typedef pair<int ,int> PAR;


string G("welcome to code jam");
int T;
int dp[50][2000];
void init()
{
	freopen("input2.txt","r",stdin);
	freopen("output.txt","w",stdout);
	RE("%d\n",&T);
}
void sol(){
	int t, i, j;
	string s;
	FOR(t,1,T){
		getline(cin, s);
		int N = SZ(s);
		CLR(dp);
		FOR(i,0,N-1){
			if (s[i]==G[0]) dp[0][i] = 1;
		}
		FA(i, G) if (i){
			dp[i][0] = 0;
			int sum = 0;
			FOR(j,1,N-1){
				sum = (sum + dp[i-1][j-1]) % 10000;
				if (s[j]==G[i]) dp[i][j] = sum;
			}
		}
		int ans = 0;
		FOR(i,0,N-1) ans = (ans + dp[SZ(G)-1][i]) % 10000;
		
		WR("Case #%d: ", t);
		string h;
		FOR(i,0,3) h = string(1, ans%10 + '0') + h, ans/=10;
		cout << h;
		if (t<T) WR("\n");
	}
}
int main()
{
	init();
	sol();
	return 0;
}