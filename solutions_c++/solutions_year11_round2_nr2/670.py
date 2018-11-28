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

vector<string> split(const string& s, const string& delim=" ")
{ vector<string> res; string t; for(unsigned int i=0;i<s.length();i++) { if(delim.find(s[i])!=string::npos) { if(!t.empty()) { res.PB(t); t=""; } } else t+=s[i]; } if(!t.empty()) res.PB(t); return res; }
vector<int> splitint(const string& s, const string& delim=" ") { vector<string> vs=split(s); vector<int> res; for(unsigned int i=0;i<vs.size();i++) res.PB(atoi(vs[i].c_str())); return res; }

void _case(int casenum)
{
  int c,d; scanf("%d%d",&c,&d);
  int p[202],v[202]; REP(i,c) scanf("%d%d",&p[i],&v[i]);
  double ll=0,hh=1e9,mm;
  while((hh-ll)>1e-9)
  {
    mm=(ll+hh)/2;
    bool ok=true;

    double f=-10e10;
    REP(i,c)
    {
      f=max(f,(double)p[i]-mm);
      if(f+(double)(v[i]-1)*(double)d>p[i]+mm) { ok=false; break; }
      f+=(double)v[i]*(double)d;
    }

    if(ok) hh=mm; else ll=mm;
  }
  printf("Case #%d: %.9lf\n",casenum,mm);
}

int main()
{
  int n;
  scanf("%d ",&n);
  FOR(i,1,n) _case(i);
  return 0;
}
