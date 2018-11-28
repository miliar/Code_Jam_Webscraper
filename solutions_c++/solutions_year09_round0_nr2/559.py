
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#define REP(i,u) for(__typeof(u) i=0;i<(u);i++)
#define REPS(i,n) for(int(i)=0;i<int(n.size());++i)
#define FOR(i,a,b) for(__typeof(a) i=(a);i<=(b);i++)
#define FORD(i,a,b) for(__typeof(a) i=(a);i>=(b);i--)
#define FORE(it,c) for(__typeof(c.begin()) it=(c).begin();it!=(c).end();it++)
#define SQR(a) ((a)*(a))
#define all(qq) qq.begin(),qq.end()
#define rall(qq) qq.rbegin(),qq.rend()
#define mset(a,u) memset(a,u,sizeof(a))
#define sz(a) ((int)a.size())
#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define fi first
#define se second
#define PI 3.141592653589793238462

using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> pii;

int f;
int kam[4][2]={{-1,0},{0,-1},{0,1},{1,0}},s[3];
int t[105][105][3],H,W,res[30];
int getfarba(int h, int w)
{
  if(t[h][w][1]!=0) return t[h][w][1];
  s[0]=t[h][w][0];
  REP(i,4)
    if(s[0]>t[h+kam[i][0]][w+kam[i][1]][0])
    {
      s[0]=t[h+kam[i][0]][w+kam[i][1]][0];
      s[1]=kam[i][0];
      s[2]=kam[i][1];      
    }
  if(s[0]==t[h][w][0]) return t[h][w][1]=f++;
  return t[h][w][1]=getfarba(h+s[1],w+s[2]);
}

void solve_case(int cases)
{
  cin>>H>>W;
  f=1;
  mset(res,0);
  REP(i,W+2)
  {
    t[0][i][0]=1000000;
    t[H+1][i][0]=1000000;
  }
  REP(i,H+2)
  {
    t[i][0][0]=1000000;
    t[i][W+1][0]=1000000;
  }
  REP(i,H)
  {
    REP(j,W)
    {
      scanf("%d",&t[i+1][j+1][0]);
      t[i+1][j+1][1]=0;
    }
  }
  REP(i,H)
  {
    REP(j,W)
    {
      if(t[i+1][j+1][1]==0) t[i+1][j+1][1]=getfarba(i+1,j+1);
//      cout<<t[i+1][j+1][1]<<" ";
    }
//    cout<<endl;
  }

  char c='a';
  printf("Case #%d:\n",cases+1);  
  REP(i,H)
  {
    REP(j,W)
    {
      if(res[t[i+1][j+1][1]]==0) res[t[i+1][j+1][1]]=c++;
      if(j!=0) putchar(' ');
      putchar(res[t[i+1][j+1][1]]);
    }
    putchar(10);
  }
}


int cases;
int main( )
{
  scanf("%d",&cases);getchar();
  REP(ii,cases)
  {
    solve_case(ii);
  }         
  return 0;
}

