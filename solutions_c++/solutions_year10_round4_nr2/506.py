#include <cstdio>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <map>
#include <algorithm>
#include <vector>

#if 0
#define D(x...) fprintf(stderr, x)
#else
#define D(x...)
#endif

using namespace std;

typedef long long ll;

int solve() {
    int P;
    scanf("%d", &P);
    int teams = 1 << P;
    int misses[1024];
    for (int i = 0; i < teams; i++) {
        scanf("%d", &misses[i]);
    }
    for (int i = 0; i < P; i++) {
        int num_matches = 1 << (P - i - 1);
        for (int j = 0; j < num_matches; j++) {
            scanf("%*d");
        }
    }
    int tree[10][512];
    memset(tree, 0, sizeof(tree));
    int cost = 0;
    for (int team = 0; team < teams; team++) {
        int k = misses[team];
        // Descend k times, then fill in the erst.
        int match = team;
        for (int i = 0; i < P; i++) {
            match >>= 1;
            if (tree[i][match]) {
                break;
            } else if (i >= k) {
                tree[i][match] = 1;
                cost++;
                D("Attending round %d, match %d for %d\n", i+1, match+1, team+1);
            }
        }
        D("Team %d done\n", team+1);
    }
    return cost;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: %d\n", i, solve());
    }
    return 0;
}
