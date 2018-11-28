#include<stdio.h>
#include<algorithm>
using namespace std;
struct data{
    int len,v;
    void scan(){
        int x,y;
        scanf("%d%d%d",&x,&y,&v);
        len=y-x;
    }
    bool operator<(data b)const{
        return v<b.v||(v==b.v&&len<b.len);
    }
}a[1024];
main(){
    int T,t=0,X,S,R,N,r,i;
    double sec,an,tmp;
    scanf("%d",&T);
    while(T--){
        an=0;
        t++;
        scanf("%d%d%d%lf%d",&X,&S,&R,&sec,&N);
        r=X;
        for(i=0;i<N;i++){
            a[i].scan();
            r-=a[i].len;
        }
        a[N]=(data){r,0};
        sort(a,a+N+1);
        for(i=0;i<=N;i++){
            if((tmp=(1.*a[i].len/(a[i].v+R)))<sec){
                sec-=tmp;
                an+=tmp;
            }
            else{
                an+=sec;
                an+=(a[i].len-sec*(a[i].v+R))/(a[i].v+S);
                sec=0;
            }
        }
        printf("Case #%d: %.9lf\n",t,an);
    }
}
