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

char s[64];

bool skus(int pos)
{
//  printf("%s\n",s);
  if(s[pos]=='?')
  {
    s[pos]='0'; if(skus(pos+1)) return true;
    s[pos]='1'; if(skus(pos+1)) return true;
    s[pos]='?'; return false;
  }
  if(s[pos]=='0') return skus(pos+1);
  if(s[pos]=='1') return skus(pos+1);
  if(s[pos]==0)
  {
    long long x=0;
    int i=0; while(s[i]) { x=2*x+(s[i]-'0'); i++; }
    long long y=(long long)(sqrt((long double)x));
//printf("%d %d %d %d %d\n",y,y*y,(y-1)*(y-1),(y+1)*(y+1),x);
    if(y*y==x) return true;
    if((y-1)*(y-1)==x) return true;
    if((y+1)*(y+1)==x) return true;
  }
  return false;
}

void _case(int casenum)
{
  scanf("%s ",s);
  skus(0);
  printf("Case #%d: %s\n",casenum,s);
}

int main()
{
  int n;
  scanf("%d ",&n);
  FOR(i,1,n) _case(i);
  return 0;
}
