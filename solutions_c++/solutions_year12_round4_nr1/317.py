#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

#define MAX_N 10005

int dist[MAX_N], len[MAX_N], f[MAX_N];

int main()
{
    freopen("probA.in", "r", stdin);
    int T;
    cin >> T;
    for (int __ = 0; __ < T; ++__) {
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i)
            scanf("%d%d", dist + i, len + i);
        int D;
        cin >> D;
        dist[n++] = D;
        len[n] = 0;

        memset(f, -1, sizeof(f));
        f[0] = min(dist[0], len[0]);

        for (int i = 0; i < n; ++i) {
            // printf("%d ", f[i]);
            if (f[i] == -1)
                continue;
            for (int j = i+1; j < n; ++j)
                if (f[i] + dist[i] >= dist[j])
                    f[j] = max(f[j], min(dist[j]-dist[i], len[j]));
        }
        printf("Case #%d: %s\n", __+1, f[n-1] >= 0 ? "YES" : "NO");
    }
    return 0;
}
