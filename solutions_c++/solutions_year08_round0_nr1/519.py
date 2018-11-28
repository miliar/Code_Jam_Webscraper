#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
using namespace std;
#define REP(i,n) for(int i=0,n_=(n);i<n_;i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FOR(i,a,b) for (int i=a,b_=b;i<=(b_);i++)
#define ALL(a) a.begin(),a.end()
#define SZ(a) (int)(a).size()
#define SORT(a) sort(ALL(a))
#define INF 1073741823
#define DEB(x) cout<<#x<<":"<<x<<"\n"
#define PB(b) push_back(b)
map<string,int> Map;
char Pal[110];
int Qs[1000];
int DP[1001][101];
int q,s;
int go(int qs,int ss)
{
  if (qs==q)
    return 0;
  if (DP[qs][ss]!=-1)
  {
    return DP[qs][ss];
  }
  int &y=DP[qs][ss];
  y=INF;
  if (ss!=Qs[qs])
   {
    y=go (qs+1,ss);
    return y;
   }
  REP(i,s)
  {
    if (i==ss)
      continue;
     y=min (y,go (qs+1,i)+1);
  }
  return y;
}
int main ()
{
  int c,cas=1;
  scanf ("%d",&c);
  while (c--)
  {
    memset(DP,-1,sizeof DP);
    Map.clear();
    scanf ("%d",&s);
    gets(Pal);
    REP(i,s)
    {
      gets(Pal);
      Map[Pal]=i;
    }
    scanf ("%d",&q);
    gets(Pal);
    REP(i,q)
    {
      gets(Pal);
      //DEB(Pal);
      Qs[i]=Map[Pal];
    }
    int res=INF;
    REP(i,s)
      res=min (go (0,i),res);
     printf ("Case #%d: %d\n",cas++,res);
  }
}