#include <stdio.h>
#include <memory.h>
#include <map>
#include <algorithm>

using namespace std;

int n = 0, m = 0;

struct tt
{
    long long v[64];
    bool operator < (const tt &o) const
    {
        int i = 0;
        for (i = 0; i < n; i ++) {
            if (v[i] != o.v[i]) {
                return v[i] < o.v[i];
            }
        }
        return false;
    }
    bool operator == (const tt &o) const
    {
        int i = 0;
        for (i = 0; i < n; i ++) {
            if (v[i] != o.v[i]) {
                return false;
            }
        }
        return true;
    }
    void p()
    {
        printf("-------------------\n");
        int i = 0, j = 0;
        for (i = 0; i < n; i ++) {
            for (j = 0; j < m; j ++) {
                if (v[i] & (1LL << j)) {
                    printf("1");
                }
                else {
                    printf("0");
                }
            }
            printf("\n");
        }
        printf("-------------------\n");
    }
}now, our, ans, ll[1<<20];

map<tt, bool> my;

int kk[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int lx[4000] = { 0 }, ly[4000] = { 0 };

int bfs(int x, int y)
{
    int p = 0, q = 0, k = 0, xx = 0, yy = 0;

    memset(&now, 0, sizeof(now));
    now.v[x] |= 1LL << y;
    p = q = 0;
    lx[q] = x;
    ly[q] = y;
    q ++;
    while (p < q) {
        for (k = 0; k < 3; k ++) {
            xx = lx[p] + kk[k][0];
            yy = ly[p] + kk[k][1];
            if (our.v[xx] & (1LL << yy)) {
                if (now.v[xx] & (1LL << yy)) {
                    continue;
                }
                now.v[xx] |= 1LL << yy;
                lx[q] = xx;
                ly[q] = yy;
                q ++;
            }
        }
        p ++;
    }
    return q;
}



bool judge()
{
    int p = 0, q = 0, i = 0;

    my.clear();
    p = q = 0;
    ll[q ++] = now;
    my[now] = true;
    while (p < q) {
        //ll[p].p();
        if (ll[p] == ans) {
            return true;
        }
        //memset(ll + q, 0, sizeof(tt));
        for (i = 0; i < n; i ++) {
            ll[q].v[i] = ((ll[p].v[i] << 1) & our.v[i]) | (((~our.v[i]) >> 1) & ll[p].v[i]);
            if ((ll[q].v[i] & now.v[i]) != ll[q].v[i]) {
                break;
            }
        }
        if (i == n) {
            if (!my[ll[q]]) {
                my[ll[q]] = true;
                q ++;
            }
        }
        //memset(ll + q, 0, sizeof(tt));
        for (i = 0; i < n; i ++) {
            ll[q].v[i] = ((ll[p].v[i] >> 1) & our.v[i]) | (((~our.v[i]) << 1) & ll[p].v[i]);
            if ((ll[q].v[i] & now.v[i]) != ll[q].v[i]) {
                break;
            }
        }
        if (i == n) {
            if (!my[ll[q]]) {
                my[ll[q]] = true;
                q ++;
            }
        }
        //memset(ll + q, 0, sizeof(tt));
        //ll[q].v[0] = 0;
        for (i = 0; i < n; i ++) {
            ll[q].v[i] = (i > 0 ? (ll[p].v[i - 1] & our.v[i]) : 0) | (i + 1 < n ? (ll[p].v[i] & (~our.v[i+1])) : ll[p].v[i]);
            if ((ll[q].v[i] & now.v[i]) != ll[q].v[i]) {
                break;
            }
        }
        if (i == n) {
            if (!my[ll[q]]) {
                my[ll[q]] = true;
                q ++;
            }
        }
        p ++;
    }
    return false;
}

char str[64][64] = { 0 };

int main()
{
    int c = 0, o = 0, i = 0, j = 0, k = 0;
    
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);

    scanf("%d", &c);
    for (o = 1; o <= c; o ++) {
        scanf("%d%d", &n, &m);
        memset(&our, 0, sizeof(our));
        for (i = 0; i < n; i ++) {
            scanf("%s", str[i]);
            for (j = 0; j < m; j ++) {
                if (str[i][j] != '#') {
                    our.v[i] |= 1LL << j;
                }
            }
        }
        printf("Case #%d:\n", o);
        for (k = 0; k < 10; k ++) {
            for (i = 0; i < n; i ++) {
                for (j = 0; j < m; j ++) {
                    if (str[i][j] == '0' + k) {
                        memset(&ans, 0, sizeof(ans));
                        ans.v[i] |= 1LL << j;
                        printf("%d: %d ", k, bfs(i, j));
                        if (judge()) {
                            printf("Lucky\n");
                        }
                        else {
                            printf("Unlucky\n");
                        }
                    }
                }
            }
        }
    }
    return 0;
}
