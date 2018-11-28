#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <string>

#include <set>

using namespace std;

#define REP(i,N) for (int i=0; i<(int)N; i++)
#define FOREACH(v,it) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)




long long w [255];

double solve ()
{
    long long X, S, R, N;
    double t;
    cin >> X >> S >> R >> t >> N;
    REP (i, 255) w[i] = 0;
    w[0] = X;
    REP (i, N)
    {
        int B, E, W;
        cin >> B >> E >> W;
        w[W] += E - B;
        w[0] -= E - B;
    }
    long double ans = 0.0;
    REP (i, 255)
    {
        double dis = min (t * (R+i), (double)w[i]);
        ans += dis / (R+i);
        ans += (w[i] - dis) / (S+i);
        t -= dis / (R+i);
    }
    return ans;
}

int main ()
{
    freopen ("A-large.in", "r", stdin);
    freopen ("out.txt", "w", stdout);

    int T;
    cin >> T;
    REP (cas, T)
    {
        cout << "Case #" << cas+1 << ": " << setprecision(12) << solve() << endl;
    }
    return 0;
}
