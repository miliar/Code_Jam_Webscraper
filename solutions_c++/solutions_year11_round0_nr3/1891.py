#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

#define pb push_back
#define sz size

int it, n, a[2000];

void read ()
{
    cin >> n;
    for (int i = 0; i < n; ++i)
        cin >> a[i];
}

void solve ()
{
    sort( a, a + n );
    int xa = a[0], xb = 0, sb = 0;
    for (int i = 1; i < n; ++i)
    {
        xb ^= a[i];
        sb += a[i];
    }
    if (xa != xb)
        cout << "NO" << endl;
    else
        cout << sb << endl;
}

int main ()
{
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );

    cin >> it;
    for (int i = 0; i < it; ++i)
    {
        read();
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
