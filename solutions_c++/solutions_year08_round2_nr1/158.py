#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    int N;
    cin >> N;
    for (int ca = 1; ca <= N; ca++)
    {
        long long n, a, b, c, d, x0, y0, m;
        cin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;

        long long count[3][3];
        memset(count, 0, sizeof(count));
        long long x = x0, y = y0;
        for (int i = 0; i < n; i++)
        {
            //cout << x << " " << y << endl;
            count[x % 3][y % 3]++;
            x = (a * x + b) % m;
            y = (c * y + d) % m;
        }

        long long total = 0;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
            {
                if (count[i][j] == 0)
                    continue;
                long long c1 = count[i][j];
                count[i][j]--;
                for (int k = 0; k < 3; k++)
                    for (int l = 0; l < 3; l++)
                    {
                        if (count[k][l] == 0)
                            continue;
                        long long c2 = count[k][l];
                        count[k][l]--;

                        int rx = (6 - i - k) % 3;
                        int ry = (6 - j - l) % 3;

                        //cerr << i << " " << j << " " << k << " " << l << " " << rx << ":" << ry << endl;
                        total += c1 * c2 * count[rx][ry];
                        count[k][l]++;
                    }
                count[i][j]++;
            }

        cout << "Case #" << ca << ": " << (total / 6) << endl;
    }
    return 0;
}
