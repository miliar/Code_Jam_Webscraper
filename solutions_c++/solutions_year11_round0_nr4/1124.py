#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

#define MAX 1010

using namespace std;

int vec[MAX], vec2[MAX];
double ans[MAX];

void init() {
    int i;

    ans[0] = ans[1] = 0.0;
    for (i = 2; i < MAX; i++) {
        ans[i] = (double)i;
    }
}

int check(const int n) {
    int i, ret = 0;

    for (i = 0; i < n; i++) {
        if (vec[i] != vec2[i]) ret++;
    }

    return ret;
}

int main() {
    int t, cnt = 1, n, i;

//    freopen("D-large.in", "r", stdin);
//    freopen("D-large.out", "w", stdout);

    init();
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        for (i = 0; i < n; i++) scanf("%d", &vec[i]);
        memcpy(vec2, vec, sizeof(vec));
        sort(vec2, vec2 + n);
        printf("Case #%d: %.6lf\n", cnt++, ans[check(n)]);
    }

    return 0;
}
