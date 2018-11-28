#include <stdio.h>

int main(){
    int n,m,i,j,o,b,s,t,tx,os,bs;char r;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        o=b=1;os=bs=s=0;
        scanf("%d",&m);
        for(j=0;j<m;j++){
            scanf(" %c %d",&r,&tx);
            if(r=='O'){
                t=tx-o;
                t=t<0?-t:t;
                t=t-(s-os);
                t=t<0?0:t;
                s+=t;
                o=tx;
                s++;
                os=s;
            }else{
                t=tx-b;
                t=t<0?-t:t;
                t=t-(s-bs);
                t=t<0?0:t;
                s+=t;
                b=tx;
                s++;
                bs=s;
            }
        //printf("#%d\n",s);
        }
        printf("Case #%d: %d\n",i+1,s);
    }//while(1);
    return 0;
}
