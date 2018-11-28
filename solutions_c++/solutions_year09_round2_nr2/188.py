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


int T;
void init()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	RE("%d\n",&T);
}
void sol(){
	int t, i;
	string s;
	FOR(t,1,T){
		cin >> s;
		s = string("0") + s;
		next_permutation(s.begin(),s.end());
		if (s[0]=='0') s.erase(0,1);
		if (t>1) WR("\n");
		WR("Case #%d: %s",t,s.c_str());
	}
}
int main()
{
	init();
	sol();
	return 0;
}