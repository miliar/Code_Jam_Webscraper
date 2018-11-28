#include<iostream>
#include<cmath>
int x[1000],y[1000],r[1001];
double mn;
double mx(double a,double b){
    if(a>b){return a;}
    else{return b;}
}
double dist(int a,int b){
    return sqrt((double)((x[a]-x[b])*(x[a]-x[b])+(y[a]-y[b])*(y[a]-y[b])));
}
main(){
    int ti,tt,n,i;
    scanf("%d",&tt);
    for(ti=1;ti<=tt;ti++){
        scanf("%d",&n);
        for(i=0;i<n;i++){
            scanf("%d",&x[i]);
            scanf("%d",&y[i]);
            scanf("%d",&r[i]);
        }
        mn = 1000000;
        if(n==1){
            mn = r[0];
        }
        if(n==2){
            mn <?= mx(r[0],r[1]);
        }
        if(n==3){
            mn <?= mx((dist(0,1)+r[0]+r[1])/2,r[2]);
            mn <?= mx((dist(0,2)+r[0]+r[2])/2,r[1]);
            mn <?= mx((dist(1,2)+r[1]+r[2])/2,r[0]);
        }
        printf("Case #%d: %lf\n",ti,mn);
    }
}
