#include<sstream>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)
int n, l, h;
int a[200000];

int main() {
    int cas;
    scanf("%d", &cas);
    for (int tt = 0; tt < cas; tt++) {
        scanf("%d%d%d", &n, &l, &h);
        rep(i, n) scanf("%d", &a[i]);
        int res = -1;
        for (int i = l; i <= h; i++) {
            int ok = 1;
            rep(j, n) if (a[j] % i == 0 || i % a[j] == 0) {} else ok = 0;
            if (ok) {
                res = i;
                break;
            }
        }
        printf("Case #%d: ", tt + 1);
        if (res < 0) puts("NO"); else printf("%d\n", res);

    }
    return 0;
}
