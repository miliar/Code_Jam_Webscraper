#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cassert>

using namespace std;

const int N = 10000;
const int P = 20;

int tree[N];
int miss[N];
int p;

void up(int pos, int zero_step) {
    while (zero_step) {
        pos = pos / 2;
        --zero_step;
    }
    while (pos) {
        tree[pos] = 1;
        pos = pos / 2;
    }
}
int solve_one() {
    for (int i = 0; i < (1 << p); ++i) {
        int pos = i + (1 << p);
        //printf(" %d %d\n", pos / 2, miss[i]);
        up(pos / 2, miss[i]);
    }
    /*
    for (int i = 1; i < (1 << p); ++i) {
        printf("%d ", tree[i]);
    }
    putchar('\n');
    //*/
    return count(tree + 1, tree + (1 << p), 1);
}
void solve() {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("b.small.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int tci = 1; tci <= tc; ++tci) {
        memset(tree, 0, sizeof(tree));
        scanf("%d", &p);
        for (int i = 0; i < (1 << p); ++i) {
            scanf("%d", miss + i);
        }
        for (int i = 1; i < (1 << p); ++i) {
            int t;
            scanf("%d", &t);
        }
        int ans = solve_one();
        printf("Case #%d: %d\n", tci, ans);
    }
}
int main() {
    solve();
    return 0;
}

