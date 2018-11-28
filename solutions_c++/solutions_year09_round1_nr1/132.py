// vim:set ts=8 sw=2 et smarttab:

#include <cstdio>
#include <cstdlib>
#include <cstring>

const int limit1 = 12000000;
const int limit2 = 100000000;
char table[11][limit2 + 1];
int n;
int list[10];

char recur(int base, int a);
int solve();

int main()
{
  for (int base = 2; base <= 10; ++base)
  {
    table[base][0] = -1;
    table[base][1] = 1;
    for (int i = 2; i <= limit1; ++i)
      table[base][i] = recur(base, i);
  }
  int t;
  char line[1000];
  gets(line);
  sscanf(line, "%d", &t);
  for (int tc = 1; tc <= t; ++tc)
  {
    gets(line);
    const char del[] = " \n\r\t";
    n = 0;
    for (char *p = strtok(line, del); p != NULL; p = strtok(NULL, del))
      sscanf(p, "%d", &list[n++]);
    int ans = solve();
    printf("Case #%d: %d\n", tc, ans);
  }
}

char recur(int base, int a)
{
  if (a > limit2)
  {
    printf("limit2 exceeded a: %d, limit2: %d\n", a, limit2);
    exit(1);
  }
  if (table[base][a] != 0)
    return table[base][a];
  table[base][a] = -1;
  int ca = a;
  int sum = 0;
  while (ca > 0)
  {
    int digit = ca % base;
    ca /= base;
    sum += digit * digit;
  }
  return table[base][a] = recur(base, sum);
}

int solve()
{
  int a;
  for (a = 2; true; ++a)
  {
    if (a > limit1)
    {
      printf("limit1 exceeded a: %d, limit1: %d\n", a, limit1);
      exit(1);
    }
    for (int i = 0; i < n; ++i)
      if (table[list[i]][a] == -1)
        goto nexta;
    break;
nexta:
    ;
  }
  return a;
}
