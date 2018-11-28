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

#define eps 1e-11
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
typedef long long LL;
using namespace std;
int N,L,T,C;
int D1[1005];
LL D[1000005];
vector<LL> V;
void solve_case()
{
  scanf("%d %d %d %d",&L,&T,&N,&C);
  REP(i,C)
    scanf("%d",&D1[i]);
  REP(i,N)
    D[i]=D1[i%C];
  V.clear();
  LL cur=0;
  REP(i,N)
  {
    if (cur+D[i]*2<=T)cur+=D[i]*2;
    else
    {
      LL rem = D[i] - (T-cur)/2;
      
      V.pb(rem);
      FOR(j,i+1,N-1)
        V.pb(D[j]);
      break;
    }
  }
  cur=T;
  sort(wh(V));
  reverse(wh(V));

  REPS(i,V)    
  {
//     cout<<i<<" "<<V[i]<<endl;
    if (i<L)cur+=V[i];
    else cur+=V[i]*2;
  }
  cout<<cur<<endl;



}

int main()
{
  int cases;
  scanf("%d",&cases);getchar();
  REP(kk,cases)
  {
    cout<<"Case #"<<kk+1<<": ";
    solve_case();
  }
  return 0;
}



