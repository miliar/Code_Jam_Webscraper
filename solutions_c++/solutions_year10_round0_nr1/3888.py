#include<cstdio>
int main(){
    int bits[31]={0,1};
    int n,k,tcase,t;
    for(n=2;n<=30;++n){
        bits[n]=(bits[n-1]<<1)|1;
        //printf("%d %d\n",n, bits[n]);
    }
    scanf("%d",&tcase);
    for(t=1;t<=tcase;++t){
        scanf("%d%d",&n,&k);
        if((k&bits[n])==bits[n]){
            printf("Case #%d: ON\n",t);
        }else{
            printf("Case #%d: OFF\n",t);
        }
    }
    /*n=47;
    printf("asdf %d\n",n);
    printf("asdf %d\n",bits[4]);
    printf("asdf %d\n",n&bits[4]);
    n=bits[4];
    while(n){
        putchar('0'+(n&1));
        n=n>>1;
    }
    getchar();
    getchar();
    */
    return 0;
}
