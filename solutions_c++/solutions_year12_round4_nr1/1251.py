/* AnilKishore * India */

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <algorithm>
#include <string>

#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PI;

#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define F first
#define S second
#define SET(v,x) memset(v,x,sizeof v)
#define FOR(i,a,b) for(int _n(b),i(a);i<_n;i++) 
#define EACH(it,v) for(typeof((v).begin()) it = (v).begin();it!=(v).end();it++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define SORT(v) sort(ALL(v))
#define SZ(v) int(v.size())
#define SI ({int x;scanf("%d",&x);x;})

#define MX 10004

int n, d[MX], l[MX], D, m[MX];

bool yes(int clen, int cind)
{
	//printf("\n%d, %d\n",clen,cind);
	if(D-d[cind]<=clen) return true;
	int j = -1, mxd = -1;
	for(int i=cind+1;i<n;i++)
		if(d[i]-d[cind]>clen) break;
		else
		{
			int cd = min(d[i]-d[cind],l[i]);
			if(mxd<cd){ mxd=cd; j = i; }
		}
	if(j==-1) return false;
	return yes(mxd,j);
}


bool yo()
{
	SET(m,0);
	m[0] = d[0];
	REP(i,n)
	{
		for(int j=i+1;j<n && d[j]-d[i]<=m[i];j++)
			m[j] = max( m[j], min(l[j],d[j]-d[i]) );
	}
	REP(i,n) if(D-d[i]<=m[i]) return true;
	return false;
}


int main()
{
	for(int kase=1,kases=SI;kase<=kases;kase++)
	{
		printf("Case #%d: ",kase);
		n = SI;
		REP(i,n){ d[i] = SI; l[i] = SI; }
		D = SI;
		//puts(yes(d[0],0)?"YES":"NO");
		puts(yo()?"YES":"NO");
	}
	
		
	return 0;
}

