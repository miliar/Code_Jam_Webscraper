#include <cstdio>
#include <sstream>
#include <string>
#include <iostream>

using namespace std;

char s[100010];

int dp[600][50];

int get( string a, string b )
{
  int an = a.size(), bn = b.size();
  memset(dp, 0, sizeof(dp));
  dp[0][0] = 1;
  for (int i = 0; i <= an; i++)
    for (int j = 0; j <= bn; j++)
      if (j)
      {
        int t = i;
        while (t--)
          if (a[t] == b[j - 1])
            dp[i][j] = (dp[i][j] + dp[t][j - 1]) % 10000;
      }
      else if (i)
        dp[i][j] = dp[i - 1][j];
  return dp[an][bn];
}

int main( void )
{
  int tn;
  scanf("%d", &tn);
  while (getc(stdin) != '\n');

  for (int t = 1; t <= tn; t++)
  {
    printf("Case #%d: ", t);
    gets(s);
    string b = "welcome to code jam";
    printf("%04d\n", get(s, b));
  }

  return 0;
}