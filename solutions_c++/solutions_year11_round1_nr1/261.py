#include<stdio.h>
#include<stdlib.h>

long long r[101];
long long d[101];
int gcd(int a,int b){
    if(b==0)return a;
    if(b>a)return gcd(b,a);
    return gcd(b,a%b);
}
void solve(int test){
    printf("Case #%d: ",test);
    long long n;
    int pd,pg;
    scanf("%lld %d %d",&n,&pd,&pg);
    if(n<d[pd]){
        printf("Broken\n");
        return;
    }
    long long A=r[pd],B=d[pd];
    long long C=r[pg],D=d[pg];
    //long long k1=1;
    if(C==0&&A!=0||pg==100&&pd<100)printf("Broken\n");
    else printf("Possible\n");
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    for(int i=0;i<=100;i++){
        int a=i,b=100;
        int k=gcd(a,b);
        //printf("%d %d %d %d\n",a,a/k,b/k,k);
        //a/=k;
        //b/=k;
        r[i]=(long long)(a/k);
        d[i]=(long long)(b/k);
    }
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        solve(i);
    }
}
