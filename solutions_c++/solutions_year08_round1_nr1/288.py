#include<iostream>
#include<stdlib.h>
#include<set>
#include<map>
#include<algorithm>
#include<queue>
#include<utility>
using namespace std;
#define oo 2100000000
#define eps 0.000001
long long N,n,k,i,x[801],y[801];
long long sum;
    bool cmp(long long a, long long b){
        return a>b;
    }
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%lld",&N);
    for(k=1;k<=N;++k){
        scanf("%I64d",&n);
        for(i=0;i<n;++i)scanf("%I64d",x+i);
        for(i=0;i<n;++i)scanf("%I64d",y+i);
        sort(x,x+n);
        sort(y,y+n,cmp);
        for(i=0,sum=0;i<n;++i)
        sum+=x[i]*y[i];
        printf("Case #%I64d: %I64d\n",k,sum);
    }
    return 0;
}        
