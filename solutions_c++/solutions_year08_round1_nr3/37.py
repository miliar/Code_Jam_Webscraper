
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <algorithm>

  using namespace std;

  #define Mod 1000

  int a[4], Res[4];
  int tst, N;

  void init()
    {
       scanf("%d", &N);
    }

  void multi(int *a, int *b, int *c)
    {
       int tmp[4];
       tmp[0] = (a[0] * b[0] + a[1] * b[2]) % Mod;
       tmp[1] = (a[0] * b[1] + a[1] * b[3]) % Mod;
       tmp[2] = (a[2] * b[0] + a[3] * b[2]) % Mod;
       tmp[3] = (a[2] * b[1] + a[3] * b[3]) % Mod;
       for (int k = 0; k < 4; ++ k) c[k] = tmp[k];
    }

  void Mul(int T)
    { 
       if (T == 0)
         {
           Res[0] = Res[3] = 1, Res[1] = Res[2] = 0;
           return;
         }
       Mul(T / 2);
       multi(Res, Res, Res);
       if (T & 1) multi(Res, a, Res);
    }

  void print(int x)
    {
       printf("%d%d%d\n", x / 100, x / 10 % 10, x % 10);
    }

  void work()
    {
       if (N == 1) { print(5); return; }
       if (N == 2) { print(27); return; }
       a[0] = 0, a[1] = 996, a[2] = 1, a[3] = 6;
       Mul(N - 2);
       int res = (6 * Res[1] + 28 * Res[3] - 1 + Mod) % Mod;
       print(res);
    }

  int main()
    {
       freopen("C-large.in", "r", stdin);
       freopen("C.out", "w", stdout);
         int tst, op = 0;
         for (scanf("%d", &tst); tst; -- tst)
           {
              printf("Case #%d: ", ++ op);
              init();
              work();
           }
       return 0;
    }


  

  