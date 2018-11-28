
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <algorithm>

  using namespace std;

  #define maxN 1005

  long long ret;
  int N;
  int a[maxN], b[maxN];

  int main()
    {
       freopen("A-small-attempt0.in", "r", stdin);
       freopen("A.out", "w", stdout);
         int tst, op = 0;
         for (scanf("%d", &tst); tst; -- tst)
           {
              scanf("%d", &N);
              for (int k = 0; k < N; ++ k) scanf("%d", &a[k]);
              sort(a, a + N);
              for (int k = 0; k < N; ++ k) scanf("%d", &b[k]);
              sort(b, b + N);
              long long ret = 0;
              for (int k = 0; k < N; ++ k) ret += a[k] * b[N - 1 - k];
              printf("Case #%d: %I64d\n", ++ op, ret);
           }
       return 0;
    }
