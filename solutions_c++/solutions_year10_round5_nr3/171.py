#include <iostream>

using namespace std;

const int maxx = 1<<20;

int a[maxx*2];

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        memset(a, 0, sizeof(a));

        int n;
        cin >> n;

        for (int i=0; i<n; i++)
        {
            int p, v;
            cin >> p >> v;
            a[p+maxx] = v;
        }

        int ans = 0;

        for (int i=0; i<maxx*2; i++)
            if (a[i] >= 2)
            {
                ans += a[i]/2;
                a[i-1] += a[i]/2;
                a[i+1] += a[i]/2;
                a[i] %= 2;
                i -= 2;
            }
        
        cout << "Case #" << tt << ": " << ans << endl;
    }
    return 0;
}
