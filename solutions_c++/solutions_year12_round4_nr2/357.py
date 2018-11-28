#include <vector>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <bitset>
#include <complex>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;

const int maxn = 1024;
const int INF = 1 << 30;

int id[maxn], r[maxn], n;
int w, h;

bool cmp(int x, int y) {
    return r[x] > r[y];
}

int ansx[maxn], ansy[maxn];

void main2() {
    scanf("%d%d%d", &n, &w, &h);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &r[i]);
    }
    for (int i = 0; i < n; ++i) {
        id[i] = i;
    }
    sort(id, id + n, cmp);
    int top = -INF;
    int rig = -INF;
    int ptr = 0;
    while (ptr < n) {
        int cury;
        int k = id[ptr];
        if (top == -INF) {
            ansx[k] = 0;
            ansy[k] = cury = 0;
            rig = r[k];
            top = r[k];
        } else {
            ansx[k] = 0;
            ansy[k] = cury = top + r[k];
            rig = r[k];
            top = top + r[k] * 2;
        }
        ptr++;
        while (ptr < n && rig + r[id[ptr]] <= w) {
            k = id[ptr];
            ansx[k] = rig + r[k];
            ansy[k] = cury;
            rig = ansx[k] + r[k];
            ptr++;
        }
    }

    for (int i = 0; i < n; ++i) {
        printf(" %d %d", ansx[i], ansy[i]);
    }
    printf("\n");
}

int main() {
    //freopen("B.in", "r", stdin);
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small-attempt0.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, ca = 0;
    for (scanf("%d", &T); T--; ) {
        printf("Case #%d:", ++ca);
        main2();
    }
}

