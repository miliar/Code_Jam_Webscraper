
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <algorithm>

  using namespace std;

  #define maxN 2005

  int dr[maxN];
  bool like[maxN][maxN], yes[maxN];
  int malt[maxN], que[maxN];
  int N, M;

  void init()
    {
       scanf("%d", &N);
       scanf("%d", &M);

       for (int i = 1; i <= M; ++ i)
         for (int j = 1; j <= N; ++ j)
           like[i][j] = 0;

       for (int k = 1; k <= M; ++ k) malt[k] = 0;

       for (int k = 1; k <= M; ++ k)
         {
           int T, x, y;
           dr[k] = 0;
           for (scanf("%d", &T); T; -- T)
             {
                scanf("%d %d", &x, &y);
                if (y == 1) malt[k] = x; else
                  {
                     like[k][x] = 1;
                     ++ dr[k];
                  }
             }
         }
    }
 
  bool work()
    {
       memset(yes, 0, sizeof(yes));
       int h = 0, t = 0;
       for (int k = 1; k <= M; ++ k)
         if (dr[k] == 0)
           {
              if (malt[k] == 0) return 0;
              if (yes[malt[k]]) continue;
              que[++t] = malt[k];
              yes[malt[k]] = 1;
           }

       while (h < t)
         {
            int x = que[++h];
            for (int k = 1; k <= M; ++ k)
              if (like[k][x])
                {
                   like[k][x] = 0;
                   -- dr[k];
                   if (dr[k] > 0) continue;
                   if (malt[k] == 0) return 0;
                   if (yes[malt[k]]) continue;
                   que[++t] = malt[k];
                   yes[malt[k]] = 1;
                }
         }

       for (int k = 1; k <= N; ++ k)
         printf("%d%c", yes[k], (k == N ? '\n' : ' '));

       return 1;
    }

  int main()
    {
       freopen("B-large.in", "r", stdin);
       freopen("B.out", "w", stdout);
         int tst, op = 0;
         for (scanf("%d", &tst); tst; -- tst)
           {
             printf("Case #%d: ", ++ op);
             init();
             if (!work()) printf("IMPOSSIBLE\n");
           }
       return 0;
    }
