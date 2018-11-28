#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct Walkway
{
    double l;
    double w;
    bool operator<(Walkway const & other) const
    {
        return w < other.w;
    }
};

int main()
{
    int T;
    cin >> T;
    cout.precision(18);
    for (int K = 1; K <= T; ++K)
    {
        double x;
        double s;
        double r;
        double t;
        int n;
        cin >> x >> s >> r >> t >> n;

        vector<Walkway> ws(n+1);
        for (int i = 1; i <= n; ++i)
        {
            double b, e;
            cin >> b >> e >> ws[i].w;
            ws[i].l = e - b;
            x -= ws[i].l;
        }
        ws[0].l = x;
        ws[0].w = 0;
        sort(ws.begin(), ws.end());

        double ans = 0;
        for (int i = 0; i <= n; ++i)
        {
            double t0 = min(t, ws[i].l / (ws[i].w + r));
            t -= t0;
            ans += t0;
            double t1 = (ws[i].l - (ws[i].w + r) * t0) / (ws[i].w + s);
            ans += t1;
        }

        cout << "Case #" << K << ": " << ans << "\n";
    }

    return 0;
}
