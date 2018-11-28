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
  int p[10010]; FOR(x,0,10001) p[x]=0;
  int n; scanf("%d",&n);
  REP(i,n) { int x; scanf("%d",&x); p[x]++; }

  vector<int> b,e;
  FOR(x,1,10001)
  {
    if(p[x]>p[x-1]) REP(i,p[x]-p[x-1]) b.PB(x);
    if(p[x]<p[x-1]) REP(i,p[x-1]-p[x]) e.PB(x);
  }

  int m=b.size();
  int res=1000000;
  REP(i,m) res=min(res,e[i]-b[i]);
  if(n==0) res=0;

  printf("Case #%d: %d\n",casenum,res);
}

int main()
{
  int n;
  scanf("%d ",&n);
  FOR(i,1,n) _case(i);
  return 0;
}
