#include <iostream>
#include <cstring>
#include <iomanip>

using namespace std;

char pattern[] = "welcome to code jam";
int dp[501][30];
char s[502];

int main ()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int n;
  cin >> n;
  cin.getline(s,501);
  cout.fill('0');
  for (int t = 1; t <= n; t++)
  {
    cout << "Case #" << t << ": ";
    cin.getline(s,501);
    dp[0][0] = 1;
    for (int i = 0; s[i] > 0; i++)
    {
      dp[i][0] = 1;
      for (int j = 0; pattern[j] > 0; j++)
      {
        dp[i+1][j+1] = dp[i][j+1];
        if (s[i] == pattern[j])
        {
          dp[i+1][j+1] += dp[i][j];
          dp[i+1][j+1] %= 10000;
        }
      }
    }
    cout << setw(4) << dp[strlen(s)][strlen(pattern)] << endl;
  }
  return 0;
}