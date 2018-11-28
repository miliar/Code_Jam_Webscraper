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
int n, s, p;
int ans;
int a[200];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d", &T);
    forn(t, T) {
        scanf("%d%d%d", &n, &s, &p);
        forn(i, n) scanf("%d", &a[i]);
        sort(a, a + n);
        ans = 0;
        forba(i, n, 0)
             if ((a[i] + 2) / 3 >= p) ans++;
            else
                if (s > 0 && a[i] != 0 && (a[i] + 4) / 3 >= p) {
                    ans++;
                    s--;
                }
        printf("Case #%d: %d\n", t + 1, ans);
    }
    return 0;
}
