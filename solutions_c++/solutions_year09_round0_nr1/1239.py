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


string words[6000];
bool q[600][20][30];
int ans[600];
int L, D, N;
void init()
{
	freopen("input2.txt","r",stdin);
	freopen("output.txt","w",stdout);
	RE("%d %d %d",&L, &D, &N);
	int i, j;
	string s;
	FOR(i,0,D-1) cin >> words[i];
	FOR(i,0,N-1){
		cin >> s;
		int p = -1, be = -2, en = -1;
		FA(j, s){
			if (s[j]=='('){
				p++;
				be = j;
			} else if (s[j]==')'){
				en = j;
			} else {
				if (en>be) p++;
				q[i][p][s[j]-'a'] = true;
			}
		}
	}
}
void sol(){
	int i, j, k;
	FOR(i,0,D-1) FOR(j,0,N-1) {
		bool ok  = true;
		FOR(k,0,L-1) if (!q[j][k][words[i][k]-'a']) ok = false;
		if (ok) ans[j]++;
	}
	FOR(i,0,N-1){
		WR("Case #%d: %d", i+1, ans[i]);
		if (i<N-1) WR("\n");
	}
}
int main()
{
	init();
	sol();
	return 0;
}