#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

#define REP(i,n) for (int i = 0; i < (int)n; ++i)
#define FOR(i,c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)

using namespace std;

int main(void)
{
    int nCase;
    int N, K;

    scanf("%d", &nCase);
    REP(c, nCase) {
        scanf("%d %d", &N, &K);

        int base = (1 << N) - 1;

        bool on_off = (K % (base+1)) == base;

        printf("Case #%d: %s\n", c+1, (on_off ? "ON" : "OFF"));
    }

    return 0;
}
