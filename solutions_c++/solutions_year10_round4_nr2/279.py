#include <cstdio>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int p;
vector<int> m;
vector<int> costs;

int main(void) {
    int T;
    scanf("%d", &T);
    for (int testNo = 1; testNo <= T; testNo++) {
        printf("Case #%d: ", testNo);
        scanf("%d", &p);
        m.resize(1<<p);
        costs.resize((1<<p));
        for (int i = 0; i < (1<<p); i++) {
            scanf("%d", &m[i]);
        }
        for (int offset = 1<<(p-1); offset != 0; offset /= 2) {
            for (int i = offset; i != offset + offset; i++) {
                scanf("%d", &costs[i]);
            }
        }
        const long long INF = LLONG_MAX / 3;
        vector< vector<long long> > res(2<<p, vector<long long>(p+1, INF));
        for (int i = 0; i < (1<<p); i++) {
            for (int j = 0; j <= m[i]; j++)
                res[(1<<p) + i][j] = 0;
        }
        for (int i = (1<<p) - 1; i != 0; i--) {
            for (int j = 0; j <= p; j++) {
                res[i][j] = min(res[i][j], costs[i] + res[i * 2][j] + res[i * 2 + 1][j]);
                if (j != p)
                    res[i][j] = min(res[i][j], res[i * 2][j + 1] + res[i * 2 + 1][j + 1]);
            }
        }
        printf("%lld\n", res[1][0]);
    }
    return 0;
}
