#include <iostream>
#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    freopen("A.in", "r", stdin);
    //freopen("smth.txt", "r", stdout);
    int t;
    cin >> t;
    for (int q = 1; q <= t; ++q)
    {
        int a, b;
        cin >> a >> b;
        vector<double> p(a + 1);
        for (size_t i = 1; i <= a; ++i)
        {
            cin >> p[i];
        }
        cout.setf(ios::fixed,ios::floatfield);
        if (b == a)
        {
            //enter
            double res = 1;
            cout.precision(6);
            cout << "Case #" << res << ": " << res << endl;
            continue;
        }
        double enter_now = (double)b + 2;
        double k, b1, b2, b3, res;
        if (a == 1)
        {
            k = p[1] * (b - a + 1) + (1 - p[1]) * (b - a + 1 + b + 1);
            res = k;
        }
        if (a == 2)
        {
            k =
                    p[1] * p[2] * (b - a + 1) +
                    (1 - p[1] * p[2]) * (b - a + 1 + b + 1);
            b1 =
                    p[1] * (b - a + 1 + 2) +
                    (1 - p[1]) * (b - a + 1 + 2 + b + 1);
            res = min(k, b1);
        }
        if (a == 3)
        {
            k =
                    p[1] * p[2] * p[3] * (b - a + 1) +
                    (1 - p[1] * p[2] * p[3]) * (b - a + 1 + b + 1);
            b1 =
                    p[1] * p[2] * (b - a + 1 + 2) +
                    (1 - p[1] * p[2]) * (b - a + 1 + 2 + b + 1);
            b2 =
                    p[1] * (b - a + 1 + 2 + 2) +
                    (1 - p[1]) * (b - a + 1 + 2 + 2 + b + 1);
            res = min(k, min(b1, b2));
        }
        res = min(res, enter_now);
        cout.precision(6);
        cout << "Case #" << q << ": " << res << endl;
    }
    return 0;
}
