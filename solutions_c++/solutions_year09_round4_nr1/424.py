#include <algorithm>
#include <cstdio>

using namespace std;

#define maxn 40

int n, mn[maxn];
char a[maxn][maxn];

int main()
{
  int testN;
  scanf("%d", &testN);
  for (int test = 1; test <= testN; test++)
  {
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
      mn[i] = 0;
      for (int j = 0; j < n; j++)
      {
        scanf(" %c", &a[i][j]), a[i][j] -= '0';
        if (a[i][j])
          mn[i] = j;
      }
    }
    int ans = 0;
    while (true)
    {
      int j = -1;
      for (int i = 0; i < n; i++)
        if (i < mn[i])
          j = i, i = n;
      if (j == -1)
        break;
      int k = j + 1;
      while (j < mn[k])
        k++;
      for (; k > j; k--)
      {
        ans++;
        swap(mn[k], mn[k - 1]);
      }
    }
    printf("Case #%d: %d\n", test, ans);
  }
  
  return 0;
}

