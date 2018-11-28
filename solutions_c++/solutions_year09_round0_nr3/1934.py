#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  int N;
  cin >> N;

  char sx[1000];
  cin.getline(sx, 1000);

  string t = "welcome to code jam";
  for (int cas = 1; cas <= N; cas++) {
    cin.getline(sx, 1000);
    string s = sx;
    //cout << s << endl;

    int dp[1000][50];
    dp[0][0] = 1;
    for (int i = 1; i <= t.size(); i++) {
      dp[0][i] = 0;
    }
    for (int i = 0; i < s.size(); i++) {
      dp[i+1][t.size()] = dp[i][t.size()];
      for (int j = t.size()-1; j >= 0; j--) {
        dp[i+1][j] = dp[i][j];
        if (s[i] == t[j]) {
          dp[i+1][j+1] += dp[i][j];
          dp[i+1][j+1] %= 1000;
        }
      }
    }
    cout << "Case #" << cas << ": " << setfill('0') << setw(4) << dp[s.size()][t.size()] << endl;
  }

  return 0;
}
