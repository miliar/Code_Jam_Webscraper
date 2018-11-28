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

int d,k;
int s[10];

bool isprime(int x)
{
  if(x<2) return false;
  for(int i=2;i*i<=x;i++) if((x%i)==0) return false;
  return true;
}

void _case(int casenum)
{
  scanf("%d%d",&d,&k);
  int h=1; REP(i,d) h*=10;
  REP(i,k) scanf("%d",&s[i]);
  int m=s[0]; REP(i,k) m=max(m,s[i]);

  if(k==1) { printf("Case #%d: I don't know.\n",casenum); return; }

  int res=-1;
  FOR(p,m+1,h)
    if(isprime(p))
      REP(a,p)
      {
        bool ok=true;
        int b=(p+s[1]-(a*s[0])%p)%p;
        FOR(j,1,k-2) if(((a*s[j]+b)%p)!=s[j+1]) ok=false;
        if(ok)
        {
          int nxt=(a*s[k-1]+b)%p;
          if(res==-1) res=nxt;
          if(res!=nxt) { printf("Case #%d: I don't know.\n",casenum); return; }
        }
      }

  printf("Case #%d: %d\n",casenum,res);
}

int main()
{
  int n;
  scanf("%d ",&n);
  FOR(i,1,n) _case(i);
  return 0;
}
