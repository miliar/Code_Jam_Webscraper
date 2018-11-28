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
typedef vector<int> VI;
typedef vector<string>VS;

int T;

#define PAR pair< LL, LL >

LL g[3][3];

void init()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	RE("%d",&T);
}
int main()
{
	init();
	int i, j, k, t;
	LL n, A, B, C ,D, x0, y0, M;
	FOR(t,1,T)
	{
		RE("%I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d",&n, &A, &B, &C ,&D, &x0, &y0, &M);
		vector < PAR > r;
		LL X = x0, Y = y0;
		r.PB(make_pair(X, Y));
		FOR(i,1,n-1)
		{
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			r.PB(make_pair(X, Y));
			if (X<0 || Y<0) WR("aLERT!!!\n");
		}
		
		//FA(i,r) WR("%I64d %I64d\n",r[i].FI,r[i].SE);
		
		LL ans = 0;
		CLR(g);
		FA(i,r) g[r[i].FI %3][r[i].SE%3]++;
		
		vector < pair<int, int> > hh;
		FOR(i,0,2) FOR(j,0,2) hh.PB(make_pair(i,j));
		//3
		FOR(i,0,6) FOR(j,i+1,7) FOR(k,j+1,8) 
		if ((hh[i].FI + hh[j].FI + hh[k].FI)  % 3==0)
		if ((hh[i].SE + hh[j].SE + hh[k].SE)  % 3==0) 
		ans+=g[hh[i].FI][hh[i].SE]*g[hh[j].FI][hh[j].SE]*g[hh[k].FI][hh[k].SE];
		
		//2
		FOR(i,0,8) FOR(j,0,8) if (i!=j) 
		if ((hh[i].FI + hh[j].FI + hh[j].FI)  % 3==0)
		if ((hh[i].SE + hh[j].SE + hh[j].SE)  % 3==0)
		ans+=g[hh[i].FI][hh[i].SE]* g[hh[j].FI][hh[j].SE]*(g[hh[j].FI][hh[j].SE]-1)/2;
		
		//1
		FOR(i,0,8)
		if ((hh[i].FI + hh[i].FI + hh[i].FI)  % 3==0)
		if ((hh[i].SE + hh[i].SE + hh[i].SE)  % 3==0)
		ans+=g[hh[i].FI][hh[i].SE]*(g[hh[i].FI][hh[i].SE]-1)*(g[hh[i].FI][hh[i].SE]-2)/6;
		
		WR("Case #%d: %I64d",t,ans);
		if (t<T) WR("\n");
	}
	return 0;
}