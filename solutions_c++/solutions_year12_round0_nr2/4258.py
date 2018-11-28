#include <cstdio>

int T,N,S,p,t;

int main(){
    scanf("%d",&T);
    for (int k=1;k<=T;++k){
        scanf("%d%d%d",&N,&S,&p);
        int ts=S,cnt=0;
        for (int i=0;i<N;++i){
            scanf("%d",&t);
            if (t-(p*3-2)>=0 || (p==1 && t>0))
                ++cnt;
            else if (ts && t>0 && t-(p*3-4)>=0){
                ++cnt;
                --ts;
            }
        }
        printf("Case #%d: %d\n",k,cnt);
    }
}
