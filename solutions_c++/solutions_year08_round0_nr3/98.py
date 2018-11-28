#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;

double triangle_area(double x1, double y1, double x2, double y2, double x3, double y3){
    return (x3*y1-x2*y1+x1*y2-x3*y2-x1*y3+x2*y3)/2.0;
}

double tembereng(double px, double py, double qx, double qy, double rad){
    double pizza = fabs(atan2(py,px)-atan2(qy,qx)) * rad * rad / 2.0;
    double tria = fabs(triangle_area(px,py,qx,qy,0,0));
    return pizza-tria;
}

double calc(double ki, double ka, double ba, double at, double rad){
    // all out
    if (ki*ki+ba*ba>=rad*rad) return 0;
        
    double lebar = ka-ki;
    if (lebar<=0) return 0;
    
    // all in
    if (ka*ka+at*at<=rad*rad) return lebar*lebar;   
    
    if (ki*ki+at*at<=rad*rad){
        if (ka*ka+ba*ba<=rad*rad){
            // three nodes
            double hpoint = sqrt(rad*rad-at*at);
            double vpoint = sqrt(rad*rad-ka*ka);

            double segitiga = (ka-hpoint)*(at-vpoint)/2.0;
            return lebar*lebar - segitiga + tembereng(hpoint,at, ka,vpoint, rad);
        } else {
            // | two nodes 
            double hpoint = sqrt(rad*rad-ba*ba);           
            double hpoint2 = sqrt(rad*rad-at*at);     
            return (hpoint-ki+hpoint2-ki)/2.0*lebar + tembereng(hpoint2,at, hpoint,ba, rad);
        }
    } else {
        double vpoint = sqrt(rad*rad-ki*ki);
        if (ka*ka+ba*ba<=rad*rad){
            // -- two nodes
            double vpoint2 = sqrt(rad*rad-ka*ka);
            return (vpoint-ba+vpoint2-ba)/2.0*lebar + tembereng(ki,vpoint,ka,vpoint2,rad);
        } else {
            double hpoint = sqrt(rad*rad-ba*ba);
            // one node
            return (hpoint-ki)*(vpoint-ba)/2.0 + tembereng(ki,vpoint,hpoint,ba,rad);
        }        
    }
}

int main(){
    double PI = 2*acos(0);
    
    int ntc,ttc=0;
    scanf("%d", &ntc);
    while (ntc--){
        double f,R,t,r,g;
        scanf("%lf%lf%lf%lf%lf", &f,&R,&t,&r,&g);
        
        double area = PI*R*R;
        double inner = R-t-f;
        
        if (inner<=0){
            printf("Case #%d: 1.000000lf\n", ++ttc);
        } else {            
            double openarea = 0;
            for (double ki=r+f;ki<inner;ki+=g+r+r)
            for (double ba=r+f;ba<inner;ba+=g+r+r)
            {
                openarea+=calc(ki,ki+g-f-f,ba,ba+g-f-f,inner);
            }
            openarea*=4;
            double closearea = area-openarea;
            
            printf("Case #%d: %.6lf\n", ++ttc, closearea/area);
        }
    }    
    
    return 0;
}
