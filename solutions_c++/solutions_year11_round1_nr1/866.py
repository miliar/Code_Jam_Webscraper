#include<iostream>
#include<stdio.h>
#include<map>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,pd,pg,i,x,y,k;
    long long n;
    scanf("%d",&t);
    for(k=1;k<=t;k++) {
        scanf("%lld%d%d",&n,&pd,&pg);
        printf("Case #%d: ",k);
        if((pd!=0&&pg==0)||(pd!=100&&pg==100)) {
            printf("Broken\n");
            continue;
        }
        if(pd==0) {
            printf("Possible\n");
            continue;
        }
        if(pd%2==1) x=1;
        if(pd%4==2) x=2;
        if(pd%4==0) x=4;
        if(pd%5!=0) y=1;
        if(pd%5==0&&pd%25!=0) y=5;
        if(pd%25==0) y=25;
        long long m;
        m=100/((long long)x*y);
        if(n>=m) printf("Possible\n");
        else printf("Broken\n");
    }
    return 0;
}
