#include<stdio.h>
#include<math.h>
#include<stdlib.h>
using namespace std;

long long a[1000];

long long gcd(long long a, long long b)
{
    long long r;
    
    while(b){
        r=a%b;
        a=b;
        b=r;
    }
    return a;
}

int main()
{
    freopen("b.in", "r" , stdin);
    freopen("b.out", "w", stdout);
    
    int cc, ct, i, n;
    long long T, x;
    
    scanf("%d", &cc);
    for(ct=1; ct<=cc; ct++){
        scanf("%d", &n);
        for(i=0; i<n; i++) scanf("%I64d", &a[i]);
        T=0;
        for(i=1; i<n; i++) T=gcd(T, abs(a[i]-a[i-1]));
        x=(-a[0]%T+T)%T;
        printf("Case #%d: %I64d\n", ct, x);
    }
    
    return 0;
}
