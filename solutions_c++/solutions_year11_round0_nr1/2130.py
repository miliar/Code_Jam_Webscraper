//darkstallion's template

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
using namespace std;

int t,n,x,bz,oz,bpos,opos,ans;
char s;

int main()
{
	scanf("%d",&t);
	FORN(i,t)
	{
		scanf("%d",&n);
		vector<PII> b,o;
		FORN(j,n)
		{
			cin >> s >> x;
			if (s == 'B')
				b.pb(mp(x,j));
			else
				o.pb(mp(x,j));
		}
		bz = 0;
		oz = 0;
		bpos = 1;
		opos = 1;
		ans = 0;
		while ((bz < b.sz()) && (oz < o.sz()))
		{
			if (b[bz].se < o[oz].se)
			{
				if (abs(b[bz].fi-bpos) < abs(o[oz].fi-opos))
					opos = o[oz].fi-(abs(o[oz].fi-opos)-(abs(b[bz].fi-bpos)+1));
				else
					opos = o[oz].fi;
				ans += abs(b[bz].fi-bpos)+1;
				bpos = b[bz].fi;
				bz++;
			}
			else
			{
				if (abs(b[bz].fi-bpos) > abs(o[oz].fi-opos))
					bpos = b[bz].fi-(abs(b[bz].fi-bpos)-(abs(o[oz].fi-opos)+1));
				else
					bpos = b[bz].fi;
				ans += abs(o[oz].fi-opos)+1;
				opos = o[oz].fi;
				oz++;
			}
		}
		while (bz < b.sz())
		{
			ans += abs(b[bz].fi-bpos)+1;
			bpos = b[bz].fi;
			bz++;
		}
		while (oz < o.sz())
		{
			ans += abs(o[oz].fi-opos)+1;
			opos = o[oz].fi;
			oz++;
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
}
