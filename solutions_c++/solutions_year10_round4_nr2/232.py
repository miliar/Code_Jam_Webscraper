//DEDICATED TO EMMA WATSON, THE BRITISH *SUNSHINE*
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
//#include <fstream>

#define eps 10e-10
#define INF 1000000000
#define PI 3.141592653589793238462
#define EU 2.71828182845904523536
#define sz(a) (int)a.size()
#define pb(a) push_back(a)
#define mset(a,hodnota) memset(a,hodnota,sizeof(a))
#define wh(a) a.begin(),a.end()
#define REP(i,n) for(__typeof(n) i=0;i<(n);++i)
#define REPS(i,n) for(int(i)=0;i<int(n.size());++i)
#define FOR(i,a,b) for(__typeof(b) i=(a);i<=(b);++i)
#define FORD(i,a,b) for(__typeof(a) i=(a);i>=(b);--i)
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define SQR(a) ((a)*(a))
#define pii pair<int,int>
#define mp(a,b) make_pair(a,b)
#define fi first
#define se second
typedef long long ll;
typedef long double ld;
using namespace std;

int P,N;
int M[1050];
int C[12][1050];
ll DP[12][12][1050];//level, missed, index
ll solve(int lev,int missed,int ind)
{
  ll &res=DP[lev][missed][ind];
  if (res!=-1) return res;
  //bottom level?
  if (lev==P)
    return res=(missed<=M[ind]?0:INF);
  

  //buy ticket
  res=solve(lev+1,missed,ind*2)+solve(lev+1,missed,ind*2+1)+C[lev][ind];

  //don't buy
  res=min(res,solve(lev+1,missed+1,ind*2)+solve(lev+1,missed+1,ind*2+1));

  return res;
}
void solve_case()
{
  mset(DP,-1);
  scanf("%d",&P);
  N=1<<P;
  REP(i,N)
    scanf("%d",&M[i]);
  FORD(i,P-1,0)
  {
    int K=1<<i;
    REP(j,K)
      scanf("%d",&C[i][j]);      
  }
  
  ll res=solve(0,0,0);
  cout<<res<<endl;
}


int cases;
int main( )
{
  scanf("%d",&cases);getchar();
  REP(ii,cases)
  {
    printf("Case #%d: ",ii+1);
    solve_case();
  }         
  return 0;
}
