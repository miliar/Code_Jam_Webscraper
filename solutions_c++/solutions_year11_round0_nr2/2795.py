#include <cstdio>

int N, T, t, C, D, i, d, j, k, L;
char SC[100][3], SD[100][2], W[105], X;

int main()
{
 freopen("test.in","r",stdin);
 freopen("test.out","w",stdout);
 
 scanf("%d", &T);
 for (t=1; t<=T; ++t)
     {
      scanf("%d ", &C);
      for (i=0; i<C; ++i)
           scanf("%s", &SC[i]);
      scanf("%d ", &D);
      for (i=0; i<D; ++i)
          scanf("%s", &SD[i]);
          
      scanf("%d ", &N);
      L = 1;
      for (i=0; i<N; ++i)
          {
           scanf("%c", &X);
           W[L++] = X;
           for (j=0; j<C; ++j)
               if ( (SC[j][0] == W[L-1] && SC[j][1] == W[L-2]) || (SC[j][1] == W[L-1] && SC[j][0] == W[L-2]) )
                  { --L, W[L-1] = SC[j][2]; break; }
           //check for opposed
           for (d=0; d<D; ++d)
               for (j=1; j<L; ++j)
                   for (k=j+1; k<L; ++k)
                       if ( (SD[d][0] == W[j] && SD[d][1] == W[k]) || (SD[d][1] == W[j] && SD[d][0] == W[k]) )
                          L = 1;
          }
      
      printf("Case #%d: [", t);
      for (i=1; i+1<L; ++i)
          printf("%c, ", W[i]);
      if (L>1) printf("%c", W[L-1]);
      printf("]\n");
     }
 
}
