#include <algorithm>
#include <cstdio>
#include <map>
#include <string>

using namespace std;

#define maxl 110
#define maxn 110
#define maxm 1010

char temp[maxl];
int n, m, a[maxm], d[maxm][maxn];
map <string, int> se;

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int test = 1; test <= tn; test++)
  {
    scanf("%d ", &n);
    for (int i = 0; i < n; i++)
    {
      gets(temp);
      se[temp] = i;
    }
    scanf("%d ", &m);
    for (int i = 0; i < m; i++)
    {
      gets(temp);
      a[i] = se[temp];
    }
    memset(d, 0x7f, sizeof(d));
    for (int i = 0; i < n; i++)
      d[0][i] = 0;
    for (int i = 0; i < m; i++)
      for (int j = 0; j < n; j++)
        for (int k = 0; k < n; k++)
          if (a[i] != k)
            d[i + 1][k] = min(d[i + 1][k], d[i][j] + (k == j ? 0 : 1));
    int ans = 1 << 30;
    for (int i = 0; i < n; i++)
      ans = min(ans, d[m][i]);
    printf("Case #%d: %d\n", test, ans);
  }
  return 0;
}
