#include<stdio.h>
#define Err 1e-9
struct Point{
    double x,y;
}boo[2][1024];
void fill(int No,int lx,int ly,int rx,int ry,int x){
    boo[No][x]=(Point){x,ly+(double)(ry-ly)*(x-lx)/(rx-lx)};
}
double Area(int x,double r){
    return r*(boo[0][x].y*2-boo[1][x].y*2+(boo[0][x+1].y-boo[0][x].y)*r-(boo[1][x+1].y-boo[1][x].y)*r)/2;
}
double Area(int x,double l,double r){
    return Area(x,r)-Area(x,l);
}
main(){
    int T,prob,rx,ry,lx,ly,W,L,U,G,i,j;
    double area,target;
    scanf("%d",&T);
    for(prob=1;prob<=T;prob++){
        scanf("%d%d%d%d",&W,&L,&U,&G);
        scanf("%d%d",&lx,&ly);
        for(i=1;i<L;i++){
            scanf("%d%d",&rx,&ry);
            for(j=lx;j<rx;j++){
                fill(1,lx,ly,rx,ry,j);
            }
            lx=rx;
            ly=ry;
        }
        boo[1][lx]=(Point){lx,ly};
        scanf("%d%d",&lx,&ly);
        for(i=1;i<U;i++){
            scanf("%d%d",&rx,&ry);
            for(j=lx;j<rx;j++){
                fill(0,lx,ly,rx,ry,j);
            }
            lx=rx;
            ly=ry;
        }
        boo[0][lx]=(Point){lx,ly};
        printf("Case #%d:\n",prob);
        area=0;
        for(i=0;i<W;i++){
            area+=(boo[0][i].y+boo[0][i+1].y-boo[1][i].y-boo[1][i+1].y)/2;
        }
        target=area/G;
        int now_int=0;
        double now_double=0;
        double now_area;
        for(i=1;i<G;i++){
            now_area=0;
            do{
                double tmp;
                if((tmp=now_area+Area(now_int,now_double,1))<=target){
                    now_area=tmp;
                    now_int++;
                    now_double=0;
                }
                else{
                    double left=now_double,right=1,mid;
                    while(left+Err<right){
                        mid=(left+right)/2;
                        if(now_area+Area(now_int,now_double,mid)<=target)left=mid;
                        else right=mid;
                    }
                    now_double=mid;
                    printf("%.8lf\n",now_int+mid);
                    break;
                }

            }while(1);
        }
    }
}
