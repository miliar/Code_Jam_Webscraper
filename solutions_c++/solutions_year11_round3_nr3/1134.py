#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
    int t, n, l, h;
    int a[110];

    cin >> t;
    for (int ca = 1; ca <= t; ++ca)
    {
        cin >> n >> l >> h;
        for (int i = 0; i < n; i++)
            cin >> a[i];
        int i;
        for (i = l; i <= h; i++)
        {
            int j;
            for (j = 0; j < n; j++)
            {
                if ( a[j]%i != 0 && i%a[j] != 0 )
                    break;
            }
            if ( j >= n )
                break;
        }
        cout << "Case #" << ca << ": ";
        if (i <= h)
            cout << i << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}
