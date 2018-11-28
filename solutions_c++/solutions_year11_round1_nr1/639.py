#include<stdio.h>
#include<iostream>
using namespace std;

long long gcd(long long a, long long b)
{
    long long r;
    while(b)
    {
        r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    
    int T, tt;
    long long n, pd, qd, pg, qg, g;
    
    scanf("%d", &T);
    for(tt = 1; tt <= T; tt++)
    {
        printf("Case #%d: ", tt);
        cin >> n >> pd >> pg;
        g = gcd(pd, 100);
        pd /= g;
        qd = 100 / g;
        g = gcd(pg, 100);
        pg /= g;
        qg = 100 / g;
        if(qd > n)
        {
            cout << "Broken\n";
            continue; 
        }
        if(pg == 0 && pd > 0){
            cout << "Broken\n";
            continue;
        }
        if(pg == qg && pd < qd)
        {
            cout << "Broken\n";
            continue;
        }
        cout << "Possible\n";
    }
    
    return 0;
}
