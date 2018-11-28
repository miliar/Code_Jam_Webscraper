#include <cstdio>
#include <vector>
#include <algorithm>
#define MaxN 111

using namespace std;

char a[MaxN][MaxN];

bool placeTile(int x, int y)
{
   if (a[x  ][y  ] == '#') a[x  ][y  ] = '/'; else return false;
   if (a[x+1][y  ] == '#') a[x+1][y  ] = '\\'; else return false;
   if (a[x  ][y+1] == '#') a[x  ][y+1] = '\\'; else return false;
   if (a[x+1][y+1] == '#') a[x+1][y+1] = '/'; else return false;
   return true;
}

void solve()
{
   int n, m;
   memset(a, 0, sizeof(a));
   scanf("%d %d\n", &n, &m);
   for (int i=0; i<n; i++)
      scanf("%s", a[i]);
   bool ok = true;
   for (int i=0; i<n; i++)
      for (int j=0; j<m; j++)
         if (a[i][j] == '#')
            ok &= placeTile(i, j);
   if (!ok){
      printf("Impossible\n");
      return;
   }
   for (int i=0; i<n; i++)
      printf("%s\n", a[i]);
}

int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
   int tst;
   scanf("%d", &tst);
   for (int iter = 1; iter <= tst; iter++){
      printf("Case #%d:\n", iter);
      solve();
   }
   return 0;
}