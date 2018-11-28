
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <algorithm>

  using namespace std;

  #define maxlen 2005

  const int dx[4] = {1, 0, -1, 0};
  const int dy[4] = {0, -1, 0, 1};

  struct node
    {
       int x, y;
    }P[maxlen];

  int len;
  int tot, N;
  char cmds[maxlen];
  int num[maxlen];

  void init()
    {
       scanf("%d", &len);
       char s[20];
       int tt;
       tot = 0;
       for (int k = 0; k < len; ++ k)
         {
            scanf("%s", &s);
            scanf("%d", &tt);
            for (int i = 0; i < tt; ++ i)
              for (int j = 0; j < strlen(s); ++ j)
                {
                  if (tot > 0 && cmds[tot - 1] == s[j]) ++ num[tot - 1]; else
                    {
                      cmds[tot] = s[j];
                      num[tot] = 1;
                      tot ++;
                    }
                }
         }

        int dr = 0;
        N = 1;
        P[0].x = 0, P[0].y = 0;
        for (int k = 0; k < tot; ++ k)
          {
             if (cmds[k] == 'F')
               {
                  P[N].x = P[N - 1].x + num[k] * dx[dr];
                  P[N].y = P[N - 1].y + num[k] * dy[dr];
                  ++ N;
               }
             if (cmds[k] == 'L')
               {
                  dr = (dr - num[k]) % 4;
                  if (dr < 0) dr += 4;
               }
             if (cmds[k] == 'R')
               {
                  dr = (dr + num[k]) % 4;
               }
          }
        -- N;
    }

  bool between(double x, double l, double r)
    {
       if (l > r) swap(l, r);
       return x >= l && x <= r;
    }

  bool check(int x, int y)
    {
       int east = 0, west = 0, north = 0, south = 0;

       for (int i = 0; i < N; ++ i)
         if (P[i].x == P[i + 1].x)
           {
             if (P[i].x < x + 0.5 && between(y + 0.5, P[i].y, P[i + 1].y)) ++ west;
             if (P[i].x > x + 0.5 && between(y + 0.5, P[i].y, P[i + 1].y)) ++ east;
           }
       if (west & 1) return 0;
       if (east & 1) return 0;
       if (west > 0 && east > 0) return 1;
     
       for (int i = 0; i < N; ++ i)
         if (P[i].y == P[i + 1].y)
           {
             if (P[i].y < y + 0.5 && between(x + 0.5, P[i].x, P[i + 1].x)) ++ north;
             if (P[i].y > y + 0.5 && between(x + 0.5, P[i].x, P[i + 1].x)) ++ south;
           }
       if (north & 1) return 0;
       if (south & 1) return 0;
       if (north > 0 && south > 0) return 1;  

       return 0;
    }

  void work()
    {
       int ret = 0;
       for (int i = -101; i <= 101; ++ i)
         for (int j = -101; j <= 101; ++ j)
           if (check(i, j)) ++ ret;
       printf("%d\n", ret);
    }

  int main()
    {
       freopen("A-small-attempt0.in", "r", stdin);
 
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
