#include <iostream>

using namespace std;

typedef long long LL;
const int MAXN = 2000020;
bool vist[MAXN];

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int nCase, A, B;
    scanf("%d", &nCase);
    for (int tCase = 1; tCase <= nCase; ++tCase) {
        scanf("%d %d", &A, &B);
        memset(vist, false, B - A + 1);
        LL ans = 0;
        for (int n = A; n <= B; ++n) {
            if (vist[n-A]) continue;
            vist[n-A] = true;
            LL c = 1, tl = n; char s1[24];
            sprintf(s1, "%d", n);
            int len = strlen(s1);
            for (int i = 0; i < len; ++i) {
                s1[len+i] = s1[i];
            }
            s1[len * 2] = 0;
            //puts(s1);
            int v;
            for (int i = 1; i < len; ++i) {
                char ch = s1[i + len];
                s1[i + len] = 0;
                sscanf(s1 + i, "%d", &v);
                //printf("%d %d ", v, vist[v-A]);
                if (v >= A && v <= B && !vist[v-A]) {
                      vist[v-A] = true; ++c;
                }
                //puts("");
                s1[i + len] = ch;
            }
            //printf("%d\n", c);
            ans += c * (c - 1) / 2;
        }
        printf("Case #%d: %lld\n", tCase, ans);
    }
    return 0;
} 
