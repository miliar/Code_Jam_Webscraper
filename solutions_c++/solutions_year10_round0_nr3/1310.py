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
  int r,k,n;
  scanf("%d%d%d",&r,&k,&n);
  int g[1001];
  REP(i,n) scanf("%d",&g[i]);
  printf("Case #%d: ",casenum);

  int sum=0; REP(i,n) sum+=g[i];
  if(sum<=k)
  {
    long long res=sum;
    res*=r;
    printf("%lld\n",res);
    return;
  }

  int m[1001];
  int p[1001];
  REP(i,n) m[i]=-1;
  int mm=0;
  int pp=0;
  int i=0;

  while((m[i]==-1)&&(r))
  {
    m[i]=mm;
    p[i]=pp++;
    int t=0;
    while(t+g[i]<=k) { t+=g[i]; mm+=g[i]; i=(i+1)%n; }
    r--;
  }
 
  long long res=mm;

  if(r)
  {
    res+=(long long)(mm-m[i]) * (long long)(r/(pp-p[i]));
    r%=(pp-p[i]);
  }

  while(r)
  {
    int t=0;
    while(t+g[i]<=k) { t+=g[i]; res+=g[i]; i=(i+1)%n; }
    r--;
  }

  printf("%lld\n",res);
}

int main()
{
  int n;
  scanf("%d ",&n);
  FOR(i,1,n) _case(i);
  return 0;
}
