#include <iostream>
using namespace std;

int len = 200;

bool a[205][205], b[205][205];
int n;

int main()
{
    freopen("c1.in", "r", stdin);
    freopen("c1.out", "w", stdout);

    int t2; cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        cin >> n;
        memset(a, 0, sizeof(a));
        while (n--) {
            int x1, y1, x2, y2;
            cin >> x1 >> y1 >> x2 >> y2;
            for (int i = x1; i <= x2; ++i)
                for (int j = y1; j <= y2; ++j)
                    a[i][j] = true;
        }
        int ret = 0;
        do {
            bool ok = false;
            for (int i = 1; i <= len; ++i)
                for (int j = 1; j <= len; ++j) {
                    b[i][j] = a[i][j];
                    if (a[i][j] && !a[i - 1][j] && !a[i][j - 1])
                        b[i][j] = false;
                    if (!a[i][j] && a[i - 1][j] && a[i][j - 1])
                        b[i][j] = true;
                    if (b[i][j]) ok = true;
                }
            for (int i = 1; i <= len; ++i)
                for (int j = 1; j <= len; ++j)
                    a[i][j] = b[i][j];
            ++ret;
            if (!ok) break;
        }while (1);
        printf("Case #%d: %d\n", t1, ret);
        
    }

    return 0;
}
