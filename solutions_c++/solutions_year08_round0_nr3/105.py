#include<cstdio>
#include<cmath>
#include<vector>
#include<iostream>
using namespace std;

#define PI 2*acos(0)


double brittochap(double r,double ja){
    double angle = asin((ja*0.5)/r);
    double ba = angle*r*r;
    double ta = 0.5*ja*sqrt(r*r-0.25*ja*ja);
    return ba-ta;
}


double Area(double x,double y,double side,double r){
    double x1 = x+side;
    double y1 = y+side;
    double d1 = x1*x1+y1*y1;
    if(d1<=r*r) return side*side;
    double d2 = x*x+y1*y1;
    double d3 = x1*x1+y*y;
    if(d2<=r*r){
        double x2 = sqrt(r*r-y1*y1);
        if(d3<=r*r){
            double y2 = sqrt(r*r-x1*x1);
            return side*(x2-x)+0.5*(side+y2-y)*(x1-x2)+brittochap(r,hypot(y1-y2,x1-x2));
        }
        else{
            double x3 = sqrt(r*r-y*y);
            return 0.5*(x3+x2-2*x)*side+brittochap(r,hypot(y1-y,x3-x2));
        }
    }
    else{
        double y2 = sqrt(r*r-x*x);
        if(d3<=r*r){
            double y3 = sqrt(r*r-x1*x1);
            return 0.5*(y2+y3-2*y)*side+brittochap(r,hypot(x1-x,y2-y3));
        }
        else{
            double x2 = sqrt(r*r-y*y);
            return 0.5*(y2-y)*(x2-x)+brittochap(r,hypot(x2-x,y2-y));

        }
    }

}


int main(){
    int N;
    double f,R,t,r,g;
    scanf("%d",&N);
    for(int cas=1;cas<=N;++cas){
        scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
        double res;
        double ir =R-t-f;
        if(ir<=r){
            res = 1.0;
        }
        else if(2*f>=g){
            res = 1.0;
        }
        else{
            double incr =g+2*r;
            double side = g-2*f;
            double x = r+f;
            double used = 0;
            while(true){
                double y = r+f;
                if(x*x+y*y>=ir*ir){
                    break;
                }
                while(true){
                    if(x*x+y*y>=ir*ir){
                        break;
                    }
                    used+=Area(x,y,side,ir);
                    y+=incr;
                }
                x+=incr;
            }
            double tot = 0.25*PI*R*R;
            res = (tot-used)/tot;
        }
        printf("Case #%d: %lf\n",cas,res);
    }
    return 0;
}
