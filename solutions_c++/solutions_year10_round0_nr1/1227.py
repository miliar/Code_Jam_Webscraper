#include <stdlib.h>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef unsigned int ui;

#define LET(k, val) typeof(val) k = (val)
#define FOR(k, a, b) for (typeof(a) k = (a); k < (b); ++k)
#define SIZE(x) ((int)(x).size())

int main() {
    int t, n, k;
    ui snappers = 0;

    scanf("%d\n", &t);
    FOR(i, 0, t) {
        scanf("%d %d\n", &n, &k);
        snappers = 0;

        int a = 1 << n;
        int b = k % a;

        printf("Case #%d: %s\n", i + 1, (b == a - 1) ? "ON" : "OFF");
    }

    return 0;
}

