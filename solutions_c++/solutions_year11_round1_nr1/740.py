#include<stdio.h>
int gcd(int a,int b){
    if(a<b)
        return gcd(b,a);
    if(b==0)
        return a;
    return gcd(b,a-b);
}
int main(){
    int t,n,d,pd,pg;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%d%d%d",&n,&pd,&pg);
        printf("Case #%d: ",i);
        if((pg==100&&pd<100)||(pg==0&&pd>0))
            printf("Broken\n");
        else
            if(100/gcd(pd,100)<=n)
                printf("Possible\n");
            else
                printf("Broken\n");
    }
    return 0;
}
