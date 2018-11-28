#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
long long gcd(long long a,long long b){
    while((a%=b) && (b%=a));
    return a+b;
}
int main (){
    int flag,g,d,ca = 0,T,tmp,total;
    long long n;
    double c;
    int x,y;
    scanf("%d",&T);
    while(T--){
        flag =0;
        scanf("%lld%d%d",&n,&d,&g);
        tmp = 0;
        total = 0;
        for(y=1;y<=n && y <= 100;y++){
            for(x=0;x<=y;x++){
                if(100*x == d*y){
                    flag = 1;
                    tmp = x;
                    total = y;
                    //printf("tmp %d total %d\n",tmp,total);
                    break;
                }
            }
            if(flag == 1)break;
        }
        /*
        total = 0;
        tmp = 0;
        if(d != 0){
            tmp = d/gcd(d,100);
            total = 100 * tmp / d;
        }
        if(total > n)flag = 0;
        */
        /*
        c = 100*(tmp + 1e15)/(total+1e15);
        if(g > c)
            flag = 0;
        */
        if(flag == 1){
            flag = 0;
        for(y = 1;y < 10000;y++){
            for(x = 0;x <= y; x++){
                if( (tmp+x)/(total+y) > g+1)break;
                if(100*(tmp+x) == g * (total+y)){
                    flag = 1;
                   // printf("tmp+x %d total+y %d\n",tmp+x,total+y);
                    break;
                }
            }
            if(flag == 1)break;
        }
        }
        ca++;
        printf("Case #%d: ",ca);
        if(flag == 1)printf("Possible\n");
        else printf("Broken\n");
    }
    return 0;
}
