#include <iostream>
#include <algorithm>
using namespace std;

typedef long long int64;

int64 gcd(int64 a, int64 b) {return b==0?a:gcd(b, a%b);}

int64 a[1000];
int n;

int main()
{
    freopen("B-small-attempt0.in.txt", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    
    int cs;
    scanf("%d", &cs);
    for (int fcs=1; fcs<=cs; fcs++)
    {
        scanf("%d", &n);
        for (int i=0; i<n; i++) scanf("%lld", &a[i]);
        sort(a, a+n);
        int64 d=a[1]-a[0];
        for (int i=2; i<n; i++) d=gcd(d, a[i]-a[i-1]);    
        int64 ans=(a[0]%d==0)?0:d-a[0]%d;
        printf("Case #%d: %lld\n", fcs, ans);
    }
    return 0;
}
