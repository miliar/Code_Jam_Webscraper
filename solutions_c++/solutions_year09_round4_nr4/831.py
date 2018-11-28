using namespace std;

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>

inline int min(int a,int b) { return a<b?a:b; }
inline int max(int a,int b) { return a>b?a:b; }
int cmp(const int &a, const int &b) { return a<b; }

inline double sqr(double a) { return a*a; }
inline double modul ( double a) { return a>0?a:-a; }


int C, c, N, i, j, k, c1, c2, cb1, cb2, O[100];
double X[100], Y[100], R[100], d, dx, dy, d1, d2, px1, px2, py1, py2, xx, yy, rr, rb, xb, yb;

int main()
{
 freopen("d.in","r",stdin);
 freopen("d.out","w",stdout);
 
 scanf("%d",&C);
 for (c=1; c<=C; ++c)
     {
      scanf("%d",&N);
      for (i=1; i<=N; ++i)
          {
           scanf("%lf %lf %lf",&X[i], &Y[i], &R[i]);
           O[i] = i;
          }
      for (i=1; i<N-1; ++i)
          {
           rb=100000;
           for (j=1; j<=N; ++j)
               for (k=j+1; k<=N; ++k)
                if (O[j] != O[k])
                   {
                    c1=O[j];
                    c2=O[k];
                    d = sqrt( sqr(X[c1]-X[c2]) + sqr(Y[c1]-Y[c2]) );
                    dx = modul(X[c1]-X[c2]);
                    dy = modul(Y[c1]-Y[c2]);
                    
                    d2 = dx * (d+R[c2]) / d;
                    d1 = dx * (d+R[c1]) / d;
                    px1 = X[c1]+d2;
                    px2 = X[c2]-d1;
                    
                    d2 = dy * (d+R[c2]) / d;
                    d1 = dy * (d+R[c1]) / d;
                    py1 = Y[c1]+d2;
                    py2 = Y[c2]-d1;
                    
                    xx = (px1+px2)/2;
                    yy = (py1+py2)/2;
                    rr = (d+R[c1]+R[c2])/2;                    
                    //d = sqrt( sqr(px1-px2) + sqr(py1-py2) );
                    //rr = d/2;                    
                    
                    if (rr<rb)
                       {
                        rb = rr;
                        xb = xx;
                        yb = yy;
                        cb1=O[j];
                        cb2=O[k];
                       }
                   }
           X[cb1] = xb;
           Y[cb1] = yb;
           R[cb1] = rb;
           //printf("%d %d %lf %lf %lf\n",cb1,cb2,rb, xb, yb);
           for (j=1; j<=N; ++j)
               if (O[j]==cb2) O[j]=cb1;               
          }
      rb = 0;
      for (i=1; i<=N; ++i)
          if (R[O[i]] > rb) rb=R[O[i]];
      printf("Case #%d: %.6lf\n",c,rb);
     }
 
 return 0;
}
