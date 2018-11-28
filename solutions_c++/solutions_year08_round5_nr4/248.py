
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <algorithm>

  using namespace std;

  #define maxR 105
  #define Mod  10007

  int H, W, tot;
  int f[maxR][maxR];
  bool yes[maxR][maxR];

  void init()
    {
       scanf("%d %d %d", &H, &W, &tot);
       memset(yes, 1, sizeof(yes));
       for (int k = 0; k < tot; ++ k)
         {
            int x, y;
            scanf("%d %d", &x, &y);
            yes[x][y] = 0;
         }
    }

  void work()
    {
       memset(f, 0, sizeof(f));
       f[1][1] = 1;
       for (int i = 1; i <= H; ++ i)
         for (int j = 1; j <= W; ++ j)
           if (yes[i][j])
             {
                if (i > 2 && j > 1) f[i][j] += f[i - 2][j - 1];
                if (i > 1 && j > 2) f[i][j] += f[i - 1][j - 2];
                f[i][j] %= Mod;
             }
       printf("%d\n", f[H][W]);
    }

  int main()
    {
       freopen("D-small-attempt0.in", "r", stdin);
       int caseNo;
       scanf("%d", &caseNo);
       for (int t = 1; t <= caseNo; ++ t)
         {
            printf("Case #%d: ", t);
            init();
            work();
         }
       return 0;
    }
