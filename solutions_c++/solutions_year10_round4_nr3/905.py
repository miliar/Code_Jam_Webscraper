
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

int P;
bool a[2][1200][120];
void solve_case(int TT)
{
  scanf("%d",&P);getchar();
  mset(a,0);
  bool akt=0;
  int x,x1,y,y1;
  REP(i,P)
  {
    scanf("%d %d %d %d",&x,&y,&x1,&y1);
    for(int ii=x;ii<=x1;ii++)
      for(int jj=y;jj<=y1;jj++)
        a[akt][ii][jj]=1;
  }
  int maxx=100,poc=1,T=0;
  while(poc)
  {
    poc=0;
    for(int ii=1;ii<=maxx;ii++)
      for(int jj=1;jj<=110;jj++)
      {
        if(!a[akt][ii-1][jj] && !a[akt][ii][jj-1]){ a[!akt][ii][jj]=0; }
        else
        if(a[akt][ii-1][jj] && a[akt][ii][jj-1] && a[!akt][ii][jj]==0)
        {
          a[!akt][ii][jj]=1;
          poc++;
        }
        else if(a[akt][ii][jj]==1)
        {
          a[!akt][ii][jj]=1;
          poc++;
        }        
      }
    mset(a[akt],0);
    akt=!akt;
//    cout<<poc<<endl;
    maxx++;
    T++;
  }
  printf("Case #%d: %d\n",TT+1,T);
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

