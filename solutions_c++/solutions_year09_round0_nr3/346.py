#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;
string match = "welcome to code jam";
int m = match.size();
string text;
int n;
int MOD = 10000;
int memo[36][512];

int dp(int x, int y) {
  if (x == m) return 1;
  if (y == n) return 0;
  if (memo[x][y] != -1) return memo[x][y];

  char c = match[x];
  int ret = 0;
  for (int i = y; i < n; ++i) {
    if (text[i] == c) {
      ret += dp(x+1, i+1);
      ret %= MOD;
    }
  }
  return memo[x][y] = ret;
}

int main() {
  int numcase;
  string junk;
  cin >> numcase;
  getline(cin, junk);
  for (int ncase = 1; ncase <= numcase; ++ncase) {
    getline(cin, text);
    n = text.size();
    memset(memo, -1, sizeof(memo));
    int ans = dp(0, 0);
    printf("Case #%d: %04d\n", ncase, ans);
  }
}
