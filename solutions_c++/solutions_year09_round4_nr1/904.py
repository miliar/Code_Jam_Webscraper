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

int N;
int M[55][55];
int R[55];
void solve_case()
{
  cin>>N;
  REP(i,N)
  {
    REP(j,N)
    {
      char ch;
      cin>>ch;
      M[i][j]=ch-'0';
    }
  }
  mset(R,0);
  REP(i,N)
    REP(j,N)
      if (M[i][j])
        R[i]=max(R[i],j);
  int res=0;
  REP(i,N)
  {
    int maxi_here=i;
    if (R[i]<=maxi_here)continue;
    
    int kde=i;
    while(R[kde]>maxi_here)kde++;
    FORD(j,kde,i+1)
      swap(R[j],R[j-1]),res++;
  }
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
