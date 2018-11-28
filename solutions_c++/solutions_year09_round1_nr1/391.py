#include <stdio.h>

#define int64 long long

const int maxs = 1000 + 10;
const int maxr = 10 + 2;

int exist[maxs], flag[maxr][maxs], rank;
int r[maxr];

bool check(int s, int r)
{
    ++rank;
    while (s != 1) {
        int _s = 0;
        while (s > 0) {
            _s += (s%r)*(s%r);
            s /= r;
        }
        s = _s;
        if (flag[r][s]) return false;
        if (exist[s] == rank) {
            flag[r][s] = 1;
            return false;
        }
        exist[s] = rank;
    }
    return true;
}

int main(void)
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout); 
    rank = 0;
    int tot, cas = 0;
    scanf("%d", &tot);
    while (tot--) {
        int k = 0;
        ++cas;
        do {
            char c;
            scanf("%d", &r[k]);
            ++k;
            if (scanf("%c", &c)==-1 || c=='\n') break;
        } while (true);
        int re = 2;
        while (true) {
            int j = 0;
            while (j<k && check(re, r[j])) ++j;
            if (j == k) break;
            ++re;
        }
        printf("Case #%d: %d\n", cas, re);
    }
    return 0; 
} 
