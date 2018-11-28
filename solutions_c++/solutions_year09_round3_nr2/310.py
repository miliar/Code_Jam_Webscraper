#include <stdlib.h>
#include <math.h>
#include <stdio.h>

using namespace std;

int main () {
    int t,n,i,j;
    double r0,r1,r2,r3,r4,r5,m0,m1,m2,m3,m4,m5,a,b,c,dmin,tmin;
    freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    scanf ("%d",&t);
    for (i=1;i<=t;i++) {
        scanf ("%d",&n);
        m0 = 0; m1 = 0; m2 = 0; m3 = 0; m4 = 0; m5 = 0;
        for (j=1;j<=n;j++) {
            scanf ("%lf%lf%lf%lf%lf%lf",&r0,&r1,&r2,&r3,&r4,&r5);
            m0+=r0;
            m1+=r1;
            m2+=r2;
            m3+=r3;
            m4+=r4;
            m5+=r5;
        }
        m0 = m0/n;
        m1 = m1/n;
        m2 = m2/n;
        m3 = m3/n;
        m4 = m4/n;
        m5 = m5/n;
        //printf ("%lf %lf %lf %lf %lf %lf\n",m0,m1,m2,m3,m4,m5);
        printf ("Case #%d: ",i);
        a = m3*m3 + m4*m4 + m5*m5;
        b = 2*(m0*m3+m1*m4+m2*m5);
        c = m0*m0 + m1*m1 + m2*m2;
        //printf ("%.8lf %.8lf %.8lf\n",a,b,c);
        if (fabs(a) < 1e-9) a = 0;
        if (fabs(b) < 1e-9) b = 0;
        if (fabs(c) < 1e-9) c = 0;
        if (a>0) {
           if (b>0) tmin = 0; 
           else tmin = -b/(2*a);
        }
        else if (a==0) {
             if (b==0) tmin = 0;
             else tmin = -c/b;
        }  
        dmin = (a*tmin*tmin)+(b*tmin)+c;
        if (fabs(dmin) < 1e-5) dmin = 0;
        printf ("%.8lf %.8lf\n",sqrt(dmin),tmin);
    }
    return 0;
}
