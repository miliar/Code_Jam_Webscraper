#include <cstdio>

const int MAXN = 1000+3;

inline int get(void) {
    int x;
    scanf("%d", &x);
    return x;
}

int solve(void) {
    int groups[MAXN];
    int moneyFrom[MAXN];
    int next[MAXN];

    int r = get();
    int k = get();
    int n = get();
    
    for (int i = 0; i < n; i++) {
        groups[i] = get();
    }

    // could be done linear
    for (int i = 0; i < n; i++) {
        int totalPeople = 0;
        int j = i;
        for (; j - i < n; j++) {
            if (totalPeople + groups[j%n] <= k) {
                totalPeople += groups[j%n];
            } else {
                // My friend, it's been too long.
                break;
            }
        }
        moneyFrom[i] = totalPeople;
        next[i] = j % n;
    }

    unsigned long long total = 0;
    int current = 0;
    for (int i = 0; i < r; i++) {
        total += moneyFrom[current];
        current = next[current];
    }
    return total;
}

int main(void) {
    int t = get();
    for (int test = 1; test <= t; test++) {
        printf("Case #%d: %d\n", test, solve());
    }
    return 0;
}
