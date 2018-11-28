#include <stdio.h>
#include <iostream>
using namespace std;

int h,i,t,n,sum,tmp;

int main(){
    freopen("D-large.in", "r", stdin);
    freopen("D-large.txt", "w", stdout);
    scanf("%d",&t);
    for(h=1;h<=t;++h){
        sum=0;
        scanf("%d",&n);
        for(i=1;i<=n;++i){
            scanf("%d",&tmp);
            if(tmp==i) ++sum;
        }
        printf("Case #%d: %d.000000\n",h,n-sum);
    }
}
