#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef long long ll;
typedef double db;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

struct chel {
    int r;
    int num;

    bool operator <(const chel & a) const {
        if (r != a.r) return r < a.r;
        return num < a.num;
    }
};

int T;

int n, w, l;
chel a[1010];
int x, y, mx;
int ax[1010], ay[1010];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d", &T);
    forn(t, T) {
        scanf("%d%d%d", &n, &w, &l);
        forn(i, n) {
            scanf("%d", &a[i].r);
            a[i].num = i;
        }

        printf("Case #%d: ", t + 1);

        sort(a, a + n);
        y = l;
        mx = -a[n - 1].r;
        a[n].r = 0;
        forba(i, n, 0) {
            if (y + a[i + 1].r + a[i].r <= l) {
                y = y + a[i + 1].r + a[i].r;
            } else {
                x = mx + a[i].r;
                mx = x + a[i].r;
                y = 0;
            }
            ax[a[i].num] = x, ay[a[i].num] = y;
        }

        forn(i, n) printf("%d %d ", ax[i], ay[i]);
        printf("\n");
    }
    return 0;
}
