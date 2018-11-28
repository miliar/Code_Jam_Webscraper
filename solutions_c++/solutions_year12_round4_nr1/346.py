#include <iostream>
#include <stdio.h>
#define N 10000

using namespace std;

int d[N], l[N], f[N];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cases = 1; cases <= T; cases++) {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf("%d%d", &d[i], &l[i]), f[i] = 0;
        int D;
        scanf("%d", &D);
        f[0] = d[0];
        for (int i = 0; i < n; i++) {
            if (!f[i]) break;
            for (int j = i + 1; j < n; j++)
                if (d[i] + f[i] >= d[j]) f[j] = max(f[j], min(l[j], d[j] - d[i]));
                else break;
        }
        bool flag = false;
        for (int i = n - 1; i >= 0; i--)
            if (d[i] + f[i] >= D) {
                flag = true;
                break;
            }
        if (flag) printf("Case #%d: YES\n", cases);
        else printf("Case #%d: NO\n", cases);
    }
    return 0;
}
