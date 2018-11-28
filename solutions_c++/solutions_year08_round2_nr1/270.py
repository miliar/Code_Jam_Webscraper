#include <iostream>

using namespace std;

long long z[3][3];

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        memset(z, 0, sizeof(z));
        int i, j, k, t, u, v, n;
        long long a, b, c, d, x, y, m;
        cin >> n >> a >> b >> c >> d >> x >> y >> m;
        for (i=0; i<n; i++)
        {
            z[x%3][y%3]++;
            x = (x*a + b)%m;
            y = (y*c + d)%m;
        }
        long long ans = 0;
        for (i=0; i<9; i++)
            for (j=i; j<9; j++)
            {
                k = (6 - i%3 - j%3)%3 + (6 - i/3 - j/3)%3*3;
                if (k < j)
                    continue;
                if (i != k && (i == j || j == k))
                {
                    ans += z[i/3][i%3] * (z[j/3][j%3] - 1) * z[k/3][k%3] / 2;
                    continue;
                }
                if (i == j && j == k)
                {
                    ans += z[i/3][i%3] * (z[j/3][j%3] - 1) * (z[k/3][k%3] - 2) / 6;
                    continue;
                }
                ans += z[i/3][i%3] * z[j/3][j%3] * z[k/3][k%3];

            }
        cout << "Case #" << tt << ": " << ans << endl;
    }
    return 0;
}
