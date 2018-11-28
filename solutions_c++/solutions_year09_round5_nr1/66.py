// Powered by FTH

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iterator>
#include <functional>
#include <utility>
#include <numeric>
#include <complex>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) ((c).begin()), ((c).end())

#define N 16
#define W 8

typedef unsigned long long int state_t;
#define DANGER_BIT (1ull << 63)
typedef bool field_t[N][N];

int n;
field_t field;
state_t start, goal;

int ADJ[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};

int count_connected(field_t& f, int i, int j) {
    if (!f[i][j])
        return 0;
    f[i][j] = false;
    int c = 1;
    REP(dir, 4) {
        int di = ADJ[dir][0], dj = ADJ[dir][1];
        c += count_connected(f, i+di, j+dj);
    }
    return c;
}
inline bool is_danger(const field_t& f) {
    REP(si, N) REP(sj, N) {
        if (f[si][sj]) {
            field_t ff;
            memcpy(ff, f, sizeof(field_t));
            return (count_connected(ff, si, sj) < n);
        }
    }
    return false;
}
inline void field_to_state(const field_t& f, state_t& s) {
    s = 0;
    REP(i, N) REP(j, N) {
        if (f[i][j]) {
            int k = i * N + j;
            s = (s << W) + k;
        }
    }
    if (is_danger(f))
        s |= DANGER_BIT;
}

inline void state_to_field(state_t s, field_t& f) {
    s &= ~DANGER_BIT;
    memset(f, 0, sizeof(f));
    while(s) {
        int k = s & ((1ull << W)-1);
        s >>= W;
        int i = k / N, j = k % N;
        f[i][j] = true;
    }
}

int solve() {
    if (start == goal)
        return 0;

    map<state_t, int> memo;
    queue<state_t> q;
    q.push(start);
    memo[start] = 0;
    while(!q.empty()) {
        const state_t cur = q.front();
        q.pop();
        const int cur_dist = memo[cur];
        field_t cur_f;
        state_to_field(cur, cur_f);

        /*
        cout << cur_dist << ": " << cur << endl;
        REP(i, N) {
            REP(j, N) {
                cout << (cur_f[i][j] ? 'o' : field[i][j] ? '.' : '#');
            }
            cout << endl;
        }
        cout << endl;
        */

        REP(ci, N) REP(cj, N) if (cur_f[ci][cj]) {
            REP(dir, 4) {
                int di = ADJ[dir][0], dj = ADJ[dir][1];
                if (!cur_f[ci-di][cj-dj] && !cur_f[ci+di][cj+dj] && field[ci+di][cj+dj] && field[ci-di][cj-dj]) {
                    field_t next_f;
                    memcpy(next_f, cur_f, sizeof(field_t));
                    next_f[ci][cj] = false;
                    next_f[ci+di][cj+dj] = true;
                    state_t next;
                    field_to_state(next_f, next);
                    if (cur & next & DANGER_BIT)
                        continue;
                    int next_dist = cur_dist + 1;
                    if (memo.insert(make_pair(next, next_dist)).second) {
                        if (next == goal)
                            return next_dist;
                        q.push(next);
                    }
                }
            }
        }
    }
    return -1;
}

int main() {

    int nCases;
    {
        string s;
        getline(cin, s);
        istringstream is(s);
        is >> nCases;
    }

    REP(iCase, nCases) {
        // init
        field_t start_f, goal_f;
        memset(field, 0, sizeof(field_t));
        memset(start_f, 0, sizeof(field_t));
        memset(goal_f, 0, sizeof(field_t));
        n = 0;

        // read
        int nGoals = 0;
        int nRows, nCols;
        cin >> nRows >> nCols;
        REP(i, nRows) REP(j, nCols) {
            char c;
            cin >> c;
            field[i+1][j+1] = (c != '#');
            if (c == 'o' || c == 'w') {
                start_f[i+1][j+1] = true;
                n++;
            }
            if (c == 'x' || c == 'w') {
                goal_f[i+1][j+1] = true;
                nGoals++;
            }
        }
        field_to_state(start_f, start);
        field_to_state(goal_f, goal);

        cout << "Case #" << iCase+1 << ": ";
        if (n != nGoals) {
            cout << "-1" << endl;
            continue;
        }

        cout << solve() << endl;
    }

    return 0;
}
