#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

int r, c, d;
char a[501][501];
int b[501][501];
string str;

inline double sqr(double x)
{
    return x * x;
}

bool f(int k)
{
    int l = k / 2;
    if (k % 2 == 0)
    {
        for (int i = 0; i + k <= r; ++i)
             for (int j = 0; j + k <= c; ++j) {
                        double massx = 0, massy = 0;
                        for (int x = 0; x < k; ++x)
                            for (int y = 0; y < k; ++y) {
                                //double l = sqrt(sqr(k - i - 0.5) + sqr(k - j - 0.5))
                                massx += a[i+x][j+y] * (x - l + 0.5);
                                massy += a[i+x][j+y] * (y - l + 0.5);
                            }
                                massx -= a[i][j] * (0 - l + 0.5);
                                massy -= a[i][j] * (0 - l + 0.5);
                                massx -= a[i+k-1][j+k-1] * (k-1 - l + 0.5);
                                massy -= a[i+k-1][j+k-1] * (k-1 - l + 0.5);
                                massx -= a[i][j+k-1] * (0 - l + 0.5);
                                massy -= a[i][j+k-1] * (k-1 - l + 0.5);
                                massx -= a[i+k-1][j] * (k-1 - l + 0.5);
                                massy -= a[i+k-1][j] * (0 - l + 0.5);

                        if (fabs(massx) < 1e-6 && fabs(massy) < 1e-6)
                            return true;
              } 
    }
    else
    {
        for (int i = 0; i + k <= r; ++i)
             for (int j = 0; j + k <= c; ++j) {
                        double massx = 0, massy = 0;
                        for (int x = 0; x < k; ++x)
                            for (int y = 0; y < k; ++y) {
                                //double l = sqrt(sqr(k - i - 0.5) + sqr(k - j - 0.5))
                                massx += a[i+x][j+y] * (x - l);
                                massy += a[i+x][j+y] * (y - l);
                            }
                                massx -= a[i][j] * (0 - l);
                                massy -= a[i][j] * (0 - l);
                                massx -= a[i+k-1][j+k-1] * (k-1 - l);
                                massy -= a[i+k-1][j+k-1] * (k-1 - l);
                                massx -= a[i][j+k-1] * (0 - l);
                                massy -= a[i][j+k-1] * (k-1 - l);
                                massx -= a[i+k-1][j] * (k-1 - l);
                                massy -= a[i+k-1][j] * (0 - l);

                            if (fabs(massx) < 1e-6 && fabs(massy) < 1e-6)
                            return true;
              } 
    }
    return false;

}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for (int TT = 1; TT <= T; ++TT)
    {
        cin >> r >> c >> d;
        for (int i = 0; i < r; ++i)
        {
            cin >> str;
            for (int j = 0; j < c; ++j)
            {
                a[i][j] = str[j] - '0';
            }
        }

        int ans = -1;
        for (int k = min(r, c); k >= 3; --k)
        {
            if (f(k))
            {
                ans = k;
                break;
            }
        }
        printf("Case #%d: ", TT, ans);
        if (ans == -1)
                    printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }

    return 0;
}