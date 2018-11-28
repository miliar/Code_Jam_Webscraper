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
  int n; scanf("%d ",&n);
  char a[101][101]; REP(i,n)REP(j,n) scanf("%c ",&a[i][j]);

  int w[101];
  int g[101];
  REP(i,n) { w[i]=g[i]=0; REP(j,n) if(a[i][j]=='1') { w[i]++; g[i]++; } else if(a[i][j]=='0') g[i]++; }
  
  double wp[101];
  REP(i,n) wp[i]=(double)w[i]/(double)g[i];

  double owp[101];
  REP(i,n)
  {
    owp[i]=0;
    REP(j,n) if(a[i][j]!='.')
      owp[i]+=(double)(w[j]-(a[j][i]-'0'))/(double)(g[j]-1);
    owp[i]/=(double)g[i];
  }

  double oowp[101];
  REP(i,n)
  {
    oowp[i]=0;
    REP(j,n) if(a[i][j]!='.') oowp[i]+=owp[j];
    oowp[i]/=(double)g[i];
  }

  printf("Case #%d:\n",casenum);
  REP(i,n) printf("%.12lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
}

int main()
{
  int n;
  scanf("%d ",&n);
  FOR(i,1,n) _case(i);
  return 0;
}
