// include {{{
#include <cstdio>
#include <iostream>
//#include <sstream>
#include <string>
#include <vector>
//#include <deque>
#include <stack>
#include <queue>
//#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <numeric>
//#include <complex>
// }}}
using namespace std;
// macro {{{
typedef long long ll;
typedef vector<int> vec;
typedef vector<vec> mat;
typedef pair<int,int> P;
#define rep(i,n) for(int i=0;i<(n);++i)
#define REP(i,j,k) for(int i=j;i<(k);++i)
#define foreach(it,v) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();++it)
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define priority_queue_greater(T) priority_queue< T, vector<T>, greater<T> >
// }}}

int T;
int n,D;
int main(){
  cin >> T;
  REP(times,1,T+1){
    cin >> n;
    vec d(n+1), l(n+1);
    rep(i,n){ scanf("%d%d",&d[i], &l[i]); }
    cin >> d[n]; l[n] = 0;

    vec dp(n+1,-1);
    dp[0] = d[0];
    rep(i,n)REP(j,i+1,n+1){
      if( dp[i] + d[i] < d[j] ){ break; }
      dp[j] = max( dp[j], l[j] < d[j]-d[i] ? l[j] : d[j]-d[i] );
    }

    //rep(i,n+1){ cout << dp[i] << endl; }
    cout << "Case #" << times << ": " << (dp[n]<0 ? "NO" : "YES") << endl;
  }
  return 0;
}


