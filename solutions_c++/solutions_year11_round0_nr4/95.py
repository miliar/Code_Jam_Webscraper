#include <cstdio>
using namespace std;

int main()
{
    int cases, n, a[1992];
    bool flag[1992];
    scanf("%d", &cases);
    for (int T = 1; T <= cases; T++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%d", &a[i]), a[i]--, flag[i] = false;
        int res = 0;
        for (int i = 0; i < n; i++)
            if (!flag[i]) {
                int j = i, cnt = 0;
                while (!flag[j]) {
                    flag[j] = true;
                    cnt++;
                    j = a[j];
                }
                if (cnt > 1) res += cnt;
            }
        printf("Case #%d: %d.000000\n", T, res);
    }
}
