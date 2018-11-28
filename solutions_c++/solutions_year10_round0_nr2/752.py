#include<stdio.h>
#include<memory.h>
#include<algorithm>
using namespace std;

long long data[110];
int t,n;

long long gcd(long long a,long long b){
    if(b==0)   return a;
    return gcd(b,a%b);
}
int main(){
    int ccount = 0;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
            scanf("%I64d",&data[i]);
        sort(data+1,data+1+n);
        long long m = data[2] - data[1];
        for(int i=3;i<=n;i++)
            m = gcd(m, data[i] - data[i-1]);
        long long test = data[1]%m;
        if(test==0)
           printf("Case #%d: %I64d\n",++ccount,0);
        else
           printf("Case #%d: %I64d\n",++ccount,m  - test);
    }
    return 0;
}

