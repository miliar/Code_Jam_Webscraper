#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int T, n, k;
    scanf("%d", &T);
    for (int tt = 1; tt <= T; ++tt) {
        scanf("%d%d", &n, &k);
        bool ok = true;
        for (int i = 0; i < n; ++i)
            if (!(k & (1 << i))) {
                ok = false;
                break;
            }
        if (ok) printf("Case #%d: ON\n", tt);
        else printf("Case #%d: OFF\n", tt);
    }
    return 0;
}
