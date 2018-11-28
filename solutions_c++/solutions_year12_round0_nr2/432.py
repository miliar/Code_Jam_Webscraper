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

bool surprisable[31];
bool unsurprisable[31];
int smx[31];
int umx[31];

bool check() {
  for(int i = 0; i < 11; ++i) {
    for(int j = i; j - i <= 2 && j < 11; ++j) {
      for(int k = i; k - i <= 2 && k < 11 ; ++k) {
	if(j-i == 2 || k-i == 2) {
	  surprisable[i+j+k] = true;
	  smx[i+j+k] = max(smx[i+j+k], k);
	}else {
	  unsurprisable[i+j+k] = true;
	  umx[i+j+k] = max(umx[i+j+k], k);
	}
      }
    }
  }
}

int dp[111][111];
int solve(const vector<int>& scores, int n, int s, int p) {
  memset(dp, 0, sizeof(dp));
  rep(i, n) {
    rep(j, 105) {
      if(surprisable[scores[i]]) {
	int best_increase = smx[scores[i]] >= p ? 1 : 0;
	dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+best_increase);
      }
      if(unsurprisable[scores[i]]) {
	int best_increase = umx[scores[i]] >= p ? 1 : 0;
	dp[i+1][j] = max(dp[i+1][j], dp[i][j]+best_increase);
      }
    }
  }
  return dp[n][s];
}

int main(){
  int t; scanf("%d\n", &t);

  rep(i, 31) {
    surprisable[i] = false;
    unsurprisable[i] = false;
    smx[i] = 0;
    umx[i] = 0;
  }

  check();
  for(int j = 1; j<=t; j++){
    int n, s, p; cin >> n >> s >> p;
    vector<int> scores(n);
    rep(i, n) {
      cin >> scores[i];
    }
    int ans = solve(scores, n, s, p);
    cout << "Case #" << j << ": " << ans <<endl;
  }
  return 0;

}
