#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#define MAXN 10005
using namespace std;
int n;
int can[MAXN];
int p[MAXN], l[MAXN];
int tar;

int main() {
    freopen("ain", "r", stdin);
    freopen("aout", "w", stdout);
    int cas = 1;
    int T;
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%d%d", &p[i], &l[i]);
        scanf("%d", &tar);

        memset(can, -1, sizeof (can));

        can[0] = p[0];


        for (int i = 0; i < n; i++) {
            if (can[i] != -1) {
                for (int j = i + 1; j < n; j++) {
                    if (p[j] - p[i] <= can[i]) {
                        can[j] = max(can[j], min(p[j] - p[i], l[j]));
                    } else
                        break;
                }
            }
        }

        bool ans = false;
        for (int i = n - 1; i >= 0; i--)
            if (can[i] != -1 && tar - p[i] <= can[i]) {
                ans = true;
                break;
            }
        printf("Case #%d: ", cas++);
        if (ans)puts("YES");
        else puts("NO");
    }
}