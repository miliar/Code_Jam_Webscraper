
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
void solve_case(int TT)
{
  int c[10][520];
  mset(c,0);
  scanf("%d",&P);getchar();

  vector<int> M(1<<P); 
  REP(i,1<<P)
  { 
    scanf("%d",&M[i]);
    M[i]=P-M[i];
  }
/*  REP(i,sz(M)) cout<<M[i]<<" ";
  cout<<endl;*/
  REP(j,P)
    for(int i=(1<<(P-1-j))-1;i>=0;i--)
      scanf("%d",&c[j][i]);
 /* REP(i,10)
  {
    REP(j,10)
     cout<<c[i][j];
    cout<<endl;
  }*/
  int poc=0;
  REP(i,sz(M))
  {
    REP(j,M[i])
    {
      int poz=i;
      REP(k,P-j) poz/=2;
//      cout<<" "<<P-j<<" "<<i<<" "<<poz<<endl;      
      if(c[P-1-j][poz]==1)
      {
        c[P-1-j][poz]=2;
        poc++;
      }
    }
  }
/*  REP(i,10)
  {
    REP(j,10)
     cout<<c[i][j];
    cout<<endl;
  }*/
  printf("Case #%d: %d\n",TT+1,poc);
  
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

