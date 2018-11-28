#include <iostream>
#include <cstdio>

using namespace std;

#define REP(i,N) for (int i=0; i<N; i++)

int gcd (int a, int b)
{
    if (a == 0) return b;
    return gcd (b % a, a);
}

int main ()
{
    freopen ("A-large.in", "r", stdin);
    //freopen ("A-large.in", "r", stdin);
    freopen ("out.txt", "w", stdout);

    int T;
    cin >> T;
    REP (cas, T)
    {
        long long n;
        int pd, pg;
        cin >> n >> pd >> pg;

        int x = 100 / gcd (pd, 100);

        bool ok = (x <= n);
        if (pg == 100 && pd < 100) ok = false;
        if (pg == 0 && pd > 0) ok = false;

        cout << "Case #" << (cas+1) << ": ";
        if (ok) cout << "Possible";
        else cout << "Broken";
        cout << endl;
    }
    return 0;
}
