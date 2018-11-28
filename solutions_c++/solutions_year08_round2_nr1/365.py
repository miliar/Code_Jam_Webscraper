#include <iostream>
#include <fstream>
using namespace std;

int N, nt, n, i, j, k;
long long a, b, c, d, x0, y0, m, res, x, y;
long long p[100005][2];
int q[3][3][100000];

int main()
{
    ifstream fin("in.txt");
    fin >> N;
    for(nt = 1; nt <= N; ++nt)
    {
        fin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
        for(i = 0; i < 3; ++i) for(j = 0; j < 3; ++j) q[i][j][0] = 0;
        p[0][0] = x0;
        p[0][1] = y0;
        q[x0 % 3][y0 % 3][0] = 1;
        q[x0 % 3][y0 % 3][1] = 0;
        for(i = 1; i < n; ++i)
        {
            p[i][0] = (a * p[i - 1][0] + b) % m;
            p[i][1] = (c * p[i - 1][1] + d) % m;
            ++q[p[i][0] % 3][p[i][1] % 3][0];
            q[p[i][0] % 3][p[i][1] % 3][q[p[i][0] % 3][p[i][1] % 3][0]] = i;
        }

        res = 0;
        for(i = 0; i < (n - 2); ++i)
        {
            for(j = i + 1; j < (n - 1); ++j)
            {
                for(k = j + 1; k < n; ++k)
                {
                    x = (p[i][0] + p[j][0] + p[k][0]) % 3;
                    y = (p[i][1] + p[j][1] + p[k][1]) % 3;
                    if((x == 0) && (y == 0)) ++res;
                }
/*
                x = (3 - ((p[i][0] + p[j][0]) % 3)) % 3;
                y = (3 - ((p[i][1] + p[j][1]) % 3)) % 3;
                for(k = 1; k <= q[x][y][0]; ++k) if(q[x][y][k] > j) break;
                res += q[x][y][0] - r + 1;

                l = 1;
                r = q[x][y][0];
                if(r > 0)
                {
                    while((r - l) > 1)
                    {
                        m = (l + r) >> 1;
                        if(q[x][y][m] < j) l = m;
                        else r = m;
                    }
                    if(q[x][y][r] <= j) ++r;
                    res += q[x][y][0] - r + 1;
                }
*/
            }
        }
        cout << "Case #" << nt << ": " << res << endl;
    }
    return 0;
}
