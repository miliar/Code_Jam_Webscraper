#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<string>
#include<cctype>
#include<climits>
#include<algorithm>
#include<complex>
#include<vector>
#include<queue>
#include<set>
#include<map>

using namespace std;

typedef long long LL;

const int MaxN = 1000 + 5;

int T, N, W, L;

struct Node {
    int r, lab;
    void load(int _lab) {
        scanf("%d", &r);
        lab = _lab;
    }
    bool operator < (const Node &t) const {
        return r > t.r;
    }
}circle[MaxN];

int ansx[MaxN], ansy[MaxN];

void check(int x, int y) {
    if (x < 0 || x > W || y < 0 || y > L) {while (1) {}};
}

int main() {

    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    scanf("%d", &T);
    for (int te = 1; te <= T; ++te) {
        scanf("%d%d%d", &N, &W, &L);
        for (int i = 0; i < N; ++i) circle[i].load(i);
        sort(circle, circle + N);
        int ll;
        int nowup = -circle[0].r, nxtup;
        int st = 0;
        while (st < N) {
            int cnt = circle[st].r;
            nxtup = nowup + 2 * circle[st].r;
            int fi = st;
            ll = circle[st].lab; 
            ansy[ll] = nowup + circle[st].r;
            ansx[ll] = 0;
            check(ansx[ll], ansy[ll]);
            while (fi + 1 < N && cnt + circle[fi + 1].r <= W) {
                fi++; 
                ll = circle[fi].lab; 
                ansy[ll] = nowup + circle[fi].r;
                if (ansy[ll] < 0) ansy[ll] = 0;
                if (ansy[ll] < 0) ansy[ll] = 0;
                ansx[ll] = cnt + circle[fi].r;
                check(ansx[ll], ansy[ll]);
                cnt += 2 * circle[fi].r;
            }
            st = fi + 1;
            nowup = nxtup;
        }
        printf("Case #%d:", te);
        for (int i = 0; i < N; ++i)
            printf(" %d %d", ansx[i], ansy[i]);
        puts("");
    }

    return 0;

}

