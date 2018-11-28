#include <iostream>

using namespace std;

int maxn = 1<<10;

int a[1<<11];

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        int p;
        cin >> p;
        maxn = 1<<p;
        for (int i=0; i < maxn; i++)
            cin >> a[i+maxn];
        for (int i=1; i < maxn; i++)
        {
            int x;
            cin >> x;
        }

        for (int i=0; i < maxn; i++)
            a[i+maxn] = p - a[i+maxn];

        for (int i=maxn-1; i; i--)
            a[i] = max(a[i+i], a[i+i+1]);

        int ans = 0;
        for (int i=0; i < p; i++)
            for (int j=1<<i; j < 2<<i; j++)
                if (a[j] > i)
                    ans++;                
                
        cout << "Case #" << tt << ": " << ans << endl;
    }
    return 0;
}
