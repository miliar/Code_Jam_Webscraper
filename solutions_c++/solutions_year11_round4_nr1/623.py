#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct sw
{
    int b, e, w;

    bool operator <(const sw &b) const
    {
        return w < b.w;
    }
};

int main()
{
    int t, tn = 1;

    cout.setf(ios::fixed);
    cout.precision(9);

    cin >> t;

    while (tn <= t)
    {
        int x, s, r, n;
        double t;
        vector<sw> inp;
        double ans;

        cin >> x >> s >> r >> t >> n;

        inp.resize(n);
        for (int i = 0; i < n; i++)
        {
            cin >> inp[i].b >> inp[i].e >> inp[i].w;
            x -= inp[i].e - inp[i].b;
        }

        if (t > (double)x / (double)r)
        {
            ans = (double)x / (double)r;
            t -= ans;
        }
        else
        {
            ans = t + (x - t * r) / (double)s;
            t = 0.0;
        }

        sort(inp.begin(), inp.end());

        for (int i = 0; i < n; i++)
            if (t * (r + inp[i].w) > inp[i].e - inp[i].b)
            {
                ans += (double)(inp[i].e - inp[i].b) / (double)(r + inp[i].w);
                t -= (double)(inp[i].e - inp[i].b) / (double)(r + inp[i].w);
                x -= inp[i].e - inp[i].b;
            }
            else
            {
                ans += t;
                ans += (inp[i].e - inp[i].b - t * (r + inp[i].w)) / (double)(s + inp[i].w);
                t = 0.0;
                x -= inp[i].e - inp[i].b;
            }


        cout << "Case #" << tn << ": " << ans << endl;
        tn++;
    }

    return 0;
}
