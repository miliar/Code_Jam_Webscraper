#include <cstdio>
#include <cmath>
using namespace std;


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;t++)
    {
        int N;
        scanf("%d",&N);
        double s[N];
        double X=0.0;
        for (int i=0;i<N;i++) scanf("%lf",&s[i]),X+=s[i];
        printf("Case #%d:",t);
        for (int i=0;i<N;i++)
        {
            double L=0.0,R=1.0;
            while (R-L>1e-10)
            {
                  double mid=(L+R)*0.5;
                  double get=X*mid+s[i];
                  double rest=1.0-mid;
                  for (int j=0;j<N;j++)
                      if (j!=i)
                      {
                         if (s[j]<get)
                            rest-=(get-s[j])/X;
                      }
                  if (rest<0) R=mid;
                  else L=mid;
            }
            printf(" %.7f",R*100.0);
        }
        printf("\n");
    }
}
