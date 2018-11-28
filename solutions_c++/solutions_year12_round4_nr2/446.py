#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define VAR(v,w) __typeof(w) v=(w)
#define FORE(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define PB push_back
#define MP make_pair
#define FT first
#define SD second

typedef pair<int, int> pii;
int w,l,n;
vector<pii> rs;
int rad[1000000];
pii pos[1000000];
bool used[1000000];
typedef long long int lld;

void test() {
    bool rev = false;
    scanf("%d%d%d", &n, &w, &l);
    if (w < l) {
        rev = true;
        swap(w,l);
    }
    rs.clear();

    REP(i,n) {
        int r; scanf("%d", &r);
        rad[i] = r;
        rs.PB(MP(r,i));
        used[i] = false;
    }
    sort(rs.begin(), rs.end());
    reverse(rs.begin(), rs.end());
    int x = 0, y = 0;
    int hei = rs[0].FT;
    for (int i = 0; i < n; i++) {
        pii k = rs[i];
        if (used[k.SD]) continue;        
        int rx = x + k.FT;
        if (x == 0) rx = 0;
        if (rx > w) {
            //printf("NEWROW hei %d at %d\n", hei, i);
            x = 0;
            rx = x;
            y = y + hei;
            hei = 2 * k.FT;
        }
        int ry = y + k.FT;
        int space = hei - 2*k.FT;
        if (y + hei > l) space = l - (y + 2*k.FT);
        if (y == 0) {
            ry = 0;
            space = hei - k.FT;
            if (y + hei > l) space = l - k.FT;
        }
        else {
            for (int j = i+1; j < n; j++) {
                pii dk = rs[j];
                if (used[dk.SD]) continue;
                continue;
                if (space >= 2*dk.FT) {
                    int dx = x + dk.FT;
                    int dy = ry + k.FT + dk.FT;
                    pos[dk.SD] = MP(dx,dy);
                    if (dx > w) printf("BUBA st\n");
                    if (dy > l) printf("Buba yyu\n");
                    used[dk.SD] = true;
                    break;
                }
            }
        }
        pos[k.SD] = MP(rx,ry);
        if (x == 0) x += k.FT;
        else x += 2*k.FT;
//        printf("Wsadzone %d\n", k.SD);
        if (rx > w) printf("Nietak! %d %d %d\n", i, rx, w);
        if (ry > l) printf("BUBA tutaj\n");
    }
    if (rev) {
        REP(i,n) swap(pos[i].FT,pos[i].SD);
        swap(w,l);
    }
//    REP(i,n) {
//        if (pos[i].FT < 0 || pos[i].FT > w) {
//            printf("BUBA [%d] %d %d (%d)\n", i, pos[i].FT, pos[i].SD, w);
//        }
//        if (pos[i].SD < 0 || pos[i].SD > l) {
//            printf("DUPPA!\n");
//        }
//        FOR(j,i+1,n) {
//            lld xx = pos[i].FT - pos[j].FT;
//            lld yy = pos[i].SD - pos[j].SD;
//            lld dd = rad[i] + rad[j];
//            if (xx*xx + yy*yy < dd*dd) {
//                printf("STYKAJA! %d & %d\n", i, j);
//            }
//        }
//    }
    REP(i,n) printf("%d %d ", pos[i].FT, pos[i].SD);
    puts("");
}

main() {
    int z; scanf("%d", &z);
    REP(i,z) {
        printf("Case #%d: ", i+1); test();
    }
}
