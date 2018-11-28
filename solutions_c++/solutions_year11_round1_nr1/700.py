#include <stdio.h>
#include <iostream>
using namespace std;

int t;
long long n,pd,pg;

long long gcd(long long a,long long b){
    long long r;
    while(b){
        r=a%b;
        a=b;
        b=r;
    }
    return a;
}

int main(){
    freopen("A.in","r",stdin);
    freopen("A.txt","w",stdout);
    int i;
    long long j,k;
    scanf("%d",&t);
    for(i=1;i<=t;++i){
        printf("Case #%d: ",i);
        scanf("%d %d %d",&n,&pd,&pg);
        j=gcd(pd,100);
        k=100/j;
        if(n>=k){
            if(pg==0){
                if(pd==0)
                    printf("Possible\n");
                else
                    printf("Broken\n");
            }else if(pg==100){
                if(pd==100)
                    printf("Possible\n");
                else
                    printf("Broken\n");
            }else
                printf("Possible\n");
        }else
            printf("Broken\n");
    }
}
