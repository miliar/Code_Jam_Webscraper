#include <iostream>
using namespace std;

const int mo = 100003;

long long f[505][505], c[505][505];
int t2, n;


int main()
{
    freopen("c2.in", "r", stdin);
    freopen("c2.out", "w", stdout);

    for (int i = 0; i <= 500; ++i)
        c[i][0] = 1;
    for (int i = 1; i <= 500; ++i)
        for (int j = 1; j <= i; ++j)
            c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % mo;
    f[1][0] = 1;
    for (int i = 2; i <= 500; ++i)
        for (int j = 1; j < i; ++j)
            for (int k = 0; k < j; ++k)
                f[i][j] = (f[i][j] + f[j][k] * c[i - j - 1][j - k - 1]) % mo;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        cin >> n;
        int ret = 0;
        for (int i = 1; i <= n; ++i)
            ret = (ret + f[n][i]) % mo;
        printf("Case #%d: %d\n", t1, ret);
    }


    return 0;
}
