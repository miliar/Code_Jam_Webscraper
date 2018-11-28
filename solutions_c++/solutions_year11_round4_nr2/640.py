#include <iostream>
#include <cmath>

double a[500][500];

double m[3][500][500];
double x[3][500][500];
double y[3][500][500];

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        int r, c, d;
        std::cin >> r >> c >> d;
        for (int i = 0 ; i < r ; ++i)
        {
            for (int j = 0 ; j < c ; ++j)
            {
                char c;
                std::cin >> c;
                m[0][i][j] = a[i][j] = d + c - '0';
                x[0][i][j] = j;
                y[0][i][j] = i;
            }
        }
        int kk = 1;
        int K = std::min(r, c);
        int res = -1;
        for (int k = 2 ; k <= K ; ++k)
        {
            for (int i = 0 ; i <= r - k ; ++i)
            {
                for (int j = 0 ; j <= c - k ; ++j)
                {
                    int k1 = (3 + kk - 1) % 3;
                    int k2 = (3 + kk - 2) % 3;
                    m[kk][i][j] = m[k1][i][j] + m[k1][i+1][j+1] + a[i][j+k-1] + a[i+k-1][j] - 
                        (k > 2 ? m[k2][i+1][j+1] : 0);
                    x[kk][i][j] = (m[k1][i][j] * x[k1][i][j]
                                + m[k1][i+1][j+1] * x[k1][i+1][j+1]
                                + a[i][j+k-1] * (j+k-1)
                                + a[i+k-1][j] * j
                                - (k > 2 ? m[k2][i+1][j+1] * x[k2][i+1][j+1] : 0)
                                ) / m[kk][i][j];
                    y[kk][i][j] = (m[k1][i][j] * y[k1][i][j]
                                + m[k1][i+1][j+1] * y[k1][i+1][j+1]
                                + a[i][j+k-1] * i
                                + a[i+k-1][j] * (i+k-1)
                                - (k > 2 ? m[k2][i+1][j+1] * y[k2][i+1][j+1] : 0)
                                ) / m[kk][i][j];
                }
            }

            if (k >= 3)
            for (int i = 0 ; i <= r - k ; ++i)
            {
                for (int j = 0 ; j <= c - k ; ++j)
                {
                    double xx = (x[kk][i][j] * m[kk][i][j]
                              - j * a[i][j]
                              - j * a[i+k-1][j]
                              - (j+k-1) * a[i+k-1][j+k-1]
                              - (j+k-1) * a[i][j+k-1])
                              / (m[kk][i][j] - a[i][j] - a[i+k-1][j] - a[i+k-1][j+k-1] - a[i][j+k-1]);
                    double yy = (y[kk][i][j] * m[kk][i][j]
                              - i * a[i][j]
                              - (i+k-1) * a[i+k-1][j]
                              - (i+k-1) * a[i+k-1][j+k-1]
                              - i * a[i][j+k-1])
                              / (m[kk][i][j] - a[i][j] - a[i+k-1][j] - a[i+k-1][j+k-1] - a[i][j+k-1]);
                    if (std::fabs(yy - (i + i + k - 1) / 2.0) < 0.00000001
                        && std::fabs(xx - (j + j + k - 1) / 2.0) < 0.00000001)
                    {
                        res = k;
                    }
                }
            }

            kk = (kk + 1) % 3;
        }

        std::cout << "Case #" << t << ": ";
        if (res >= 3)
            std::cout << res;
        else
            std::cout << "IMPOSSIBLE";
        std::cout << "\n";
    }
	return 0;
}

