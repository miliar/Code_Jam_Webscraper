#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <numeric>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) int((c).size())

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<VPII> VVPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;

map<string,int> cor_ind;

int MapColor(const string &col) {
     if(!cor_ind.count(col))cor_ind.insert(make_pair(col,SZ(cor_ind)));
     return cor_ind[col];
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int n,test;
	
	for(cin>>n,test=1;test<=n;++test) {
             cor_ind.clear();
             VVPII off;
             int n;
             cin>>n;
             REP(i,n) {
                  PII cur;
                  string col;
                  int ci;
                  cin>>col>>cur.X>>cur.Y;
                  ci=MapColor(col);
                  if(SZ(off)<=ci)off.resize(ci+1);
                  off[ci].pb(cur);
             }
             int res=INF;
             REP(c1,SZ(off))FOR(c2,c1,SZ(off))FOR(c3,c2,SZ(off)) {
                  VPII offs;
                  offs.insert(offs.end(),ALL(off[c1]));
                  offs.insert(offs.end(),ALL(off[c2]));
                  offs.insert(offs.end(),ALL(off[c3]));
                  UNIQUE(offs);
                  int cnt=0,nxt=1,end=-1,i=0,osz=SZ(offs);
                  bool ok=true;
                  for(;i<osz&&ok&&nxt<=10000;) {
                       while(i<osz&&offs[i].X<=nxt) {
                            end=max(end,offs[i].Y);
                            i++;
                       }
                       if(end>=nxt) {
                            cnt++;
                            nxt=end+1;
                       }
                       else ok=false;
                  }
                  if(nxt!=10001)ok=false;
                  if(ok)res=min(res,cnt);
             }
             if(res==INF)printf("Case #%d: IMPOSSIBLE\n",test);
             else printf("Case #%d: %d\n",test,res);
	}
	
	fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
	return 0;
} 
