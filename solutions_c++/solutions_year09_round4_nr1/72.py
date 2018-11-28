#include <iostream>

using namespace std;

char a[64][64];
char tmp[64];

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        int n;
        cin >> n;
        for (int i=0; i<n; i++)
            cin >> a[i];

        int ans = 0;

        for (int i=0; i<n; i++)
        {
            int j, k;
            for (k=i; k<n; k++)
            {
                for (j=i+1; j<n; j++)
                    if (a[k][j] == '1')
                        break;
                if (j == n)
                    break;
            }
            ans += k-i;
            memcpy(tmp, a[k], sizeof(a[k]));
            for (int j=k; j>i; j--)
                memcpy(a[j], a[j-1], sizeof(a[j]));
            memcpy(a[i], tmp, sizeof(a[i]));
        }

        cout << "Case #" << tt << ": " << ans << endl;
    }

    return 0;
}
