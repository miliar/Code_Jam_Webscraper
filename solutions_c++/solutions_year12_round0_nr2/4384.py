#include <cstdio>
#include <algorithm>
using namespace std;

int main () {
    int q;
    scanf("%d", &q);
    for (int b = 1; b <= q; b++) {
        int n, p, s;
        scanf("%d%d%d", &n, &s, &p);
            int nn = 0, nt = 0, tn = 0, tt = 0;
        for (int a = 0; a < n; a++) {
            int t;
            scanf("%d", &t);
            int ns = 0, ts = 0;
            for (int i = 0; i <= 10; i++)
            for (int j = 0; j <= 10; j++)
            for (int k = 0; k <= 10; k++) {
                int maxi = max(i, max(j, k));
                int mini = min(i, min(j, k));
                if (i + j + k == t && maxi >= p && mini + 2 == maxi) ts = 1;
                if (i + j + k == t && maxi >= p && maxi - mini <= 1) ns = 1;
            }
            nn += (!ts && !ns);
            nt += (!ts && ns);
            tn += (ts && !ns);
            tt += (ts && ns);
        }
        printf("Case #%d: %d\n", b, nt + tt + min(s, tn));
    }
    return 0;
}
