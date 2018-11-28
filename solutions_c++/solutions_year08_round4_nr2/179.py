#include <cstdio>
#include <cstring>
#include <cmath>

int C,cc;
int N,M,A,g,rez;
int x1,yy1,x2,y2;

int main()
{
 freopen("b.in","r",stdin);
 freopen("b.out","w",stdout);
 scanf("%d",&C);
 for (cc=1; cc<=C; ++cc)
     {
      scanf("%d %d %d",&N,&M,&A);
      g=0;
      for (x1=0; x1<=N && g==0; ++x1)
          for (y2=0; y2<=M && g==0; ++y2)
              {
               rez= x1*y2 - A;
               if (rez==0)
               {
                 g=1;
                 x2=0;
                 yy1=0;
                 continue;
                }
               if (rez<0) continue;
               if (N<M)
               {
               for (x2=1; x2<=sqrt(rez) && x2<=N; ++x2)
                   if ( rez % x2 == 0 && rez/x2<=M)
                      {
                        g=1;
                       yy1 = rez / x2;
                       break;
                      }
               }
               else
               {
               for (yy1=1; yy1<=sqrt(rez) && yy1<=M; ++yy1)
                   if ( rez % yy1 == 0 && rez/yy1<=N)
                      {
                        g=1;
                       x2 = rez / yy1;
                       break;
                      }
               }
              }
      if (g)
          printf("Case #%d: %d %d %d %d %d %d\n",cc,0,0,x1-1,yy1,x2,y2-1);
                       else printf("Case #%d: IMPOSSIBLE\n",cc);
/*      g=0;
      for (x1=0;x1<=N && !g;++x1)
        for (x2=0;x2<=N && !g;++x2)
                for (yy1=0;yy1<=M && !g;++yy1)
                        for (y2=0;y2<=M && !g;++y2)
                                if (x1*y2-x2*yy1==A)
                                        {
                                         g=1;
                                         printf("Case #%d: %d %d %d %d %d %d\n",cc,0,0,x1,yy1,x2,y2);
                                        }
                                
      if (!g) printf("Case #%d: IMPOSSIBLE\n",cc);*/
     }    
 return 0;
}
