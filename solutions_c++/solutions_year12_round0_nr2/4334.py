#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <cctype>
#include <math.h>

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>

#include <deque>
#include <queue>
#include <map>

using namespace std;
#define maxn  1e8
#define minn -1e9
#define eps 1e-6
const int oo = 0x7f;
const int Range = 1000000;
const int Nnum = 510;

/*int cmp(const void *a, const void *b) {
    return *(double*) a - *(double*) b;
}*/

int Min(int a, int b) {
    return a > b ? b : a;
}

int Max(double a, double b) {
    return a > b ? a : b;
}

int main() {
    int i, j, k;
    int cas, n, p, s, l1, l2, cnt;
    int a[110];
    freopen("s.txt","r",stdin);
    freopen("B-small.txt","w",stdout);
    scanf("%d", &cas);
    for (k = 1; k <= cas; k++) {
        memset(a, 0, sizeof (a));
        l1 = l2 = 0;
        cnt = 0;
        scanf("%d%d%d", &n, &s, &p);
        for (i = 0; i < n; i++)
            scanf("%d", &a[i]);
        l1 = p + 2 * (p - 1);
        l2 = p + 2 * (p - 2);
        if (l1 < 0)
            l1 = 0;
        if (l2 < 0)
            l2 = 0;
        for (i = 0; i < n; i++) {
            if (a[i] >= l1)
                cnt++;
            else if (a[i] >= l2 && s) {
                if (a[i] == 0 && p > 0)
                    continue;
                cnt++;
				s--;
            }
        }
        printf("Case #%d: %d\n", k, cnt);
    }
    return 0;
}
