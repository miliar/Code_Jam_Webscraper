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

int N,M;

bool getdiv(int x, int &a, int &b) // x=a*b, 0<=a<=N, 0<=b<=M
{
  if(x==0) { a=b=0; return true; }
  if(x==1) { a=b=1; return (N>=1); }
  for(int d=(x%M)?(x/M+1):(x/M);d<=N;d++)
    if(((x%d)==0)&&((x/d)<=M)) { a=d; b=x/d; return true; } 
  return false;
}

void _case(int casenum)
{
  int A;
  scanf("%d%d%d",&N,&M,&A);
  int a=0,b,c,d;
  FOR(p,A,N*M)
  {
    if(getdiv(p,a,b)&&getdiv(p-A,c,d)) break;
    a=0;
  }
  if(a) printf("Case #%d: 0 0 %d %d %d %d\n",casenum,a,d,c,b);
  else printf("Case #%d: IMPOSSIBLE\n",casenum);
}

int main()
{
  int n;
  scanf("%d ",&n);
  FOR(i,1,n) _case(i);
  return 0;
}
