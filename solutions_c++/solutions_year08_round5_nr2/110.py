#include <stdio.h>
#include <iostream>
#include <queue>
#include <set>
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)

const int dx[4] = { -1, 0, 1, 0 },
          dy[4] = { 0, -1, 0, 1 };

struct state {
    int r, c, pr, pc, moves;
    state(int _r, int _c, int _pr, int _pc, int _moves): 
        r(_r), c(_c), pr(_pr), pc(_pc), moves(_moves) {}
    bool operator<(state s) const {
        if (moves != s.moves) return moves > s.moves;
        if (r != s.r) return r < s.r;
        if (c != s.c) return c < s.c;
        if (pr != s.pr) return pr < s.pr;
        return pc < s.pc;
    }
};

int R, C;
bool wall[20][20];
priority_queue<state> q; set<state> seen;

bool valid(state s) {
    if (seen.find(s) != seen.end() || wall[s.r][s.c]) return false;
    return true;
}

int main() {
    FILE *fin = fopen("portal.in", "r"), *fout = fopen("portal.out", "w");

    int N; fscanf(fin, "%d", &N); REP(t, N) {
        fscanf(fin, "%d %d\n", &R, &C);
        memset(wall, true, sizeof(wall));
        int sx, sy, ex, ey; FOR(r, 1, R) {
            FOR(c, 1, C) {
                char ch; fscanf(fin, "%c", &ch);
                wall[r][c] = (ch == '#');
                if (ch == 'O') sy = r, sx = c;
                if (ch == 'X') ey = r, ex = c;
            }
            fscanf(fin, "\n");
        }

        q = priority_queue<state>(); seen.clear();
        state st = state(sy, sx, -1, -1, 0); q.push(st); seen.insert(st);

        int res = -1;
        while(!q.empty()) {
            state top = q.top(); q.pop();
            if (top.r == ey && top.c == ex) { res = top.moves; break; }

            REP(dir, 4) {
                int r = top.r, c = top.c;
                while(!wall[r+dy[dir]][c+dx[dir]]) r += dy[dir], c += dx[dir];
                state next = state(top.r, top.c, r, c, 0);
                if (valid(next)) {
                    seen.insert(next);
                    next.moves = top.moves;
                    q.push(next);
                }
            }

            REP(dir, 4) {
                int r = top.r+dy[dir], c = top.c+dx[dir];
                state next = state(r, c, top.pr, top.pc, 0);
                if (valid(next)) {
                    seen.insert(next);
                    next.moves = top.moves+1;
                    q.push(next);
                }
            }

            if (top.pr != -1) REP(dir, 4) {
                int r = top.r+dy[dir], c = top.c+dx[dir];
                if (!wall[r][c]) continue;
                state next = state(top.pr, top.pc, top.pr, top.pc, 0);
                if (valid(next)) {
                    seen.insert(next);
                    next.moves = top.moves+1;
                    q.push(next);
                }
            }
        }

        fprintf(fout, "Case #%d: ", t+1);
        if (res == -1) fprintf(fout, "THE CAKE IS A LIE\n");
        else fprintf(fout, "%d\n", res);
    }
}
