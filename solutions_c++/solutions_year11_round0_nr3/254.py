#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int n,total;
int t,x,d,minN;

int main(){
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&t);
    for (int cas = 1; cas <= t; ++cas ){
        scanf("%d",&n);
        scanf("%d",&d);
        minN = total = d;
        for (int i = 1; i < n; ++i){
            scanf("%d",&x);
            if( x < minN ) minN = x;
            d ^= x;
            total += x;
        }
        printf("Case #%d: ",cas);
        if( d ) printf("NO\n");
        else printf("%d\n",total - minN);
    }
    return 0;
}
