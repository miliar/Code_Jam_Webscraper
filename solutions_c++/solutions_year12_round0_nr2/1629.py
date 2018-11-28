#include <iostream>

using namespace std;


int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int nCase, S, p, ti[128], N;
    scanf("%d", &nCase);
    for (int tCase = 1; tCase <= nCase; ++tCase) {
        scanf("%d %d %d", &N, &S, &p);
        for (int i = 0; i < N; ++i) {
            scanf("%d", &ti[i]);
        }
        int c = 0;
        for (int i = 0; i < N; ++i) {
            if ((ti[i] + 2) / 3 >= p) ++c;
            else if (ti[i] >= 2 && ti[i] <= 28 && S && (ti[i] + 4) / 3 >= p) ++c, --S;
        }
        printf("Case #%d: %d\n", tCase, c);
    }
    return 0;
} 
