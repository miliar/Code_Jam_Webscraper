#include <stdio.h>
#include <algorithm>
using namespace std;
int v1[1000],v2[1000];
int main(){
    int t,x,n,i;
    long long y;
    scanf("%d",&t);
    for(x=1;x<=t;x++){
        scanf("%d",&n);
        for(i=0;i<n;i++){
            scanf("%d",v1+i);
        }
        for(i=0;i<n;i++){
            scanf("%d",v2+i);
        }
        sort(v1,v1+n);
        sort(v2,v2+n);
        for(y=0,i=0;i<n;i++){
            y+=(long long)v1[i]*(long long)v2[n-1-i];
        }
        printf("Case #%d: %I64d\n",x,y);
    }
    return 0;
}        
