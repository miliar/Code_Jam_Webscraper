#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <set>

using namespace std;

typedef long long ll;
typedef double db;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

int T;
int ans;
int a, b;
set<int> q;

void cnt(int x) {
    q.clear();
    int c[10];
    int y = x, st = 1, k = 0;
    while (y) {
        c[k++] = y % 10;
        st *= 10;
        y /= 10;
    }
    st /= 10;
    reverse(c, c + k);
    y = x;
    forn(i, k) {
        y = (y % 10) * st + y / 10;
        c[k] = c[k - 1];
        forn(j, k) c[j + 1] = c[j];
        c[0] = c[k];
        if (c[0] != 0 && y > x && y <= b) q.insert(y);
    }
    ans += q.size();
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d", &T);
    forn(t, T) {
        scanf("%d%d", &a, &b);
        ans = 0;
        forab(i, a, b + 1) cnt(i);
        printf("Case #%d: %d\n", t + 1, ans);
    }
    return 0;
}
