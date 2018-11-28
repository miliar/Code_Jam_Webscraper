#include <cstdio>

#define Nmax 128

int T, t, N, i, j, r;
int w[Nmax], p[Nmax];
double op[Nmax], oop[Nmax];
char S[Nmax][Nmax];

void getWP()
{
 for (i=0; i<N; ++i)
     {
      w[i] = p[i] = 0;
      for (j=0; j<N; ++j)
          if (S[i][j] == '1') ++p[i], ++w[i];
             else if (S[i][j] == '0') ++p[i];
      
     }
}

void getOWP()
{
 for (i=0; i<N; ++i)
     {
      r = 0;
      op[i] = 0.0;
      for (j=0; j<N; ++j)
          if (S[i][j] != '.') {
                      ++r;
             if (S[j][i] == '0') op[i] += (double) w[j] / (p[j]-1);
                else op[i] += (double) (w[j]-1) / (p[j]-1);
                }
      op[i] = op[i] / r;
     }
}

void getOOWP()
{
 for (i=0; i<N; ++i)
     {
      r = 0;
      oop[i] = 0.0;
     for (j=0; j<N; ++j)
         if (S[i][j] != '.') { ++r; oop[i] += op[j]; }
     oop[i] = oop[i] / r;
     }
}

int main()
{
 freopen("a.in","r",stdin);
 freopen("a.out","w",stdout);
 
 scanf("%d", &T);
 for (t=1; t<=T; ++t)
     {
      scanf("%d\n", &N);
      for (i=0; i<N; ++i)
          fgets(S[i], 128, stdin);
          
      getWP();
      getOWP();
      getOOWP();
      
      printf("Case #%d:\n", t);
      for (i=0; i<N; ++i)
          printf("%.10lf\n", 0.25 * w[i]/p[i] + 0.50 * op[i] + 0.25 * oop[i]);
     }
 
 return 0;
}
