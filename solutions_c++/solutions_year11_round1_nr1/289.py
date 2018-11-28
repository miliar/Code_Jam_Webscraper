#include <cstdio>
#include <iostream>

using namespace std;

typedef long long LL;

LL gcd(LL x, LL y)
{
    return x ? gcd(y % x, x) : y;
}

LL  n, p, q, d;
int tc;

bool good_(LL p, LL q, LL n)
{
        if (p > 0 && q==0) return false;
        LL d = gcd(100, p);
        LL b1 = 100 / d;
        bool ok = false;
        if (b1 <= n)
        {
            d = gcd(100, q);
            for(int i=1; i<= 100; ++i)
            {
                LL b2 = b1*i;
                if ( (b2*(p - q)) % d == 0) ok = true;
            }
        }
        return ok;
}

bool good(LL p, LL q, LL n)
{
    LL d = gcd(100, p);
    LL i = 100 / d;

    d = gcd(100, q);
    LL j = (100 / d) * 100;
    if (i > n) return false;
    return p*i <= q*j && (100-p)*i <= (100-q)*j;
}

bool simple(LL p, LL q, LL n, bool print = false)
{
    for(int i=1; i<=n; ++i) if (i*p % 100 == 0)
        for(int j=i; j<= 100*i; ++j) if (j*q % 100 == 0 && i*p/100 <= j*q/100 && i*(100-p)/100 <= j*(100-q)/100)
        {
            if (print) cout << "*" << i << ", " << j << endl;
            return true;
        }
    return false;
}



int main()
{
    //freopen("a.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    /*
    for(int N = 1; N<= 10; ++N)
        for(int P=0; P<=100; ++P)
            for(int Q=0; Q<=100; ++Q)
                if (good(P, Q, N) != simple(P, Q, N))
                {
                    cout << "N=" << N << "  P=" << P << " Q=" << Q<< endl;
                    cout << good(P, Q, N) << endl;
                    cout << simple(P, Q, N, true) << endl;
                    return 0;
                }
    
    cout << simple(10, 100, 10, true) << endl;
    */
    cin >> tc;
    for(int tt=1; tt<=tc; ++tt)
    {
        cin >> n >> p >> q;
        
        cout << "Case #" << tt << ": ";
        if (good(p, q, n)) cout << "Possible"; else cout << "Broken";
        cout << endl;
    }
    
}