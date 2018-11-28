
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

bool ok(vector <int>& a, vector <int>& b) {
    for (int i = 0; i < a.size(); ++i)
        if (a[i] >= b[i])
            return false;
    return true;
}

int main() {
    int tst;
    scanf("%d", &tst);
    for (int cas = 0; cas < tst; ++cas) {
        int N, K;
        scanf("%d %d", &N, &K);
        vector <vector <int> > data;
        for (int i = 0; i < N; ++i) {
            vector <int> vec;
            for (int j = 0; j < K; ++j) {
                int x;
                scanf("%d", &x);
                vec.push_back(x);
            }
            data.push_back(vec);
        }
        sort(data.begin(), data.end());
        vector <bool> good(1 << N, false);
        for (int set = 0; set < (1 << N); ++set) {
            int prev = -1;
            bool nice = true;
            for (int i = 0; i < N; ++i)
                if (((set >> i) & 1) > 0) {
                    int crnt = i;
                    if (prev >= 0 && !ok(data[prev], data[crnt])) {
                        nice = false;
                        break;
                    } else {
                        prev = crnt;
                    }
                }
            good[set] = nice;
        }
        
        vector <int> dp(1 << N, 0x3f3f3f3f);
        dp[0] = 0;
        for (int set = 1; set < (1 << N); ++set)
            for (int sset = set; true; sset = (sset - 1) & set) {
                if (good[sset])
                    if (dp[set] > dp[set ^ sset] + 1)
                        dp[set] = dp[set ^ sset] + 1;
                if (sset == 0)
                    break;
            }
        printf("Case #%d: %d\n", cas + 1, dp[(1 << N) - 1]);
    }
    return 0;
}