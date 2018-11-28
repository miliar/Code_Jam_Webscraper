#include <cstdio>

inline int get(void) {
    int x;
    scanf("%d\n", &x);
    return x;
}

bool solve(void) {
    int n = get();
    int k = get();
    bool res = true;
    for (int i = 0; i < n; i++) {
        if (!(k & (1 << i))) {
            res = false;
            break;
        }
    }
    return res;
}

int main(void) {
    int t = get();
    for (int tests = 1; tests <= t; tests++) {
        if (solve()) {
            printf("Case #%d: ON\n", tests);
        } else {
            printf("Case #%d: OFF\n", tests);
        }
    }
    return 0;
}
