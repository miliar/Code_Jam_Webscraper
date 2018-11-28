//
//

#include <stdio.h>
#include <math.h>

int main()
{
    int T;
    scanf("%d",&T);
    for (int i=0; i<T; i++) {
        printf("Case #%d:\n",i+1);
        double D,t,x,x1=0.0;
        double prev=0.0;
        int N,A,b=0;
        scanf("%lf",&D);
        scanf("%d%d",&N,&A);
        for (int j=0; j<N; j++) {
            scanf("%lf%lf",&t,&x);
            if (x<=D) {
                prev=t;
                x1=x;
            }
            else
            {
                if(!b)
                {
                    double v=(x-x1)/(t-prev);
                    double tmp=D-x1;
                    prev=prev+tmp/v;
                    b=1;

                }
            }
        }
        for (int j=0; j<A; j++) {
            double a;
            scanf("%lf",&a);
            double ans=sqrt(2.0*a*D)/a;
            if(prev>ans) ans=prev;
            printf("%f\n",ans);
        }
    }
    return 0;
}