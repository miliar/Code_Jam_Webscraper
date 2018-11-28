// vim:set ts=8 sw=2 et:

#include <cstdio>
#include <algorithm>

const int maxd = 5000;
const int maxl = 15;

int l, d;
char dic[maxd][maxl + 1];
char input[28 * maxl + 1];
bool table[maxl][26];

int solve();
bool match(const char str[]);

int main()
{
  int n;
  scanf("%d%d%d", &l, &d, &n);
  for (int i = 0; i < d; ++i)
    scanf("%s", dic[i]);
  for (int tc = 1; tc <= n; ++tc)
  {
    scanf("%s", input);
    int ans = solve();
    printf("Case #%d: %d\n", tc, ans);
  }
}

int solve()
{
  const char *p = input;
  std::fill(table[0], table[l], false);
  for (int i = 0; i < l; ++i, ++p)
    if (*p == '(')
      for (++p; *p != ')'; ++p)
        table[i][*p - 'a'] = true;
    else
      table[i][*p - 'a'] = true;
  int ret = 0;
  for (int i = 0; i < d; ++i)
    if (match(dic[i]))
      ++ret;
  return ret;
}

bool match(const char str[])
{
  for (int i = 0; i < l; ++i)
    if (!table[i][str[i] - 'a'])
      return false;
  return true;
}
