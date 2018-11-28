#include<stdio.h>
int abs(int x){return x<0?-x:x;}
main(){
    freopen("Ab.in","r",stdin);
    freopen("Ab.out","w",stdout);
    int T,n,t=0,O,B,x,step,Ot,Bt,now_t,i;
    char s[8],c;
    scanf("%d",&T);
    while(T--){
        t++;
        scanf("%d",&n);
        O=B=1;
        Ot=Bt=now_t=0;
        for(i=1;i<=n;i++){
            scanf("%s%d",s,&x);
            if(s[0]=='O'){
                if(Ot+abs(O-x)+1<=now_t){
                    now_t++;
                    Ot=now_t;
                    O=x;
                }
                else{
                    now_t=Ot+abs(O-x)+1;
                    Ot=now_t;
                    O=x;
                }
            }
            else{
                if(Bt+abs(B-x)+1<=now_t){
                    now_t++;
                    Bt=now_t;
                    B=x;
                }
                else{
                    now_t=Bt+abs(B-x)+1;
                    Bt=now_t;
                    B=x;
                }

            }
        }
        printf("Case #%d: %d\n",t,now_t);
    }
}
