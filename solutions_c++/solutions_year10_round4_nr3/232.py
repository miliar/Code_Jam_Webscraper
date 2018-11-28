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

int M[1005][1005];
vector<pii> V,C;
#define MAX_IT 155
void solve_case()
{
  int R;
  scanf("%d",&R);
  mset(M,0);
  REP(i,R)
  {
    int a,b,c,d;
    scanf("%d %d %d %d",&a,&b,&c,&d);
    FOR(k,a,c)
      FOR(kk,b,d)
        M[k][kk]=1;
  }
  int total=0;
  REP(i,105)REP(j,105)
    total+=M[i][j];
  int T=0;
  while(total)
  {
    T++;
    V.clear();
    C.clear();
    FOR(i,1,MAX_IT)
      FOR(j,1,MAX_IT)
      {
        if (M[i][j] && M[i-1][j]==0 && M[i][j-1]==0)
          V.pb(mp(i,j));
        if (M[i][j]==0 && M[i-1][j] && M[i][j-1])
          C.pb(mp(i,j));
      }
    FORE(it,V)
      M[it->fi][it->se]=0,total--;

    FORE(it,C)
      M[it->fi][it->se]=1,total++;
  }
  cout<<T<<endl;



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
