#include<iostream>
#include<math.h>
using namespace std;
int ii;
double x[1000],y[1000],r[1000];
int out(double x){
    printf("Case #%d: %.6f\n",ii,x);
    return(0);
}
double Max(double x,double y){
    if(x>y)return(x); else return(y);
}
double getdis(double x,double y){
    return(sqrt(x*x+y*y));
}
double doit(int i,int j){
    return((getdis(x[i]-x[j],y[i]-y[j])+r[i]+r[j])/2);
}
int main(){
    int n,i,j,tt;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>tt;
    for(ii=1;ii<=tt;ii++){
        cin>>n;
        for(i=1;i<=n;i++)
            cin>>x[i]>>y[i]>>r[i];
        if(n==1){
            out(r[1]);
        }else if(n==2){
            out(Max(r[1],r[2]));
        }else{
            double x1=Max(doit(1,2),r[3]);
            double x2=Max(doit(1,3),r[2]);
            double x3=Max(doit(2,3),r[1]);
            if(x1>x2)x1=x2;
            if(x1>x3)x1=x3;
            out(x1);
        }
    }
    return(0);
}

