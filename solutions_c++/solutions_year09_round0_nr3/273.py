#include <iostream>
using namespace std;

string fmt(int v) {
  string s(4, ' ');
  for (int i = 3; i >= 0; i--) {
    s[i] = ('0' + (v % 10));
    v /= 10;
  }
  return s;
}

int dp[1000][20];
int main() {
  string match = "welcome to code jam";

  int t; cin >> t;
  string dummy; getline(cin, dummy);
  for (int c = 1; c <= t; c++) {
    string s; getline(cin, s);
    memset(dp, 0, sizeof(dp));

    dp[0][0] = 1;
    for (int i = 1; i <= s.size(); i++)
      for (int j = 1; j <= match.size(); j++) {
        if (s[i-1] != match[j-1]) continue;

        for (int k = 0; k < i; k++) {
          dp[i][j] += dp[k][j-1];
          dp[i][j] %= 10000;
        }
      }

    int total = 0;
    for (int i = 1; i <= s.size(); i++)
      total += dp[i][match.size()];
    total %= 10000;
    cout << "Case #" << c << ": " << fmt(total) << endl;
  }
  return 0;
}
