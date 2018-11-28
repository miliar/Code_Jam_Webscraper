#include <cstdio>
#include <string>
#include <map>

#define m 1010
#define mm 110

using namespace std;

int n, s, q, a[m], r[m][mm];
char buf[999];

int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  scanf("%d", &n);
  for (int i = 0; i < n; i++)
  {
    printf("Case #%d: ", i + 1);
    scanf("%d", &s);
    map <string, int> na;
    gets(buf);
    for (int j = 0; j < s; j++)
    {
      gets(buf);
      na[buf] = j;
    }
    scanf("%d", &q);
    gets(buf);
    for (int j = 0; j < q; j++)
    {
      gets(buf);
      a[j] = na[buf];
    }
    for (int j = 0; j <= q; j++)
      for (int k = 0; k < s; k++)
        r[j][k] = j ? (int)1e9 : 0;
    for (int j = 0; j < q; j++)
      for (int k = 0; k < s; k++)
        for (int l = 0; l < s; l++)
          if (l != a[j])
            r[j + 1][l] = min(r[j + 1][l], r[j][k] + (l != k));
    int res = (int)1e9;
    for (int j = 0; j < s; j++)
      res = min(res, r[q][j]);
    printf("%d\n", res);
  }
  return 0;
}
