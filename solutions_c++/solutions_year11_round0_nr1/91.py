#include<stdio.h>
#include<stdlib.h>
int cas,n,b,o,inp,tim,bt,ot,net;
char str[5];
inline int abs(int a){
    return a>0?a:-a;
}
int main(){
    scanf("%d",&cas);
    for(int iii=0;iii<cas;iii++){
        scanf("%d",&n);
        b=1;
        o=1;
        tim=0;
        ot=0;
        bt=0;
        for(int i=0;i<n;i++){
            scanf("%s%d",str,&inp);
            if(str[0]=='B'){
                net=bt+abs(b-inp)+1;
                if(net>tim)tim=net;
                else tim++;
                bt=tim;
                b=inp;
            }else{
                net=ot+abs(o-inp)+1;
                if(net>tim)tim=net;
                else tim++;
                ot=tim;
                o=inp;
            }
        }
        printf("Case #%d: %d\n",iii+1,tim);
    }
    scanf(" ");
    return 0;
}
