#include <algorithm>
#include <cstdio>
using namespace std;
typedef long long ll;

ll gcd(ll a, ll b)
{
    ll t;
    while (b) t = a%b, a = b, b = t;
    return a;
}

int main()
{
    int cases;
    ll n, pd, pg;
    scanf("%d", &cases);
    for (int T = 1; T <= cases; T++) {
        scanf("%lld%lld%lld", &n, &pd, &pg);
        ll d = max(100 / gcd(100, pd), 1LL);
        printf("Case #%d: ", T);
        if (pg == 100 && pd != 100 || pg == 0 && pd != 0 || d > n)
            puts("Broken");
        else
            puts("Possible");
    }
}
