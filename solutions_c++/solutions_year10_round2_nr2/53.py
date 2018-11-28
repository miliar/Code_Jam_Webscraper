#include <iostream>

using namespace std;

int x[64];
int v[64];

int main()
{
    int t;
    cin >> t;
    for (int tt = 1; tt<=t; tt++)
    {
        int n, k, b, q;
        cin >> n >> k >> b >> q;

        for (int i=0; i<n; i++)
            cin >> x[i];
        for (int i=0; i<n; i++)
            cin >> v[i];

        int y = 0;
        int ans = 0;
        for (int i=n-1; i>=0 && k; i--)
        {
            if (x[i] + q*v[i] >= b)
            {
                ans += y;
                k--;
            }
            else
                y++;
        }

        cout << "Case #" << tt << ": ";
        if (k)
            cout << "IMPOSSIBLE";
        else
            cout << ans;
        cout << endl;
    }
    return 0;
}
