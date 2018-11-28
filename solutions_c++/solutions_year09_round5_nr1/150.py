#include <cstdio>
#include <cstring>
#include <algorithm>
#include <deque>
#include <vector>
using namespace std;
#define maxm 5
#define maxn 16
char maze[maxn][maxn];
struct State {
    pair<int, int>p[maxm];
    int count;
    bool isStable;
    State() {
        count = 0;
    }
    void add(const pair<int, int>&o) {
        p[count++] = o;
    }
    void sort() {
        std::sort(p, p + count);
    }
    void calcStable() {
        isStable = true;
        if (count == 1) return;
        for (int i = 0; i < count; ++i) {
            bool found = false;
            for (int j = 0; j < count; ++j) {
                if (i == j) continue;
                int a = abs(p[i].first - p[j].first);
                int b = abs(p[i].second - p[j].second);
                if (a == 1 && b == 0 || a == 0 && b == 1) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                isStable = false;
                return;
            }
        }
    }
    friend bool operator == (const State &a, const State &b) {
        for (int i = 0; i < a.count; ++i) {
            if (a.p[i] != b.p[i]) return false;
        }
        return true;
    }
};
int n, m, nm;
int dir[4][2] = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
bool judge(int x, int y) {
    if (x < 0 || y < 0 || x >= n || y >= m) return false;
    return (maze[x][y] == '.');
}
deque<State>que;
#define MOD 10009
vector<State>table[MOD];
bool isVisit(State &s, int &hash) {
    hash = 0;
    for (int i = 0; i < s.count; ++i) {
        hash = hash * m + s.p[i].first;
        hash = hash * nm + s.p[i].second;
    }
    hash &= 0x7FFFFFFF;
    hash %= MOD;
    for (int i = 0; i < table[hash].size(); ++i) {
        if (s == table[hash][i]) return true;
    }
    return false;
}
int main() {
    int t;
    scanf("%d", &t);
    for (int kase = 1; kase <= t; ++kase) {
        for (int i = 0; i < MOD; ++i) {
            table[i].clear();
        }
        scanf("%d%d", &n, &m);
        nm = n * m;
        State src, tar;
        for (int i = 0; i < n; ++i) {
            scanf("%s", maze[i]);
            for (int j = 0; maze[i][j]; ++j) {
                if (maze[i][j] == 'o') {
                    src.add(make_pair(i, j));
                    maze[i][j] = '.';
                } else if (maze[i][j] == 'x') {
                    tar.add(make_pair(i, j)); 
                    maze[i][j] = '.';
                } else if (maze[i][j] == 'w') {
                    src.add(make_pair(i, j));
                    tar.add(make_pair(i, j)); 
                    maze[i][j] = '.';
                }
            }
        }
        src.sort();
        tar.sort();
        src.calcStable();
        tar.calcStable();
        if (src == tar) {
            printf("Case #%d: 0\n", kase);
            continue;
        }
        int ans = 0;
        bool ok = false;
        que.clear();
        que.push_back(src);
        while (!que.empty()) {
            int sz = que.size();
            ans++;
            while (sz--) {
                State cur = que.front();
                que.pop_front();
                for (int i = 0; i < cur.count; ++i) {
                    maze[cur.p[i].first][cur.p[i].second] = 'o';
                }
  /*              for (int i = 0; i <n; ++i) {
                    puts(maze[i]);
                }
                puts("");*/
                for (int i = 0; i < cur.count; ++i) {
                    for (int j = 0; j < 4; ++j) {
                        State nxt = cur;
                        int x = cur.p[i].first + dir[j][0];
                        int y = cur.p[i].second + dir[j][1];
                        int px = cur.p[i].first + dir[(j + 2) % 4][0];
                        int py = cur.p[i].second + dir[(j + 2) % 4][1];
                        if (!judge(x, y) || !judge(px, py)) continue;
                        nxt.p[i] = make_pair(x, y);
                        nxt.sort();
                        int hash;
                        if (isVisit(nxt, hash)) continue;
                        nxt.calcStable();
 //                       printf("%d,%d %d\n",x,y, nxt.isStable);
                        if (!nxt.isStable && !cur.isStable) continue;
                        if (nxt == tar) {
                            ok = true;
                            goto ex;
                        }
                        table[hash].push_back(nxt);
                        que.push_back(nxt);
                    }
                }   
                for (int i = 0; i < cur.count; ++i) {
                    maze[cur.p[i].first][cur.p[i].second] = '.';
                }
            }
        }
ex:;
        if (!ok) ans = -1;
        printf("Case #%d: %d\n", kase, ans);
    }
    return 0;
}
