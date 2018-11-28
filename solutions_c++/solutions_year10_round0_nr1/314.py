#include <cstdio>
#include <cstring>

using namespace std;

int test, tests;
long N, K;

void solve() {
    scanf("%ld%ld", &N, &K);
    long mask = (1 << N) - 1;

    printf("Case #%d: ", test);
    if ((K & mask) == mask)
        printf("ON\n");
    else
        printf("OFF\n");
}

int main() {
    freopen("A-large.in", "rt", stdin);
    freopen("data.out", "wt", stdout);

    scanf("%d", &tests);
    for (test = 1; test <= tests; test++)
        solve();

    return 0;
}
