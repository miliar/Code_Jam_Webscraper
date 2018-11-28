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

int pb(int x) { int r=0; while(x) { if(x&1) r++; x/=2; } return r; }

void _case(int casenum)
{
  int n;
  vector<int> a,b;
  vector<string> c;
  cin >> n;
  REP(i,n) { string cc; int aa,bb; cin >> cc >> aa >> bb; a.PB(aa); b.PB(bb); c.PB(cc); }
  int res=9999;
  REP(x,(1<<n))
  {
    set<string> s;
    REP(i,n)if(x&(1<<i))s.insert(c[i]);
    if(s.size()>3) continue;
    bool ok[10001];
    FOR(j,1,10000) ok[j]=false;
    REP(i,n)if(x&(1<<i))FOR(j,a[i],b[i])ok[j]=true;
    ok[0]=true;
    FOR(j,1,10000)if(!ok[j])ok[0]=false;
    if(!ok[0]) continue;
    if(pb(x)<res) res=pb(x);
  }
  printf("Case #%d: ",casenum);
  if(res==9999) printf("IMPOSSIBLE\n"); else printf("%d\n",res);
}

int main()
{
  int n;
  cin >> n;
  FOR(i,1,n) _case(i);
  return 0;
}
