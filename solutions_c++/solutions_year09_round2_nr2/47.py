#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define pb push_back
#define mp make_pair

typedef vector <int> vi;

char s[99];
int f, d[10];

void gen( int i )
{
  if (f)
    return;
  if (!s[i])
    return;

  int t = s[i] - '0';
  if (d[t])
  {
    d[t]--;
    gen(i + 1);
    d[t]++;
  }
  for (int j = t + 1; j < 10; j++)
    if (d[j] && !f)
    {
      f = 1;
      forn(k, i)
        printf("%c", s[k]);
      printf("%d", j);
      d[j]--;
      forn(k, 10)
        while (d[k]--)
          printf("%d", k);
    }
}

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int tt = 1; tt <= tn; tt++)
  {
    scanf("%s", s);
    memset(d, 0, sizeof(d));
    for (int i = 0; s[i]; i++)
      d[s[i] - '0']++;
    f = 0;
    printf("Case #%d: ", tt);
    gen(0);
    if (!f)
    {
      int x = 1;
      d[0]++;
      while (!d[x])
        x++;
      printf("%d", x);
      d[x]--;
      forn(k, 10)
        while (d[k]--)
          printf("%d", k);
    }
    puts("");
  }
  return 0;
}
