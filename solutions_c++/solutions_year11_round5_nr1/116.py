#include <math.h>
#include <stdio.h>
#include <string.h>

#define maxn 128

int L,U,G,W;
int lx[maxn],ly[maxn];
int ux[maxn],uy[maxn];

double area(double X){
    int i;
    double r=0;
    double tx,ty;
    double y2;
    tx=ux[0]; ty=uy[0];
    for (i=0;i<L;i++){
        //printf("%lf %lf -> ",tx,ty);
        if (X<lx[i]){
            y2=ly[i-1]+1.0*(ly[i]-ly[i-1])*(X-lx[i-1])/(lx[i]-lx[i-1]);
            r+=tx*y2-X*ty;
            tx=X; ty=y2;
            break;
        }else{
            r+=tx*ly[i]-ty*lx[i];
            tx=lx[i]; ty=ly[i];
        }
    }
    for (i=0;i<U;i++){
        if (X<ux[i]){
          //  printf("----- %lf %lf -> ",tx,ty);
            y2=uy[i-1]+1.0*(uy[i]-uy[i-1])*(X-ux[i-1])/(ux[i]-ux[i-1]);
            r+=tx*y2-X*ty;
            tx=X; ty=y2;
            i--;break;
        }
    }
    for (;i>=0;i--){
       // printf("%lf %lf -> ",tx,ty);
        r+=tx*uy[i]-ty*ux[i];
        tx=ux[i]; ty=uy[i];
    }
    return fabs(r/2);
}

double allarea(){
    int i;
    double r=0;
    double tx,ty;
    tx=ux[0]; ty=uy[0];
    for (i=0;i<L;i++){
        r+=tx*ly[i]-ty*lx[i];
        tx=lx[i]; ty=ly[i];
    }
    for (i=U-1;i>=0;i--){
        r+=tx*uy[i]-ty*ux[i];
        tx=ux[i]; ty=uy[i];
    }
    return fabs(r/2);
}

double darea(double t){
    double low,high,mid,tar;
    low=0; high=W*1.0;
    while (low+1e-9<high){
        mid = (low+high)/2;
        tar=area(mid);
        if (tar<t) low=mid;
        else high=mid;
    }
    return low;
}

void sol(int cas){
    int i,j;
    double tot,z,rx;
    scanf("%d%d%d%d",&W,&L,&U,&G);
    for (i=0;i<L;i++) scanf("%d%d",lx+i,ly+i);
    for (i=0;i<U;i++) scanf("%d%d",ux+i,uy+i);
    tot=allarea();
    z = tot/G;
    printf("Case #%d:\n",cas);
    for (i=1;i<G;i++){
        rx = darea(z*i);
        printf("%.10lf\n",rx);
    }
}

int main(){
    int t,cas;
    scanf("%d",&t);
    for (cas=1;cas<=t;cas++) sol(cas);
    return 0;
}

