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

int r,c;
int id[81][81];
int m[6404];
vector<int> a[6404];
vector<int> fc;

bool ok(int i, int j)
{ return ((i>=0)&&(i<r)&&(j>=0)&&(j<c)&&(id[i][j]!=-1)); }

bool v[6404];

bool aug(int x)
{
  v[x]=true;
  REP(i,a[x].size())
  {
    if(m[a[x][i]]==-1) { m[a[x][i]]=x; m[x]=a[x][i]; return true; }
    if(!v[m[a[x][i]]])
      if(aug(m[a[x][i]])) { m[a[x][i]]=x; m[x]=a[x][i]; return true; }
  }
  return false;
}

bool augment()
{
  REP(x,fc.size())if(m[fc[x]]==-1)
  {
    CLEAR(v);
//    printf("try %d\n",fc[x]);
    if(aug(fc[x])) return true;
  }
  return false;
}

void _case(int casenum)
{
  scanf("%d %d ",&r,&c);
  int n=0;
  REP(i,r)REP(j,c)
  {
    char ch; scanf("%c ",&ch);
    if(ch=='.') id[i][j]=n++; else id[i][j]=-1;
  }
  REP(i,n)a[i].clear();
  fc.clear();
  REP(i,r)REP(j,c)if(ok(i,j))
  {
    if(ok(i,j-1)) a[id[i][j]].PB(id[i][j-1]);
    if(ok(i,j+1)) a[id[i][j]].PB(id[i][j+1]);
    if(ok(i-1,j-1)) a[id[i][j]].PB(id[i-1][j-1]);
    if(ok(i-1,j+1)) a[id[i][j]].PB(id[i-1][j+1]);
    if(ok(i+1,j-1)) a[id[i][j]].PB(id[i+1][j-1]);
    if(ok(i+1,j+1)) a[id[i][j]].PB(id[i+1][j+1]);
    if(j%2) fc.PB(id[i][j]);
  }
  REP(i,n) m[i]=-1;
  int mm=0;
//printf("n = %d\n",n);REP(i,n){REP(j,a[i].size()) printf("%d ",a[i][j]); printf("\n");}
  while(augment()) mm++;
  printf("Case #%d: %d\n",casenum,n-mm);
}

int main()
{
  int n;
  scanf("%d ",&n);
  FOR(i,1,n) _case(i);
  return 0;
}
