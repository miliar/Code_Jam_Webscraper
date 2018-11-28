// vim:set ts=8 sw=2 et:

#include <cstdio>
#include <cstring>
#include <algorithm>

int solve(const char input[]);

int main()
{
  char line[1000];
  gets(line);
  int t;
  sscanf(line, "%d", &t);
  for (int tc = 1; tc <= t; ++tc)
  {
    gets(line);
    int ans = solve(line);
    printf("Case #%d: %04d\n", tc, ans);
  }
}

int solve(const char input[])
{
  const char str[] = "welcome to code jam";
  const int m = sizeof(str) - 1;
  int n = strlen(input);
  int table[m];
  std::fill(table, table + m, 0);
  for (int i = 0; i < n; ++i)
    for (int j = m - 1; j >= 0; --j)
      if (input[i] == str[j])
        if (j > 0)
        {
          table[j] += table[j - 1];
          table[j] %= 10000;
        }
        else
        {
          table[j] += 1;
          table[j] %= 10000;
        }
  return table[m - 1];
}
