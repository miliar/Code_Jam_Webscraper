#include <stdio.h>
#include <math.h>
#define max 3
int n;
double x[max],y[max],r[max];
void getInput(){
    scanf("%d",&n);
    for(int i=0;i<n;i++)
        scanf("%lf %lf %lf",&x[i],&y[i],&r[i]);

}
double dis(int i,int j){
    double dx=x[i]-x[j];
    double dy=y[i]-y[j];
    return sqrt(dx*dx+dy*dy);
}
double maxx(double a,double b){
    return a+b;
}
void run(){
    double d1,d2,d3,md;
    if(n==1)
        printf("%.6lf\n",r[0]);
    if(n==2)
        if(r[0]>r[1])printf("%.6lf\n",r[0]);
        else printf("%.6lf\n",r[1]);
    if(n==3){
        d1=dis(0,1)+maxx(r[0],r[1]);
        d2=dis(0,2)+maxx(r[0],r[2]);
        d3=dis(1,2)+maxx(r[1],r[2]);
        if(d1>d2){md=d2;}
        else {md=d1;}
        if(md>d3){md=d3;}
        printf("%.6lf\n",md/2);
    }

}
int main(){
    freopen("D-small-attempt0.in","rt",stdin);
    freopen("D-small-attempt0.out","wt",stdout);
    int ntest;
    scanf("%d",&ntest);
    for(int test=0;test<ntest;test++){
        getInput();
        printf("Case #%d: ",test+1);
        run();
    }
}
