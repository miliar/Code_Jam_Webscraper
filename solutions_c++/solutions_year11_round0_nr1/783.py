#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 105;

int n;
int r[MAXN];
int p[MAXN];

int main() {
    int t, casN = 0, i, j, np;
    char buf[5];
    int curr[2];
    int cnt;

    scanf("%d", &t);
    while (t-- > 0) {
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%s%d", buf, &p[i]);
            r[i] = ((buf[0] == 'O') ? 0 : 1);
        }
        cnt = 0;
        curr[0] = curr[1] = 1;
        for (i = 0; i < n; i++) {
            for (j = i + 1; j < n; j++) {
                if (r[j] != r[i]) break;
            }
            if (j < n) np = p[j];
            else np = curr[r[i] ^ 1];
            while (curr[r[i]] != p[i]) {
                if (curr[r[i]] < p[i]) curr[r[i]]++;
                else curr[r[i]]--;
                if (curr[r[i] ^ 1] < np) curr[r[i] ^ 1]++;
                else if (curr[r[i] ^ 1] > np) curr[r[i] ^ 1]--;
                cnt++;
            }
            if (curr[r[i] ^ 1] < np) curr[r[i] ^ 1]++;
            else if (curr[r[i] ^ 1] > np) curr[r[i] ^ 1]--;
            cnt++;
        }
        printf("Case #%d: %d\n", ++casN, cnt);
    }

    return 0;
}

