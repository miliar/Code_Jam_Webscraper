#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

int q,c,n;
long long t[4],d[4];

long long gcd(long long a,long long b){
    if (b==0) return a;
        else return gcd(b,a%b);
}

int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&q);
    for (int ttt=1;ttt<=q;ttt++){
        scanf("%d",&n);
        for (int i=1;i<=n;i++) scanf("%lld",&t[i]);
        sort(t+1,t+n+1);
        long long temp=t[2]-t[1];
        for (int i=2;i<=n-1;i++) temp=gcd(temp,t[i+1]-t[i]);

        //printf("%lld\n",temp);
        long long ans=temp;
        while(ans-t[1]<0) ans+=temp;
        printf("Case #%d: %lld\n",ttt,ans-t[1]);
    }
    return 0;
}
