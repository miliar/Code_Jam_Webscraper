
#include <set>
#include <map>
#include <queue>
#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAX_R = 12 + 5;
const int MAX_C = 12 + 5;
const int MAX_B = 5 + 5;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

struct pnt {
    int r;
    int c;
    
    pnt() {}
    
    pnt(int r, int c) {
        this->r = r;
        this->c = c;
    }
    
    inline bool operator <(const pnt &rhs) const {
        if (r != rhs.r)
            return r < rhs.r;
        return c < rhs.c;
    }
};

struct state {
    vector <pnt> box;
    int dist;
    
    state() {}
    
    state(vector <pnt> box, int dist) {
        this->box = box;
        this->dist = dist;
    }
    
    inline bool operator <(const state &rhs) const {
        return dist > rhs.dist;
    }
};

int R, C;
char grid[MAX_R][MAX_C];

set <vector <pnt> > done;
priority_queue <state> pq;
map <vector <pnt>, int> best;
map <vector <pnt>, bool> cache;

void read() {
    scanf("%d %d", &R, &C);
    for (int r = 0; r < R; ++r)
        scanf("%s", grid[r]);
}

inline void push(vector <pnt> box, int dist) {
    sort(box.begin(), box.end());
    for (int i = 1; i < (int) box.size(); ++i)
        if (box[i - 1].r == box[i].r && box[i - 1].c == box[i].c)
            return;
    if (!best.count(box) || best[box] > dist) {
        best[box] = dist;
        pq.push(state(box, dist));
    }
}

inline bool valid(int r, int c) {
    return r >= 0 && r < R && c >= 0 && c < C && grid[r][c] != '#';
}

inline bool contain(int r, int c, vector <pnt> &box) {
    for (int i = 0; i < (int) box.size(); ++i)
        if (box[i].r == r && box[i].c == c)
            return true;
    return false;
}

inline bool stable(vector <pnt> pnts) {
    sort(pnts.begin(), pnts.end());
    int n = pnts.size();
    for (int i = n - 1; i >= 0; --i) {
        pnts[i].r -= pnts[0].r;
        pnts[i].c -= pnts[0].c;
    }
    if (cache.count(pnts))
        return cache[pnts];
    
    static bool mark[MAX_B];
    memset(mark, 0, sizeof(mark));
    queue <pnt> q;
    q.push(pnts[0]);
    mark[0] = true;
    while (!q.empty()) {
        pnt p = q.front();
        q.pop();
        for (int i = 0; i < n; ++i)
            if (!mark[i]) {
                int dr = pnts[i].r - p.r;
                int dc = pnts[i].c - p.c;
                if (abs(dr) + abs(dc) == 1) {
                    mark[i] = true;
                    q.push(pnts[i]);
                }
            }
    }
    for (int i = 0; i < n; ++i)
        if (!mark[i])
            return cache[pnts] = false;
    return cache[pnts] = true;
}

int solve() {
    done.clear();
    best.clear();
    cache.clear();
    while (!pq.empty())
        pq.pop();
    
    vector <pnt> src;
    for (int r = 0; r < R; ++r)
        for (int c = 0; c < C; ++c)
            if (grid[r][c] == 'o' || grid[r][c] == 'w') {
                src.push_back(pnt(r, c));
            }
    push(src, 0);
    while (!pq.empty()) {
        state s = pq.top();
        pq.pop();
        vector <pnt> cbox = s.box;
        int cdist = s.dist;
        if (done.count(cbox))
            continue;
        done.insert(cbox);
        bool final = true;
        for (int i = 0; i < (int) cbox.size(); ++i)
            if (grid[cbox[i].r][cbox[i].c] != 'w' && grid[cbox[i].r][cbox[i].c] != 'x') {
                final = false;
                break;
            }
        if (final)
            return cdist;
        for (int id = 0; id < (int) cbox.size(); ++id)
            for (int dir = 0; dir < 4; ++dir) {
                int pr = cbox[id].r - dr[dir];
                int pc = cbox[id].c - dc[dir];
                int nr = cbox[id].r + dr[dir];
                int nc = cbox[id].c + dc[dir];
                if (!valid(pr, pc) || !valid(nr, nc) || contain(pr, pc, cbox) || contain(nr, nc, cbox))
                    continue;
                cbox[id].r += dr[dir];
                cbox[id].c += dc[dir];
                if (stable(cbox))
                    push(cbox, cdist + 1);
                for (int id2 = 0; id2 < (int) cbox.size(); ++id2)
                    for (int dir2 = 0; dir2 < 4; ++dir2) {
                        int pr2 = cbox[id2].r - dr[dir2];
                        int pc2 = cbox[id2].c - dc[dir2];
                        int nr2 = cbox[id2].r + dr[dir2];
                        int nc2 = cbox[id2].c + dc[dir2];
                        if (!valid(pr2, pc2) || !valid(nr2, nc2) || contain(pr2, pc2, cbox) || contain(nr2, nc2, cbox))
                            continue;
                        cbox[id2].r += dr[dir2];
                        cbox[id2].c += dc[dir2];
                        if (stable(cbox))
                            push(cbox, cdist + 2);
                        cbox[id2].r -= dr[dir2];
                        cbox[id2].c -= dc[dir2];
                    }
                cbox[id].r -= dr[dir];
                cbox[id].c -= dc[dir];
            }
    }
    return -1;
}

int main() {
    int tst;
    scanf("%d", &tst);
    for (int cas = 0; cas < tst; ++cas) {
        read();
//        fprintf(stderr, "Case #%d..\n", cas + 1);
//        fflush(stderr);
        printf("Case #%d: %d\n", cas + 1, solve());
    }
    return 0;
}