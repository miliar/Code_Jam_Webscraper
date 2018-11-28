#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<sstream>
#include<cassert>
#include<queue>
#include<stack>
#include<bitset>
#include<cstring>

#define REP(i,b,n) for(int i=b;i<(int)n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define FOR(it,o)  for(__typeof((o).begin()) it=(o).begin(); it!=(o).end(); ++it)

using namespace std;
typedef long long lli;
typedef vector<int> vint;
typedef pair<int, int> pii;
const double EPS = 0.00000001;
const int INF = 1000000000;
template<class T> void pp(T t, int n){
  rep(i, n){
    cout << t[i] << ' ';
  }
  cout << endl;
}

int main(){
  int T;
  cin >> T;
  rep(tc, T){
    cout << "Case #" << tc+1 << ": ";
    int n;
    cin >> n;
    vector<int> v(n);
    rep(i, n){
      cin >> v[i];
    }
    int ans = -1;
    bitset<20> B;
    rep(i, (1<<n)){
      B = i;
      int psum[2], sum[2];
      rep(i, 2)psum[i] = sum[i] = 0;
      rep(i, n){
        int id = 0;
        if(B[i]){
          id = 1;
        }
        psum[id] ^= v[i];
        sum[id] += v[i];
      }
      if(psum[0] == psum[1]){
        if(min(sum[0], sum[1]) == 0)continue;
        ans = max(ans, max(sum[0], sum[1]));
      }
    }
    if(ans < 0){
      cout << "NO" << endl;
    }
    else cout << ans << endl;
  }
  return 0;
}
