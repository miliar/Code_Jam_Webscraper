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

int n, k;

int m[6000];

void init()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	RE("%d",&T);
}
int main()
{
	init();
	int i, j, t, h;
	FOR(t,1,T)
	{
		RE("%d %d",&k, &n);
		CLR(m);
		int cur = 0;
		FOR(i,1,k)
		{
			int c = 0;
			//int hi = i%(k-i+1);
			//if (hi==0) hi=1;
			while (c!=i)
			{
				if (++cur>k) cur = 1;
				if (!m[cur]) c++;
			}
			m[cur] = i;
		}
		WR("Case #%d:",t);
		FOR(i,1,n)
		{
			RE("%d",&h);
			WR(" %d",m[h]);
		}
		if (t<T) WR("\n");
	}
	return 0;
}