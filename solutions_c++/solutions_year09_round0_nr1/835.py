#include <cstdio>
#include <string>
#include <vector>
#include <iostream>

using namespace std;


vector <string> ok;

int can[20][26];

int main( void )
{
  int l, d, n;
  scanf("%d%d%d", &l, &d, &n);

  for (int i = 0; i < d; i++)
  {
    string s;
    cin >> s;
    ok.push_back(s);
  }

  int tn = n;

  for (int t = 1; t <= tn; t++)
  {
    printf("Case #%d: ", t);

    string s;
    cin >> s;
    memset(can, 0, sizeof(can));
    int p = 0, b = 0, x = 0;
    while (p < (int)s.size())
    {
      if (s[p] == '(')
        b = 1;
      else if (s[p] == ')')
        x++, b = 0;
      else
        can[x][s[p] - 'a'] = 1, x += !b;
      p++;
    }
    int res = 0;
    for (int i = 0; i < (int)ok.size(); i++)
    {
      int add = 1;
      for (int j = 0; j < l; j++)
        add &= can[j][ok[i][j] - 'a'];
      res += add;
    }

    printf("%d\n", res);
  }
  
  return 0;
}
