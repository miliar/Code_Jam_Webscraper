#include <iostream>

using namespace std;

int s = 0;

struct circle
{
    int x, y;
    int i;
    int r;

    bool operator < (const circle &right) const
    {
        return s ? i < right.i : r > right.r;
    }
} a[1024];

int main()
{
    int t;
    cin >> t;
    cout.setf(ios::fixed);
    cout.precision(5);

    for (int tt=1; tt<=t; tt++)
    {
        int n, w, h;
        cin >> n >> w >> h;

        for (int i=0; i<n; i++)
        {
            cin >> a[i].r;
            a[i].i = i;
        }

        s = 0;
        sort(a, a+n);

        for (int i=0, k=0; i<n; )
        {
            a[i].x = (rand() << 15 | rand()) % (w + 1);
            a[i].y = (rand() << 15 | rand()) % (h + 1);

            bool ok = true;

            for (int j=0; j<i; j++)
                if ((long long)(a[i].x - a[j].x) * (a[i].x - a[j].x) + (long long)(a[i].y - a[j].y) * (a[i].y - a[j].y) < (long long)(a[i].r + a[j].r) * (a[i].r + a[j].r))
                {
                    ok = false;
                    break;
                }
            k++;
            if (ok)
            {
                i++;
                k = 0;
            }

            if (k == 1000)
                i = 0;
        }

        s = 1;
        sort(a, a+n);        
        
        cout << "Case #" << tt << ":";
        for (int i=0; i<n; i++)
            cout << " " << a[i].x << " " << a[i].y;
        cout << endl;
    }
    return 0;
}
