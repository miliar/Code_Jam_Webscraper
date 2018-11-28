#include <stdio.h>
#include <string.h>
#include <assert.h>

#define FIN "a-large.in"
#define FOUT "a.out"
#define INF 0x3f3f3f3f
#define MAX_S 100
#define MAX_LEN 128

char SE[MAX_S][MAX_LEN], SQ[MAX_LEN];
int B[2][MAX_S], M[MAX_S];

inline int minim(int a, int b)
{
       return a < b ? a : b;
}

int main(void)
{
    int tests, t;
    
    freopen(FIN, "r", stdin);
    freopen(FOUT, "w", stdout);
    
    scanf("%d", &tests);
    for (t = 1; t <= tests; t++)
    {
          int i, j, p, min, m = 0, a = 0, b = 1, S, Q;

          scanf("%d\n", &S);
          for (i = 0; i < S; i++)
              gets(SE[i]);
              
          memset(B, 0, sizeof(B));
          for (i = 0; i < S; i++)
              M[m++] = i;
          
          scanf("%d\n", &Q);
          for (; Q--; a = 1 - a, b = 1 - b)
          {
              gets(SQ);
              for (p = 0; p < S; p++)
                  if (!strcmp(SQ, SE[p]))
                     break;
              assert(p < S);
              
              for (i = 0; i < S; i++)
              {
                  int best = B[a][i];
                  for (j = 0; j < m; j++)
                      if (M[j] != i)
                         break;
                  if (j < m)
                     best = minim(best, B[a][M[j]] + 1);
                  B[b][i] = best;
              }
              
              min = B[b][p] = INF, m = 0;
              for (i = 0; i < S; i++)
                  if (B[b][i] < min)
                     min = B[b][i], M[0] = i, m = 1;
                  else
                  if (B[b][i] == min)
                     M[m++] = i;
          }
          
          printf("Case #%d: %d\n", t, B[a][M[0]]);
    }
    
    return 0;
}
