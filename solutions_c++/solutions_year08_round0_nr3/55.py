#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define PI acos(-1.0)
#define eps 1e-11

struct point{
    double x,y;
};

double calc(double a,double r){
       return sqrt(r*r-a*a);
}

bool in(point a,double r){
     if((a.x*a.x+a.y*a.y)<(r*r))return true;
     else return false;     
}
double dist(point a,point b){
       return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}
double hu(double L,double R){
       double a=L/2;
       double b=calc(a,R);
       return (2*asin(a/R))*R*R/2-a*b;
}

double tri(point a,point b,point c){
       return fabs((a.x-b.x)*(a.y-c.y)-(a.y-b.y)*(a.x-c.x))/2;
}

double insert(double R,double x,double y,double g){
       point LD,LU,RD,RU;
       LD.x=x;LD.y=y;
       LU.x=x;LU.y=y+g;
       RD.x=x+g;RD.y=y;
       RU.x=x+g;RU.y=y+g;
       //正方形在原的左上方
       point a,b;
       double res=0; 
       int k=-1;
       if(in(LD,R)&&in(RD,R)&&in(LU,R)&&in(RU,R))res=g*g;
       else if(in(LD,R)&&in(RD,R)&&in(LU,R)&&(!in(RU,R))){
            a.x=x+g;
            a.y=calc(x+g,R);
            b.x=calc(y+g,R);
            b.y=y+g;
            res+=tri(LD,RD,LU);
            res+=tri(RD,LU,a);
            res+=tri(LU,a,b);
            res+=hu(dist(a,b),R);
            k=1;
       }
       else if(in(LD,R)&&(!in(RD,R))&&in(LU,R)&&(!in(RU,R))){
            a.x=calc(y,R);
            a.y=y;
            b.x=calc(y+g,R);
            b.y=y+g;
            res+=tri(LD,a,LU);;
            res+=tri(LU,a,b);
            res+=hu(dist(a,b),R);
       }
       else if(in(LD,R)&&in(RD,R)&&(!in(LU,R))&&(!in(RU,R))){
            a.x=x;
            a.y=calc(x,R);
            b.x=x+g;
            b.y=calc(x+g,R);
            res+=tri(LD,a,RD);;
            res+=tri(RD,a,b);
            res+=hu(dist(a,b),R);
       }
       else if(in(LD,R)&&(!in(RD,R))&&(!in(LU,R))&&(!in(RU,R))){
            a.x=x;
            a.y=calc(x,R);
            b.x=calc(y,R);
            b.y=y;
            res+=tri(LD,a,b);
            res+=hu(dist(a,b),R);
       }
       else if((!in(LD,R))&&(!in(RD,R))&&(!in(LU,R))&&(!in(RU,R)))res=0;
       return res;
}

double area(double R,double r,double g){
       double res=0;
       for(double i=r;i<=R;i+=(g+2*r))
          for(double j=r;(i*i+j*j)<=R*R;j+=(g+2*r)){
             res+=4*insert(R,i,j,g);
          }
       return res;
}

int main(){
    //freopen("c-small.in","r",stdin);
    //freopen("c-small.out","w",stdout);
    //freopen("c-large.in","r",stdin);
    //freopen("c-large.out","w",stdout);
    int cases;
    scanf("%d",&cases);
    for(int i=1;i<=cases;i++){
        double f,R,t,r,g;
        scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
        printf("Case #%d: ",i);
        if((2*f)>=g||(t+f)>=R)printf("1.000000\n");
        else {
            printf("%.6lf\n",1-area(R-t-f,r+f,g-2*f)/(PI*R*R));
        }
    }
    return 0;   
}
