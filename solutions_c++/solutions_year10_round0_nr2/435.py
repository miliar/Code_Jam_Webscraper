#include <iostream>
using namespace std;

int n;
long long list[10000];

long long myabs(long long v)
{
    return v < 0 ? - v : v;
}

long long gcd(long long a, long long b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

void solve()
{
    cin >> n;
    for (int i = 0; i < n; i ++)
        cin >> list[i];

    long long T = myabs(list[0] - list[1]);

    int i, j;
    for (i = 0; i < n; i ++)
        for (j = i + 1; j < n; j ++)
            T = gcd(T, myabs(list[i] - list[j]));

    long long y = (T - list[0] % T) % T;
    cout << y << endl;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small.out", "w", stdout);

    int T, t;
    cin >> T;

    for (t = 1; t <= T; t ++)
    {
        cout << "Case #" << t << ": ";

        solve();
    }
}
