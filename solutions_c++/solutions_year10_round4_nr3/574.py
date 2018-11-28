#include <iostream> 
using namespace std;

int a[2][111][111], n, c;

int main()
{   
    freopen("c1.in", "r", stdin);
    freopen("c.out", "w", stdout);
    
    scanf("%d", &c);
    for (int tt = 1; tt <= c; ++tt) {
        scanf("%d", &n); memset(a, 0, sizeof(a)); int tot = 0;
        for (int i = 0; i < n; ++i) {
            int x1, x2, y1, y2; scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            for (int x = x1; x <= x2; ++x)
                for (int y = y1; y <= y2; ++y)
                    if (!a[0][y][x]) {
                       a[0][y][x] = 1; ++tot;
                    }
        }
        int ans = 0, pre = 1, now = 0;
        while (tot) {
              ++ans; now = pre; pre = pre ^ 1;
              for (int x = 1; x <= 100; ++x)
                  for (int y = 1; y <= 100; ++y)
                      if (a[pre][x][y] == 1) {
                         if (a[pre][x - 1][y] == 0 && a[pre][x][y - 1] == 0)
                            a[now][x][y] = 0; else a[now][x][y] = 1;
                      }
                      else {
                           if (a[pre][x - 1][y] == 1 && a[pre][x][y - 1] == 1)
                              a[now][x][y] = 1; else a[now][x][y] = 0;
                      }
              tot = 0;
              for (int x = 1; x <= 100; ++x)
                  for (int y = 1; y <= 100; ++y)
                      tot += a[now][x][y];
        }
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}
