#include <iostream>

using namespace std;

int a[128][32];

bool b[128][128];

int d[1<<16];
int e[1<<16];

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        int n, m;
        cin >> n >> m;

        for (int i=0; i<n; i++)
            for (int j=0; j<m; j++)
                cin >> a[i][j];

        for (int i=0; i<n; i++)
            for (int j=0; j<n; j++)
            {
                b[i][j] = true;
                for (int k=0; k<m; k++)
                    if (a[i][k] >= a[j][k])
                        b[i][j] = false;
            }

        memset(d, 1, sizeof(d));
        memset(e, 1, sizeof(d));

        for (m = 1; m < 1 << n; m++)
        {
            int c[32] = {};
            int z = 0;
            
            for (int i=0; i<n; i++)
                if (1 << i & m)
                {
                    int k = 0;
                    for (int j=0; j<n; j++)
                        if (1 << j & m)
                            k += b[i][j];
                    z++;
                    c[k]++;
                }

            for (int i=0; i<z; i++)
                if (!c[i])
                    e[m] = 0;
        }

        d[0] = 0;

        for (m = 1; m < 1 << n; m++)
            for (int r = m; r; r = r - 1 & m)
                if (e[r])
                    d[m] = min(d[m], d[m ^ r] + 1);

        cout << "Case #" << tt << ": " << d[(1<<n) - 1] << endl;
    }

    return 0;
}
