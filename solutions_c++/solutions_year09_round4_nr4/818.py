#include<string>
#include<cmath>
#include<algorithm>
int T;
int N;
int x[4], y[4], r[4];
double max(double a, double b){return a>b?a:b;}
double min(double a, double b){return a>b?b:a;}
int main()
{
  scanf("%d", &T);
  for(int c = 1;c<=T;c++)
  {
      scanf("%d", &N);
      for(int i=0;i<N;i++)
      scanf("%d%d%d", x+i, y+i, r+i);
      double ans = 0.0;
      if(N==1)ans = r[0];
      if(N==2)ans = max(1.*r[0], 1.*r[1]);
      if(N==3)
      {
          ans = 10000;
          for(int i=0;i<N;i++)
            for(int j=i+1;j<N;j++){
                double d = sqrt( (y[j]-y[i])*(y[j]-y[i]) +(x[j]-x[i])*(x[j]-x[i]) +0.0);
                double rr = (d+r[i]+r[j])/2.;
             ans = min( rr, ans);
            }
           ans = max(ans, 1.*r[0]);
           ans = max(ans, 1.*r[1]);
           ans = max(ans, 1.*r[2]);
      }

      printf("Case #%d: %.6lf\n", c, ans);
  }
}
