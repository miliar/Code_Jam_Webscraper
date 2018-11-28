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
using namespace std;
 
#define all(c) ((c).begin()), ((c).end()) 
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end()) 
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back
#define mp make_pair

const string S = "welcome to code jam";
int dp[100];

int main() {
  int cases;
  cin >> cases;
  scanf(" ");

  rep (ca, cases) {
    string in;
    getline(cin, in);

    memset(dp, 0, sizeof(dp));
    dp[0] = 1;
    rep (i, in.length()) {
      char c = in[i];
      for (int j = S.length() - 1; j >= 0; j--) {
        if (S[j] == c) dp[j + 1] = (dp[j + 1] + dp[j]) % 10000;
      }
    }
    printf("Case #%d: %04d\n", ca + 1, dp[S.length()]);
  }

  return 0;
}
