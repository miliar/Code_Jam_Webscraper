#include <cstdio>

int T, t, N, i, k, R, S, S2, S3, j;
int C[20];

int main()
{
 freopen("test.in","r",stdin);
 freopen("test.out","w",stdout);
 
 scanf("%d", &T);
 for (t=1; t<=T; ++t)
     {
      scanf("%d", &N);
      S = 0;
      for (i=0; i<N; ++i)
          {
           scanf("%d", &C[i]);
           S ^= C[i];
          }
      
      R = 1000000000;
      for (i=1; i+1<(1<<N); ++i)
          {
           S2 = S3 = 0;           
           for (j=0; j<N; ++j)
               if (i & (1<<j)) S2 ^= C[j], S3 += C[j];
           if ((S2^S) == S2 && S3 < R) R = S3;
          }
      R = -R;
      for (i=0; i<N; ++i)
          R += C[i];
      if (R>0) printf("Case #%d: %d\n", t, R);
         else printf("Case #%d: NO\n", t);
     }
 
 return 0;
}
