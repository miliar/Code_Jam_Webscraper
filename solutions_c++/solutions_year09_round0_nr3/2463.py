#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{
  freopen("words.txt", "r", stdin);
  freopen("wordsOut.txt", "w", stdout);
  
  int tests;
  cin >> tests;

  cin.ignore();
  string const STR = "welcome to code jam";

  for (int test = 0; test < tests; ++test)
  {
    string str;
    getline(cin, str);

    vector<vector<int> > dp(str.size(), vector<int>(STR.size(), -1));
    int result = 0;

    for (int i = 0; i < str.size(); ++i)
    {      
      for (int j = 0; j <= i && j < STR.size(); ++j)
      {
        if (j > 0 && STR[j] == str[i]) {
          for (int k = 0; k < i; ++k)
            if (dp[k][j - 1] != -1)
            {
              if (dp[i][j] == -1)
                dp[i][j] = 0;
              dp[i][j] = (dp[i][j] + dp[k][j - 1]) % 10000;
            }
        }
        else
        {
          dp[i][j] = STR[j] == str[i] ? 1 : -1;
        }
      }

      if (dp[i][STR.size() - 1] != -1)
        result = (result + dp[i][STR.size() - 1]) % 10000;
    }

    cout << "Case #" << (test + 1) << ": " << setw(4) << setfill('0') << result << "\n";
  }

  return 0;
}