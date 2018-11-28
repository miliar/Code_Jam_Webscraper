#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;

const int maxn = 1000 + 10;

struct data_t {
    int to;
    long long total;
};

int R, k, N;
int g[maxn];
data_t data[maxn];

int next(int x) {
    return (x + 1) % N;
}

void prev() {
    data[0].total = 0;
    data[0].to = 0;
    while (data[0].total + g[data[0].to] <= k) {
        data[0].total = data[0].total + g[data[0].to];
        data[0].to = next(data[0].to);
        if (data[0].to == 0) {
            break;
        }
    }

    for (int i = 1; i < N; ++i) {
        data[i].total = data[i - 1].total - g[i - 1];
        data[i].to = data[i - 1].to;
        while (data[i].total + g[data[i].to] <= k) {
            data[i].total = data[i].total + g[data[i].to];
            data[i].to = next(data[i].to);
            if (data[i].to == i) {
                break;
            }
        }
    }
}

int main() {
    freopen("C.out", "w", stdout);
    int cas = 0;
    scanf("%d", &cas);
    for (int t = 0; t < cas; ++t) {
        scanf("%d %d %d", &R, &k, &N);
        for (int i = 0; i < N; ++i) {
            scanf("%d", &g[i]);
        }
        prev();
        long long ans = 0;
        int i = 0;
        while (R--) {
            ans += data[i].total;
            i = data[i].to;
        }
        printf("Case #%d: %I64d\n", t + 1, ans);
    }
    return 0;
}

