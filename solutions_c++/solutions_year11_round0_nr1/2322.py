#include <iostream>
using namespace std;

int fabs(int x)
{
    return x > 0 ? x : -x;
}

int main(void)
{
    int T;
    cin >> T;
    for (int loop = 1; loop <= T; loop++) {
        int n, a, b, ta, tb, t;
        scanf("%d", &n);
        a = b = 1;
        t = ta = tb = 0;
        for (int i = 0; i < n; i++) {
            char c;
            int x;
            cin >> c >> x;
            if (c == 'O') {
                int d = fabs(x - a);
                if (d > t - ta)
                    t += d - (t - ta);
                ta = ++t;
                a = x;
            } else {
                int d = fabs(x - b);
                if (d > t - tb)
                    t += d - (t - tb);
                tb = ++t;
                b = x;
            }
        }
        cout << "Case #" << loop << ": " << t << endl;
    }
    return 0;
}
