#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <complex>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <queue>
#include <set>
#include <map>
#include <valarray>
#include <bitset>
#include <stack>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
typedef long long ll;
typedef pair<int,int> pii;
const int INF = 1<<29;
const double PI = acos(-1);
const double EPS = 1e-8;

int dp[10010];
int d[10010];
int l[10010];

int main() {
  int T;
  cin>>T;
  REP(t,T) {
    int n;
    cin >> n;
    REP(i,n) {
      cin >> d[i] >> l[i];
    }
    int D; cin >> D;
    memset(dp,0,sizeof(dp));
    dp[0] = d[0];
    bool ans = 0;
    for (int i=0; i<n; ++i) {
      for (int j=i+1; j<n; ++j) {
        if (d[i]+dp[i] < d[j]) break;
        dp[j] = max(dp[j], min(l[j], d[j]-d[i]));
      }
      if (d[i]+dp[i]>=D) ans = 1;
      //cout << dp[i] << " ";
    }
    //cout << endl;
    printf("Case #%d: %s\n", t+1, ans?"YES":"NO");
  }
}
