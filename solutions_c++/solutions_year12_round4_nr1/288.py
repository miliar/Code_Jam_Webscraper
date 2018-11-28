#include <iostream>
#include <algorithm>

using namespace std;

struct ledge
{
    int x, d;

    bool operator < (const ledge &right) const
    {
        return x < right.x;        
    }
} a[1<<14];

int d[1<<14];

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        int n;
        cin >> n;
        for (int i=0; i<n; i++)
            cin >> a[i].x >> a[i].d;

        cin >> a[n].x;
        sort(a+1, a+n);

        memset(d, 0, sizeof(d[0]) * (n+1));
        d[0] = a[0].x;

        for (int i=0; i<n; i++)
        {
            d[i] = min(d[i], a[i].d);

            for (int j=i+1; j<=n; j++)
                if (d[i] + a[i].x >= a[j].x && d[j] < a[j].x - a[i].x)
                    d[j] = a[j].x - a[i].x;
        }

        cout << "Case #" << tt << ": " << (d[n] ? "YES" : "NO") << endl;
    }
    return 0;
}
