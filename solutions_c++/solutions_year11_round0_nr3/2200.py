#include <iostream>
#include <vector>

using namespace std;

int a[1024];

int main()
{
    int t;
    cin >> t;

    for (int tt=1; tt<=t; tt++)
    {
        cout << "Case #" << tt << ": ";

        int n;
        cin >> n;

        int m = 1<<20;
        int s = 0;
        int t = 0;

        for (int i=0; i<n; i++)
        {
            cin >> a[i];
            m = min(m, a[i]);
            s ^= a[i];
            t += a[i];
        }

        if (s == 0)
            cout << t - m << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}
