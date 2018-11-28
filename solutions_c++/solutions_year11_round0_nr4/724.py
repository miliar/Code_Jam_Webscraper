#include <iostream>
#include <cstdio>

using namespace std;

#define REP(i,N) for (int i=0; i<N; i++)

int g[1005];
bool flag[1005];

int dfs (int x)
{
    if (flag[x]) return 0;
    flag[x] = true;
    return 1 + dfs (g[x]);
}

int main ()
{
    freopen ("D-large.in", "r", stdin);
    freopen ("out.txt", "w", stdout);

    int T, N;
    cin >> T;
    REP (cas, T)
    {
        double ans = 0.0;
        cin >> N;
        REP (i, N) cin >> g[i];
        REP (i, N) g[i]--, flag[i] = false;
        REP (i, N)
        {
            int d = dfs (i);
            if (d > 1) ans += (double)d;
        }
        cout << "Case #" << (cas+1) << ": " << ans << endl;
    }

    return 0;
}
