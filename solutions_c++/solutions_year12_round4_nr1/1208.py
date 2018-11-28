#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <conio.h>
using namespace std;
#define FOR(i, a, b) for(int i=a; i<=b; i++)
#define DOW(i, a, b) for(int i=a; i>=b; i--)
#define FOREACH(it, c) for(typeof(c.begin()) it=c.begin(); it!=c.end(); it++)
#define RESET(c, val) memset(c, val, sizeof(c))

int n, test, d[10005], l[10005], pp, f[10005];
bool flag;

int main() {
    freopen("large.in", "r", stdin);
    freopen("test.out", "w", stdout);
    cin >> test;
    FOR(t, 1, test) {
        scanf("%d", &n);
        FOR(i, 1, n) scanf("%d%d", &d[i], &l[i]);
        scanf("%d", &pp);
        flag=false;
        FOR(i, 1, n) {
            if (i==1) f[i]=d[i]; else f[i]=0;
        }
        FOR(i, 1, n) {
            int j=i+1;
            while (j<=n && d[j]<=f[i]+d[i]) {
                f[j]=max(f[j], min(d[j]-d[i], l[j]));
                j++;
            }
        }
        FOR(i, 1, n) if (f[i]+d[i]>=pp) flag=true;
        if (flag) printf("Case #%d: YES\n", t);
            else printf("Case #%d: NO\n", t);
    }
    //getch();
    return 0;
}
