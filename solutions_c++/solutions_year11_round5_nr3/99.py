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
char a[8][8];
int d[8][8];

int poc()
{

  int p[8][8]; REP(i,r)REP(j,c) p[i][j]=0;
  REP(i,r)REP(j,c)
  {
    if((a[i][j]=='|')&&(d[i][j]==0)) p[(i+1+r)%r][(j+c)%c]++;
    if((a[i][j]=='|')&&(d[i][j]==1)) p[(i-1+r)%r][(j+c)%c]++;
    if((a[i][j]=='-')&&(d[i][j]==0)) p[(i+r)%r][(j+1+c)%c]++;
    if((a[i][j]=='-')&&(d[i][j]==1)) p[(i+r)%r][(j-1+c)%c]++;
    if((a[i][j]=='/')&&(d[i][j]==0)) p[(i+1+r)%r][(j-1+c)%c]++;
    if((a[i][j]=='/')&&(d[i][j]==1)) p[(i-1+r)%r][(j+1+c)%c]++;
    if((a[i][j]=='\\')&&(d[i][j]==0)) p[(i+1+r)%r][(j+1+c)%c]++;
    if((a[i][j]=='\\')&&(d[i][j]==1)) p[(i-1+r)%r][(j-1+c)%c]++;
  }
  
//  REP(i,r){REP(j,c) printf("%d",p[i][j]); printf("\n"); } printf("\n");

  REP(i,r)REP(j,c) if(p[i][j]!=1) return 0;
  return 1;
}


int skus(int i, int j)
{
  if((i<r)&&(j<c))
  {
    int ii=i,jj=j; jj++; if(jj==c) { jj=0; ii++; }
    
    int res=0;
    d[i][j]=0; res+=skus(ii,jj);
    d[i][j]=1; res+=skus(ii,jj);
    return res;
  }
  else
  {
    return poc();
  }
}

void _case(int casenum)
{
  scanf("%d %d ",&r,&c);
  REP(i,r) scanf("%s",a[i]);
  int res=skus(0,0);
  printf("Case #%d: %d\n",casenum,res%1000003);
}

int main()
{
  int n;
  scanf("%d ",&n);
  FOR(i,1,n) _case(i);
  return 0;
}
