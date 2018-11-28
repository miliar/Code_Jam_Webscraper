
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <algorithm>

  using namespace std;

  #define maxN 1005

  int Na, Nb, T;
  int Ans_a, Ans_b;
  int st[maxN], en[maxN];
  int visit[maxN];

  void Read(int &x)
    {
       char s[10];
       scanf("%s", &s);
       int p = (s[0] - '0') * 10 + s[1] - '0';
       int q = (s[3] - '0') * 10 + s[4] - '0';
       x = p * 60 + q;
    }

  void init()
    {
       scanf("%d", &T);
       scanf("%d %d", &Na, &Nb);
       for (int k = 0; k < Na + Nb; ++ k)
         {
           Read(st[k]), Read(en[k]);
         }
    }

  void work()
    {
       memset(visit, 0, sizeof(visit));
       Ans_a = 0, Ans_b = 0;
       for (int k = 0; k < Na + Nb; ++ k)
         {
            int j = -1;
            for (int i = 0; i < Na + Nb; ++ i)
              if (visit[i] != 2)
                if (j < 0 || st[i] < st[j]) j = i;

            if (visit[j] == 0)
               if (j < Na) ++ Ans_a; else ++ Ans_b;
            visit[j] = 2;

            if (j < Na)
              {
                 int best = -1;
                 for (int i = Na; i < Na + Nb; ++ i)
                   if (visit[i] == 0 && st[i] >= en[j] + T)             
                     if (best < 0 || st[i] < st[best]) best = i;
                 if (best >= 0) visit[best] = 1;
              } else
              {
                 int best = -1;
                 for (int i = 0; i < Na; ++ i)
                   if (visit[i] == 0 && st[i] >= en[j] + T)             
                     if (best < 0 || st[i] < st[best]) best = i;
                 if (best >= 0) visit[best] = 1;
              }
         }
        printf("%d %d\n", Ans_a, Ans_b);
    }

  int main()
    {
       int tst, op = 0;
       for (scanf("%d", &tst); tst; -- tst)
         {
            printf("Case #%d: ", ++ op);
            init();
            work();
         }
       return 0;
    }
