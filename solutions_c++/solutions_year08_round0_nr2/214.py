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

#define MAXT 100000
using namespace std;
typedef vector<int> VI;
typedef vector<string>VS;

int T;


pair<int ,int> ta[1000], tb[1000];

int da[MAXT + 5], db[MAXT+5];
void init()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	RE("%d",&T);
}
pair<int, int> f(string s)
{
	stringstream ss(s);
	string a, b;
	ss >> a >> b;
	pair<int,int> res;
	res.FI = ((a[0] - '0') * 10 + (a[1] - '0'))*60 + ((a[3]- '0') * 10 + (a[4]-'0'));
	res.SE = ((b[0] - '0') * 10 + (b[1] - '0'))*60 + ((b[3]- '0') * 10 + (b[4]-'0'));
	return res;
}
int main()
{
	init();
	int t, i, j;
	int d, na, nb;
	FOR(t,1,T)
	{
		RE("%d%d%d",&d,&na,&nb);
		
		char ch = getchar();
		string h;
		FOR(i,1,na)
		{
			getline(cin,h);
			ta[i] = f(h);
		}
		FOR(i,1,nb)
		{
			getline(cin,h);
			tb[i] = f(h);
		}
		CLR(da);
		CLR(db);
		FOR(i,1,na)
		{
			da[ta[i].FI] --;
			db[ta[i].SE + d] ++;
		}
		FOR(i,1,nb)
		{
			db[tb[i].FI] --;
			da[tb[i].SE + d] ++;
		}
		int ra = 0, rb = 0;
		int ca = 0, cb = 0;
		FOR(i,0,MAXT)
		{
			ca+=da[i];
			if (ca<ra) ra = ca;
			cb+=db[i];
			if (cb<rb) rb = cb;
		}
		WR("Case #%d: %d %d",t,-ra,-rb);
		if (t<T) WR("\n");
	}
	return 0;
}