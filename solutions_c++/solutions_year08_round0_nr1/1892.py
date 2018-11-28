
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <algorithm>

  using namespace std;

  #define maxS 105
  #define maxQ 1005
  #define maxlen 105

  int tst;
  int cur[maxS];
  int list[maxQ], next[maxQ];
  char a[maxS][maxlen];
  int S, Q;

  void init()
    {
       scanf("%d\n", &S);
       for (int k = 0; k < S; ++ k) gets(a[k]);
       scanf("%d\n", &Q);
       for (int k = 0; k < Q; ++ k)
         {
           char st[maxlen];
           gets(st);
           for (int i = 0; i < S; ++ i)
             if (!strcmp(st, a[i])) { list[k] = i; break; }
         }
    }

  void work()
    {
       for (int k = 0; k < S; ++ k) cur[k] = Q;
       for (int k = Q - 1; k >= 0; -- k)
         {
           next[k] = cur[list[k]];
           cur[list[k]] = k;
         }

       //for (int k = 0; k < S; ++ k) printf("%d %d\n", k, cur[k]);
       int now = -1, ret = 0;
       for (int i = 0; i < Q; ++ i)
         {
            if (now >= 0 && now != list[i]) continue;

            for (int k = 0; k < S; ++ k)
              while (cur[k] < i) cur[k] = next[cur[k]];

            int prev = now;
            now = -1;
            for (int k = 0; k < S; ++ k)
              if (now < 0 || cur[k] > cur[now]) now = k;

            //printf("%d\n", now);
            ++ ret;
            cur[prev] = next[cur[prev]];
         }
       if (Q == 0) ret = 0; else -- ret;
       printf("%d\n", ret);
    }

  int main()
    {
       int sp = 0;
       for (scanf("%d\n", &tst); tst; -- tst)
         {
            printf("Case #%d: ", ++ sp);
            init();
            work();
         }
       return 0;
    }
