#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

const int maxn = 1010;
int n;
long long g[maxn];

long long gcd(long long a, long long b)
{
    if (b == 0) return a; else return gcd(b, a%b);
}

long long mabs(long long a)
{
    if (a < 0) return -a; else return a;
}

int main()
{
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T, n;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cin >> n;
        for (int i = 0; i < n; ++i) cin >> g[i];
        long long now;
        now = mabs(g[1] - g[0]);
            for (int i = 2; i < n; ++i)
                now = gcd(now, mabs(g[i] - g[i - 1]));
        cout << "Case #" << t << ": " << (now - (g[0] % now)) % now << endl;
    }
    return 0;
}
