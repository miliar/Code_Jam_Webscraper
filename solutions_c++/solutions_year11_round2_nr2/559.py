#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

bool foo(int c, int d, vector<int> const & v, vector<int> const & p, double t)
{
    double last_x = p[0] - t - d - 1;
    for (int i = 0; i < c; ++i)
    {
        for (int j = 0; j < v[i]; ++j)
        {
            double min_x = last_x + d;
            if (min_x < p[i])
            {
                last_x = max(min_x, p[i] - t);
                continue;
            }
            
            if (p[i] + t < min_x)
            {
                return false;
            }
            last_x = min_x;
        }
    }
    return true;
}

int main()
{
    int T;
    cin >> T;
    cout << setprecision(18);
    for (int K = 1; K <= T; ++K)
    {
        int c, d;
        cin >> c >> d;
        vector<int> v(c);
        vector<int> p(c);
        for (int i = 0; i < c; ++i)
        {
            cin >> p[i] >> v[i];
        }

        double lo = 0;
        double hi = 1;
        while (!foo(c, d, v, p, hi))
        {
            lo = hi;
            hi *= 2;
        }

        while (hi - lo > 1e-9)
        {
            if (foo(c, d, v, p, (lo + hi) / 2))
            {
                hi = (lo + hi) / 2;
            }
            else 
            {
                lo = (lo + hi) / 2;
            }
        }
        cout << "Case #" << K << ": " << lo << "\n";

    }
    return 0;
}
