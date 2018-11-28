#include <iostream>

using namespace std;

bool prime(long long x)
{
    for (long long d = 2; d*d <= x; d++)
        if (!(x%d))
            return false;
    return true;
}

bool v[1<<20];

long long a, b, p;

void dfs(long long x)
{
    if (v[x])
        return;
    v[x] = true;
    for (long long d = 2; d <= b-a; d++)
        if (!(x%d))
        {
            for (; !(x%d); x/=d);
            if (d < p)
                continue;
            for (long long i=(a+d-1)/d*d; i<=b; i+=d)
                dfs(i);
        }
}

int main()
{
    int t;
    cin >> t;
    for (int tt = 1; tt<=t; tt++)
    {
        cin >> a >> b >> p;
        memset(v, 0, sizeof(v));
        long long ans = 0;
        for (long long i=a; i<=b; i++)
            if (!v[i])
            {
                ans++;
                dfs(i);
            }
        cout << "Case #" << tt << ": " << ans << endl;
    }
    return 0;
}
