#include <iostream>

using namespace std;

struct level
{
    int t, p, i;

    bool operator < (const level &other) const
    {
        int X = other.t * p;
        int Y = other.p * t;
        return X != Y ? X > Y : i < other.i;
    }
} a[1024];

int main()
{
    int t;
    cin >> t;
    for (int tt = 1; tt<=t; tt++)
    {
        int n;
        cin >> n;

        for (int i=0; i<n; i++)
            cin >> a[i].t;
        for (int i=0; i<n; i++)
        {
            cin >> a[i].p;
            a[i].i = i;
        }

        sort(a, a+n);
        cout << "Case #" << tt << ":";

        for (int i=0; i<n; i++)
            cout << " " << a[i].i;

        cout << endl;
    }
    return 0;
}
