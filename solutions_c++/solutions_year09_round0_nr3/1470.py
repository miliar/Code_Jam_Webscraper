#include <cstdio>
#include <cstring>

int N, n, i, j, L, LP, A[512][32];
char S[512];
char P[32] = "welcome to code jam";

int main()
{
 freopen("c.in","r",stdin);
 freopen("c.out","w",stdout);
 LP = 19;
 
 scanf("%d\n",&N);
 for (n=1; n<=N; ++n)
     {
      fgets(S, 512, stdin);
      L = strlen(S);
      if (S[L-1] == '\n') --L;
      
      memset(A, 0, sizeof(A));
      A[0][0] = (S[0] == P[0]);
      for (i=1; i<L; ++i)
          for (j=0; j<LP; ++j)
              {
               A[i][j] = A[i-1][j];
               if (S[i] == P[j])
                  if (j > 0) A[i][j] = (A[i][j] + A[i-1][j-1]) % 10000;
                     else A[i][j] = (A[i][j] + 1) % 10000;
              }              
      
      printf("Case #%d: %.4d\n", n, A[L-1][LP-1]);
     }

 return 0;
}
