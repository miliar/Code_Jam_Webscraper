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

long long ps[80000];
int pp;

void cp()
{
  pp=0;
  FOR(p,2,1000000)
  {
    bool pr=true;
    REP(i,pp)
    {
      if((p%ps[i])==0) { pr=false; break; }
      if(ps[i]*ps[i]>p) break;
    }
    if(pr) ps[pp++]=p;
  }
}

void _case(int casenum)
{
  long long n; scanf("%lld ",&n);
  int res=0;

  REP(i,pp)
  {
    int e=0;
    long long p=1;
    while((p*ps[i])<=n) { p*=ps[i]; e++; }
    res+=(e-1);
    if(e<=1) break;
  }

  printf("Case #%d: %d\n",casenum,res+1);
}

int main()
{
  cp();
  int n;
  scanf("%d ",&n);
  FOR(i,1,n) _case(i);
  return 0;
}
