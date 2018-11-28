#include <iostream>
#include <cstdio>

using namespace std;

const int maxn = 1005;
long long a[maxn],c[maxn];

long long gcd(long long x,long long y){
    if (y == 0) return x; return gcd(y,x%y);
}

long long calc_abs(long long k){
    if (k > 0) return k; return -k;
}

int main()
{
    freopen("B.in","r",stdin); freopen("B.out","w",stdout);
    int t,n; scanf("%d",&t);
    for (int casenum=1; casenum <= t; ++casenum){
        cin >> n;
        for (int i=1; i<=n; ++i)
            cin >> a[i];
        for (int i=1; i<n; ++i)
            c[i] = calc_abs(a[i+1]-a[i]);
        long long ans = c[1];
        for (int i=2; i<n; ++i)
            ans = gcd(ans,c[i]);
        long long tmp = a[1]%ans;
        printf("Case #%d: ",casenum);
        cout << (ans-tmp)%ans << endl;
    }
    return 0;
}
