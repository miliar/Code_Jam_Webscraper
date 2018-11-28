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

int T;

int n;

struct hren {
    int l, p, num;

    hren() {l = p = num = 0;}
    hren(int _l, int _p, int _num) {l = _l, p = _p, num = _num;}

    bool operator <(const hren & a) const {
        if (p != a.p) return p > a.p;
        if (p != 0 && l != a.l) return l < a.l;
        return num < a.num;
    }
};

hren h[1010];
int x;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d ", &T);
    forn(t, T) {
        scanf("%d", &n);
        forn(i, n) {
            scanf("%d", &x);
            h[i] = hren(x, 0, i);
        }
        forn(i, n) {
            scanf("%d", &x);
            h[i].p = x;
        }

        printf("Case #%d: ", t + 1);

        sort(h, h + n);
        forn(i, n) printf("%d ", h[i].num);
        printf("\n");
    }
    return 0;
}
