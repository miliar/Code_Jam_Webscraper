#include <iostream>
#include <cstdio>

using namespace std;

#define REP(i,N) for (int i=0; i<N; i++)


int main ()
{
    freopen ("C-large.in", "r", stdin);
    freopen ("out.txt", "w", stdout);

    int T, N, x;
    cin >> T;
    REP (cas, T)
    {
        int xs = 0, small = 1<<29, total = 0;
        cin >> N;
        REP (i, N)
        {
            cin >> x;
            xs ^= x;
            small = min (small, x);
            total += x;
        }
        int ans = total - small;
        cout << "Case #" << (cas+1) << ": ";
        if (xs == 0) cout << ans << endl;
        else cout << "NO" << endl;
    }

    return 0;
}
