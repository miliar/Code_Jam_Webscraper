#include<stdio.h>
#include<stdlib.h>
int group[10000005][3],g[1005];
int use[1005][1005];
int next_pos(int n,int x){
    if(x == n-1)return 0;
    else return x+1;
}
int pre_pos(int n,int x){
    if(x == 0)return n-1;
    else return x-1;
}
int main(){
    int i,j,N,R,K,x,tmp,T,ca,start,end,m,q;
    int cycle_s,cycle_e,flag,ans,now;
    scanf("%d",&T);
    for(ca=1;ca<=T;ca++){

        scanf("%d%d%d",&R,&K,&N);
        for(i=0;i<N;i++){
            scanf("%d",&g[i]);
        }
        tmp = 0; ans = 0;now = N-1;
        for(i=0;i<R;i++){
            start = now;
            while(tmp + g[next_pos(N,now)] <= K){
                tmp += g[next_pos(N,now)];
                now = next_pos(N,now);
                if(start == now) break;
            }
            ans += tmp;
            tmp = 0;
        }
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}

