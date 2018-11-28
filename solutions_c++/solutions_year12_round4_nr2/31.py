#include<stdio.h>
#include<algorithm>
using namespace std;
#define SIZE 1000
struct circle{
    int r,No;
    bool operator<(const circle& b)const{return r>b.r;}
}c[SIZE];
int N,W,L,an[SIZE][2];
int main(){
    int T,cs=0,i;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d%d",&N,&W,&L);
        for(i=0;i<N;i++){
            scanf("%d",&c[i].r);
            c[i].No=i;
        }
        printf("Case #%d:",++cs);
        sort(c,c+N);
        int hh=0,now=0,next=0;
        an[c[0].No][0]=0;
        an[c[0].No][1]=0;
        now+=c[0].r;
        next=c[0].r;
        for(i=1;i<N;i++){
            if(now+c[i].r>W){
                hh=next+c[i].r;
                an[c[i].No][1]=hh;
                next=hh+c[i].r;
                now=0;
                an[c[i].No][0]=now;
                now+=c[i].r;
            }
            else{
                now+=c[i].r;
                an[c[i].No][1]=hh;
                an[c[i].No][0]=now;
                now+=c[i].r;
            }
        }
        //if(hh>L)fprintf(stderr,"haha!!\n");
        for(i=0;i<N;i++)printf(" %d %d",an[i][0],an[i][1]);
        puts("");
    }
    return 0;
}
