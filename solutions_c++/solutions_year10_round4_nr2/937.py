#include<iostream>
#include<cstring>
#include<cstdio>
#include<map>
#include<cstdio>
#include<queue>
using namespace std;

typedef long long LL;

const LL inf = 100000000000LL;

struct data_t {
    LL first[12], second;
} data[2050];
LL n;

void solve(LL a, LL b) {
    LL i, j;
    if (b == n) {
        for (i = 0; i < 12; i++)
            data[a].first[i] = inf;
        data[a].first[n - data[a].second]=0;
        return;
    }
    solve(a * 2 + 1, b + 1);
    solve(a * 2, b + 1);
    for (i = 0; i < 12; i++) {
        if (i > b)
            data[a].first[i] = inf;
        LL c = inf,d = inf,e = inf;
        for (j = i + 1; j >= 0; j--) {
            c = min(c, data[a * 2].first[j]);
            d = min(d, data[a * 2 + 1].first[j]);
        }
        e = c + d + data[a].second;
        c = d = inf;
        for (j = i;j >= 0; j--) {
            c = min(c, data[a * 2].first[j]);
            d = min(d, data[a * 2 + 1].first[j]);
        }
        e = min(e, c + d);
        data[a].first[i] = e;
    }
    return ;
}
void read()
{
	freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);
    LL i, j, k, l, m, o, y, z;
    scanf("%lld", &z);
    for (y = 1; y <= 100; y++);
    for (y = 1; y <= z; y++) {
        scanf("%lld", &n);
        m = 1 << n;
        for (j = n;j >= 0; j--) {
            for (i = 0; i < (1 << j); i++)
                scanf("%lld", &data[i + (1 << j)].second);
        }
        solve(1, 0);
        printf("Case #%lld: %lld\n", y, data[i].first[0]);
    }
}
int main() {
    read();
    return 0;
}
