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
#define INF 999888

vector<string> split(const string& s, const string& delim=" ")
{ vector<string> res; string t; for(unsigned int i=0;i<s.length();i++) { if(delim.find(s[i])!=string::npos) { if(!t.empty()) { res.PB(t); t=""; } } else t+=s[i]; } if(!t.empty()) res.PB(t); return res; }
vector<int> splitint(const string& s, const string& delim=" ") { vector<string> vs=split(s); vector<int> res; for(unsigned int i=0;i<vs.size();i++) res.PB(atoi(vs[i].c_str())); return res; }

int type[10010];
int val[10010];
int cble[10010];

int m[10010][2];

void _case(int casenum)
{
  int M,v,i,x;
  scanf("%d%d ",&M,&v);
  for(i=1;i<=(M-1)/2;i++) scanf("%d%d ",&type[i],&cble[i]); 
  for(;i<=M;i++) { scanf("%d",&x); m[i][x]=0; m[i][x^1]=INF; }  
  for(i=(M-1)/2;i>=1;i--)
  {
    int a=2*i,b=2*i+1;
    int g[2];
    // result=0
    g[0]=m[a][0]+m[b][0];
    g[1]=min(m[a][0]+m[b][0],min(m[a][0]+m[b][1],m[a][1]+m[b][0]));
    if(cble[i]) m[i][0]=min(g[type[i]],g[type[i]^1]+1);
      else m[i][0]=g[type[i]];
    // result=1
    g[0]=min(m[a][1]+m[b][1],min(m[a][1]+m[b][0],m[a][0]+m[b][1]));
    g[1]=m[a][1]+m[b][1];
    if(cble[i]) m[i][1]=min(g[type[i]],g[type[i]^1]+1);
      else m[i][1]=g[type[i]];
    m[i][0]=min(m[i][0],INF);
    m[i][1]=min(m[i][1],INF);
  }
  printf("Case #%d: ",casenum);
  if(m[1][v]<INF) printf("%d\n",m[1][v]); else printf("IMPOSSIBLE\n");
}

int main()
{
  int n;
  scanf("%d ",&n);
  FOR(i,1,n) _case(i);
  return 0;
}
