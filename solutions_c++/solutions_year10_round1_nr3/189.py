#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

const double p = (sqrt(5) - 1)/2;
long long ans;

void solve(long long a1,long long a2,long long b1,long long b2){
    for (long long i=a1; i<=a2; ++i){
        long long c = i * p;
        if (c >= b2)
            ans += b2-b1+1;
        else if (c >= b1)
            ans += c-b1+1;
    }
}

int main()
{
    freopen("C.in","r",stdin); freopen("C.out","w",stdout);
    int t; scanf("%d",&t);
    for (int casenum=1; casenum <= t; ++casenum){
        long long a1,a2,b1,b2;
        cin >> a1 >> a2 >> b1 >> b2;
        ans = 0;
        solve(a1,a2,b1,b2);
        solve(b1,b2,a1,a2);
        printf("Case #%d: ",casenum);
        cout << ans << endl;
    }
    return 0;
}
