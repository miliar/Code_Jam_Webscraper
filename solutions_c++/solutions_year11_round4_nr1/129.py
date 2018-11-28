#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <sstream>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
using namespace std;

#define CLEAR(t) memset((t),0,sizeof(t))
#define FOR(i,a,b) for(__typeof(a)i=(a);i<=(b);++i)
#define FORD(i,a,b) for(__typeof(a)i=(a);i>=(b);--i)
#define REP(i,n) for(__typeof(n)i=0;i<(n);++i)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)

void _case(int casenum)
{
  int x,_s,_r,_t,n; scanf("%d%d%d%d%d",&x,&_s,&_r,&_t,&n);
  double s=_s,r=_r,t=_t;
  vector<pair<double,double> > v;
  REP(i,n) { int bb,ee,ww; scanf("%d%d%d",&bb,&ee,&ww); v.PB(MP(ww,ee-bb)); x-=(ee-bb); }
  v.PB(MP(0,x));
  sort(v.begin(),v.end());

  double y=0;
  REP(i,n+1)
  if(t>=v[i].second/(r+v[i].first))
  {
    t-=v[i].second/(r+v[i].first);
    y+=v[i].second/(r+v[i].first);
  }
  else
  {
    double d=v[i].second-t*(r+v[i].first);
    y+=t;
    t=0;
    y+=d/(s+v[i].first);
  }
  printf("Case #%d: %.9lf\n",casenum,y);
}

int main()
{
  int n;
  scanf("%d ",&n);
  FOR(i,1,n) _case(i);
  return 0;
}
