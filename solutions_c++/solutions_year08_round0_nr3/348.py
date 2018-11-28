#include <iostream>
#include <cmath>
using namespace std;
double PI = 2.*acos(0);
double getangle(double x, double y) {
    return atan2(y,x);
}
double getarea(double x, double y, double len, double r) {
    if (x*x+y*y>=r*r) return 0;
    double rx = sqrt(r*r-y*y);
    double ry = sqrt(r*r-x*x);
    double sx,sy;
    bool nox=false,noy=false;
    if (rx>x+len) {
        nox=true;
        sy=sqrt(r*r-(x+len)*(x+len));
    }
    if (ry>y+len) {
        noy=true;
        sx=sqrt(r*r-(y+len)*(y+len));        
    }
    
    double ret = 0;
    double angle;
    if (nox&&noy) {
        if (sx>=x+len) {return len*len;}
        ret=(sx-x)*len+(len-(sx-x))*(sy-y)+(len-(sx-x))*(len-(sy-y))/2;
        angle = getangle(sx,y+len)-getangle(x+len,sy);
    } else if (nox) {
        ret=len*(sy-y)+len*(ry-sy)/2;
        angle=getangle(x,ry)-getangle(x+len,sy);
    } else if (noy) {
        ret=len*(sx-x)+len*(rx-sx)/2;
        angle=getangle(sx,y+len)-getangle(rx,y);
    } else {
        ret=(ry-y)*(rx-x)/2;
        angle=getangle(x,ry)-getangle(rx,y);
    }
    double extra = 0.5*r*r*(angle-sin(angle));
//    printf("%f\n",ret+extra);
    return ret+extra;
}
int main() {
    int N; scanf("%d",&N);
    for (int cn=1; cn<=N; cn++) {
        double f,R,t,r,g;
        scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
        double area = 0;
        for (double x = r; x<R-t; x+=g+2*r)
        for (double y = r; y<R-t; y+=g+2*r) {
            double tmp = getarea(x+f,y+f,g-2*f,R-t-f);
            area+=tmp;
        }
        double fullarea = PI*R*R/4;
        double ans = (fullarea-area)/fullarea;
        printf("Case #%d: %f\n",cn,ans);
    }
    return 0;
}
