#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>

using namespace std;

#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)

int INF = 1000000;

vector<int> d;
vector<int> l;
int n;
int D;

int dp[10010];

bool solve() {
  memset(dp, ~0, sizeof(dp));
  dp[0] = d[0];
  rep(i, n-1) {
    int to = upper_bound(all(d), d[i]+dp[i]) - d.begin();
    for(int j = i+1; j < to; ++j) {
      //      cout << j << " " << d[j]-d[i] << " " << l[i] <<endl;
      int len = min(d[j]-d[i], l[j]);
      dp[j] = max(dp[j], len);
    }
  }

  rep(i, n) {
    if(dp[i] != -1 && dp[i] + d[i] >= D) {
      return true;
    }
  }
  return false;
}

int main(){
  int t; scanf("%d\n", &t);
  for(int j = 1;j<=t;j++){
    cin >> n;
    d.clear(); d.resize(n);
    l.clear(); l.resize(n);
    rep(i, n) {
      cin >> d[i] >> l[i];
    }
    cin >> D;
    string ans = solve() ? "YES" : "NO";
    cout << "Case #" << j << ": " << ans <<endl;
  }
  return 0;

}
