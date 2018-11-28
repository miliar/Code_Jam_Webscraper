
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <algorithm>

  using namespace std;

  #define maxR 11

  bool map[maxR][maxR];
  int f[maxR][maxR][1 << maxR][2];
  int M, N;
  int ret;

  void init()
    {
       scanf("%d %d", &M, &N);
       for (int i = 0; i < M; ++ i)
         for (int j = 0; j < N; ++ j)
           {
              char c;
              while (c = getchar(), c != '.' && c != 'x');
              map[i][j] = c == '.';
           }
    }

  void updata(int &x, int y)
    {
       if (y > ret) ret = y;
       if (y > x) x = y;
    }

  int get(int x, int y)
    {
       if (x & (1 << y)) return 1; else return 0;
    }

  int make(int x, int y, int p)
    {
       if (x & (1 << y)) x -= 1 << y;
       x += (1 << y) * p;
       return x;
    }

  void work()
    {
       memset(f, 255, sizeof(f));
       f[0][0][0][0] = 0;
       
       ret = 0;
       int S = 1 << N;
       for (int i = 0; i < M; ++ i)
         for (int j = 0; j < N; ++ j)
           for (int k = 0; k < S; ++ k)
             for (int op = 0; op < 2; ++ op)
               {
                  if (f[i][j][k][op] < 0) continue;

                  int nxt[2];
                  if (j == N - 1) 
                    {
                      nxt[0] = i + 1, nxt[1] = 0;
                    } else
                    {
                      nxt[0] = i, nxt[1] = j + 1;
                    }
  
                  updata(f[nxt[0]][nxt[1]][make(k, j, 0)][get(k, j)], f[i][j][k][op]);

                  if (!map[i][j]) continue;
                  if (i > 0 && j > 0 && op > 0) continue;
                  if (j > 0 && (get(k, j - 1) > 0)) continue;
                  if (i > 0 && j < N - 1 && (get(k, j + 1) > 0)) continue;
 
                  updata(f[nxt[0]][nxt[1]][make(k, j, 1)][get(k, j)], f[i][j][k][op] + 1);
               }

        printf("%d\n", ret);
    }

  int main()
    {
       freopen("C-small-attempt0.in", "r", stdin);
 
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
