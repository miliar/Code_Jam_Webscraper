#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int main()
{
    int T, testcase;
    int X;
    int S;
    int R;
    int N, n;
    double t;
    vector<pair<int, int> > w; // speed, length
    int b, e;
    double ans;
    double time_if_run;

    cin >> T;
    for (testcase = 1; testcase <= T; testcase++)
    {
        cin >> X;
        cin >> S >> R;
        cin >> t;
        cin >> N;
        w.resize(N + 1);
        for (n = 0; n < N; n++)
        {
            cin >> b >> e;
            w[n].second = e - b;
            X -= (e - b);
            cin >> w[n].first;
        }
        w[N].second = X;
        w[N].first = 0;
        sort(w.begin(), w.end());
        ans = 0.0;
        for (n = 0; n <= N; n++)
        {
            time_if_run = (double) w[n].second / (w[n].first + R);
            if (time_if_run > t)
            {
                // run for t second
                ans += t;
                ans += (double) (w[n].second - t * (w[n].first + R)) / (w[n].first + S);
                t = 0;
            }
            else
            {
                // run for the whole walkway
                ans += time_if_run;
                t -= time_if_run;
            }
        }
        printf("Case #%d: %.9lf\n", testcase, ans);
    }

    return 0;
}

