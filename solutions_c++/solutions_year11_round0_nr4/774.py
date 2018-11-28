#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 1005;

int n;
int s[MAXN];

int main() {
    int t, casN = 0;
    int i, cnt;

    scanf("%d", &t);
    while (t-- > 0) {
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%d", &s[i]);
        }
        cnt = 0;
        for (i = 0; i < n; i++) {
            if (s[i] != i + 1) cnt++;
        }
        printf("Case #%d: %.6f\n", ++casN, (double)cnt);
    }

    return 0;
}

