#include<stdio.h>
#include<string.h>
int main(){
        int T;
        scanf("%d",&T);
        int N,K;
        for(int t=1;t<=T;++t){
                scanf("%d%d",&N,&K);
                K=(K&((1<<N)-1));
                int tag=0;
                //printf("%d\n",K);
                for(int i=0;i<N;++i)
                        if((K&(1<<i))==0)tag=1;
                printf("Case #%d: ",t);
                printf("%s\n",tag?"OFF":"ON");
        }
        return 0;
}
