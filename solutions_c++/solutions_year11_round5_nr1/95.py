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

long double area(vector<pair<int,int> > &v, long double x)
{
  int n=v.size();
  long double res=0;
  int i=1;
  while((i<n)&&(x>v[i].first)) { res+=(v[i-1].second+v[i].second)*(v[i].first-v[i-1].first)*0.5; i++; }
  long double y=v[i-1].second+(v[i].second-v[i-1].second)*(x-v[i-1].first)/(v[i].first-v[i-1].first);
  res+=(y+v[i-1].second)*(x-v[i-1].first)*0.5;
  return res;
}

void _case(int casenum)
{
  int w,nlow,nupp,g; scanf("%d%d%d%d",&w,&nlow,&nupp,&g);
  vector<pair<int,int> > low,upp;
  REP(i,nlow) { int x,y; scanf("%d%d",&x,&y); low.PB(MP(x,y)); }
  REP(i,nupp) { int x,y; scanf("%d%d",&x,&y); upp.PB(MP(x,y)); }
  long double tot=area(upp,w)-area(low,w);
  printf("Case #%d:\n",casenum);
//printf("total = %.8Lf\n",tot);
  FOR(i,1,g-1)
  {
    long double tar=tot*(long double)i/((long double)g);
//printf("target = %.8Lf\n",tar);
    long double ll=0,mm=0,hh=w;
    while(hh-ll>1e-8)
    {
      mm=(ll+hh)/2.0;
      if(area(upp,mm)-area(low,mm)>tar) hh=mm; else ll=mm;
//printf("%.8Lf : %.8Lf\n",mm,area(upp,mm)-area(low,mm));
    }
    printf("%.8Lf\n",mm);
  }
}

int main()
{
  int n;
  scanf("%d ",&n);
  FOR(i,1,n) _case(i);
  return 0;
}
