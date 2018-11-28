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
typedef long long ll;
using namespace std;
int P[105];
void solve_case()
{
  int N,L,H;
  scanf("%d %d %d",&N,&L,&H);
  REP(i,N)
    scanf("%d", &P[i]);
  int ans=-1;
  FOR(n,L,H)
  {
    int isok=1;
    REP(i,N)
    {
      if (P[i]==n)continue;
      if (P[i]>n && P[i]%n == 0)continue;
      if (P[i]<n && n%P[i] == 0)continue;
      isok=0;
    }
    if (isok) {ans=n;break;}

  }
  if (ans==-1) cout<<"NO"<<endl;
  else
  cout<<ans<<endl;


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



