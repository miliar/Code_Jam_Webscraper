#include <cstdio>
#include <cstring>
#include <cmath>
#include <set>

using namespace std;

const int ten[8] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};

int count(int num, int lim) {
    int t = 10;
    int ret = 0;
    int p = (int)(log10(num));
    set<int> mark;
    while (true) {
        int a = num % t;
        int b = num / t;
        if (b == 0) break;
        int c = a * ten[p] / (t / 10) + b;
        if (num < c && c <= lim && mark.find(c) == mark.end()) {
            ret ++;
            mark.insert(c);
        }
        t *= 10;
    }
    return ret;
}

int main() {
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);

    int n;
    scanf("%d", &n);
    
    for (int i = 1; i <= n; i ++) {
        int l, r;
        scanf("%d%d", &l, &r);
        int ans = 0;
        for (int j = l; j <= r; j ++) ans += count(j, r);
        printf("Case #%d: %d\n", i, ans);
    }

    return 0;
}

