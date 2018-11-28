
#include <cstdio>
#include <queue>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAX_R = 10;
const int MAX_C = 6;

int R, C, F;
char map[MAX_R][MAX_C + 1];

struct state {
    int r;
    int c;
    int cset;
    int nset;
    int dist;
    
    inline bool operator <(const state &rhs) const {
        return dist > rhs.dist;
    }
};

int initial[MAX_R + 5];
priority_queue <state> pq;
int best[MAX_R][MAX_C][1 << MAX_C][1 << MAX_C];

inline bool valid(int r, int c) {
    return r >= 0 && r < R && c >= 0 && c < C;
}

inline bool get(int set, int bit) {
    return (set & (1 << bit)) > 0;
}

static void push(int r, int c, int cset, int nset, int dist) { // 0 for air
    if (!valid(r, c))
        return;
    int cnt = 0;
    while (r < R - 1) {
        if (((nset >> c) & 1) == 0) {
            cset = nset;
            nset = initial[r + 2];
            ++r;
            ++cnt;
        } else {
            break;
        }
    }
    if (cnt > F)
        return;
    if (best[r][c][cset][nset] > dist) {
        best[r][c][cset][nset] = dist;
        pq.push((state) {r, c, cset, nset, dist});
    }
}

int main() {
    int tst;
    scanf("%d", &tst);
    for (int cas = 0; cas < tst; ++cas) {
        scanf("%d %d %d", &R, &C, &F);
        memset(initial, 0, sizeof(initial));
        memset(best, 0x3f, sizeof(best));
        for (int r = 0; r < R; ++r) {
            scanf("%s", map[r]);
            int set = 0;
            for (int c = 0; c < C; ++c)
                if (map[r][c] == '#')
                    set |= 1 << c;
            initial[r] = set;
        }
        
        while (!pq.empty())
            pq.pop();
        push(0, 0, initial[0], initial[1], 0);
        int res = -1;
        while (!pq.empty()) {
            state crnt = pq.top();
            pq.pop();
            if (crnt.dist > best[crnt.r][crnt.c][crnt.cset][crnt.nset])
                continue;
            if (crnt.r == R - 1) {
                res = crnt.dist;
                break;
            }
            int r = crnt.r;
            int c = crnt.c;
            int cset = crnt.cset;
            int nset = crnt.nset;
            int dist = crnt.dist;
//            printf("(%d, %d, %d)\n", r, c, dist);
            if (valid(r, c - 1) && get(cset, c - 1) == 0)
                push(r, c - 1, cset, nset, dist);
            if (valid(r, c + 1) && get(cset, c + 1) == 0)
                push(r, c + 1, cset, nset, dist);
            if (valid(r, c - 1) && get(cset, c - 1) == 0 && valid(r + 1, c - 1) && map[r + 1][c - 1] == '#')
                push(r, c, cset, nset ^ (1 << (c - 1)), dist + 1);
            if (valid(r, c + 1) && get(cset, c + 1) == 0 && valid(r + 1, c + 1) && map[r + 1][c + 1] == '#')
                push(r, c, cset, nset ^ (1 << (c + 1)), dist + 1);
        }
        if (res >= 0)
            printf("Case #%d: Yes %d\n", cas + 1, res);
        else
            printf("Case #%d: No\n", cas + 1);
    }
    return 0;
}