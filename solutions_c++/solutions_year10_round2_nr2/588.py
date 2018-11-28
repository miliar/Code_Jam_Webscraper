#include <stdio.h>
void solve(){
    int n,k,b,t,cnt=0, curn,ret=0;
    int x[51]={0},v[51]={0};
    double T[51]={0};
    scanf("%d%d%d%d",&n,&k,&b,&t);
    for(int i=0;i!=n;++i)scanf("%d",x+i);
    for(int i=0;i!=n;++i)scanf("%d",v+i);
    for(int i=0;i!=n;++i)if((T[i]=(b-x[i])/(double)v[i])<=t)++cnt;
    //for(int i=0;i!=n;++i)printf("%lf ",T[i]);puts("");
    if(cnt<k) puts("IMPOSSIBLE");
    else{
        cnt=0;
        curn=0;
        for(int i=n-1;i>=0 && cnt<k;--i){
            if(T[i]<=t) cnt++,ret+=curn;
            else{
                curn++;
            }
        }
        printf("%d\n",ret);
    }    
}
int main(){
    int cases;
    scanf("%d",&cases);
    for(int i=0;i!=cases;++i) {printf("Case #%d: ",i+1);solve();}
    return 0;
}
