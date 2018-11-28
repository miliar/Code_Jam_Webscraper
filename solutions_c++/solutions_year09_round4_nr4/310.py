#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define sqr(x) ((x) * (x))

int main()
{
    int c;
    cin >> c;
    for (int caseNum = 1; caseNum <= c; caseNum++)
    {
        int n;
        cin >> n;

        int x[n], y[n], r[n];
        for (int i = 0; i < n; i++)
            cin >> x[i] >> y[i] >> r[i];

        double ans;
        if (n == 1)
        {
            ans = r[0];
        }
        else if (n == 2)
        {
            ans = max(r[0], r[1]);
        }
        else if (n == 3)
        {
            ans = -1;
            for (int i = 0; i < 3; i++)
                for (int j = 0; j < i; j++)
                {
                    double a = sqrt(sqr(x[i] - x[j]) + sqr(y[i] - y[j])) + r[i] + r[j];
                    int l = 3 - i - j;
                    a = max(a / 2, (double) r[l]);
                    if (ans < 0 || a < ans)
                        ans = a;
                }
        }
        else
        {
            assert(false);
            ans = -1;
        }

        printf("Case #%d: %.6f\n", caseNum, ans);
    }
    return 0;
}
