#define __STDC_FORMAT_MACROS
#include <inttypes.h>
#include <stdint.h>

#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>
using namespace std;
typedef int64_t ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

const int N = 1000;
struct Type { double p; int t, id; } a[N];

bool cmp(const Type& x, const Type& y)
{
    return x.p > y.p || x.p == y.p && x.id < y.id;
}

int main()
{
    int cases, N;
    scanf("%d", &cases);
    for (int T = 1; T <= cases; T++) {
        int N;
        scanf("%d", &N);
        for (int i = 0; i < N; i++)
            scanf("%*d", &a[i].t), a[i].id = i;
        for (int i = 0; i < N; i++)
            scanf("%lf", &a[i].p);
        sort(a, a+N, cmp);
        printf("Case #%d:", T);
        for (int i = 0; i < N; i++)
            printf(" %d", a[i].id);
        puts("");
    }
}
