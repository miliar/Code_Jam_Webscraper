#include<stdio.h>
#include<stdlib.h>
#define SIZE 1000
using namespace std;
long long a[SIZE];
long long R,n,k,an;
long long Go(long long x){
    long long j=0,y=x;
    while(j+a[x]<=k){
        j+=a[x];
        x++;
        if(x==n)x=0;
        if(y==x)break;
    }
    an+=j;
    return x;
}
main(){
    long long T,t=0,i,j;
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small.out","w",stdout);
    scanf("%I64d",&T); 
    while(T--){
        an=0;
        t++;
        scanf("%I64d %I64d %I64d",&R,&k,&n);
        for(i=0;i<n;i++){
            scanf("%I64d",&a[i]);
        }
        i=0;
        while(R--)i=Go(i);
        printf("Case #%I64d: %I64d\n",t,an);
    }
}
