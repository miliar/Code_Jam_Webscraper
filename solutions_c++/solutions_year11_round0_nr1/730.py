#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define REP(i,N) for (int i=0; i<N; i++)

int T, N, x, r, t, prevx[2], prevt[2];
char c;

int abs (int x) { return (x > 0) ? x : -x; }

int main ()
{
    freopen ("A-large.in", "r", stdin);
    freopen ("out.txt", "w", stdout);

    cin >> T;
    REP (cas, T)
    {
        cin >> N;
        REP (j, 2) prevx[j] = 1, prevt[j] = 0;
        t = 0;
        REP (i, N)
        {
            cin >> c >> x;
            int r = (c == 'B');
            int dt = abs (x - prevx[r]);
            prevx[r] = x;
            t = prevt[r] = 1 + max (t, prevt[r] + dt);
        }
        cout << "Case #" << (cas+1) << ": " << t << endl;
    }
    return 0;
}
