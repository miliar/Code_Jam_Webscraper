#include <algorithm>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <iostream>

using namespace std;

#define maxn 2000

char s[maxn], a[maxn];
int p[maxn];

int main( void )
{
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int tn;
  cin >> tn;
  for (int tt = 1; tt <= tn; tt++)
  {
    printf("Case #%d: ", tt);
    int k;
    scanf("%d%s", &k, s);
    int n = strlen(s);
    
    for (int i = 0; i < k; i++)
      p[i] = i;
    int r = 1000000;
    do
    {
      for (int i = 0; i < n; i += k)
      {
        for (int j = 0; j < k; j++)
          a[i + j] = s[i + p[j]];
      }
      int res = 1;
      a[n] = 0;
      for (int i = 1; i < n; i++)
        res += a[i] != a[i - 1];
      r <?= res;

    }while (next_permutation(p, p + k));
    printf("%d\n", r);

  }



  return 0;
}