#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
using namespace std;

const int MAX_N = 520;

struct Board {
    int size;
    int x, y;

    Board(int _size, int _x, int _y) {
        size = _size;
        x = _x;
        y = _y;
    }

    bool operator <(const Board& other) const {
        if (size < other.size) return true;
        if (size > other.size) return false;

        if (x > other.x) return true;
        if (x < other.x) return false;

        if (y > other.y) return true;
        if (y < other.y) return false;

        return false;
    }
};

int n, m;
int a[MAX_N][MAX_N];
int best[MAX_N][MAX_N];
bool vis[MAX_N][MAX_N];

int getsize(Board b) {
    if (vis[b.x][b.y]) return 0;
    int sol = 1;
    for (int newsz = 2; newsz <= b.size; ++newsz) {
        bool ok = true;
        for (int i = 0; i < newsz; ++i) {
            ok &= !vis[b.x + i][b.y + newsz - 1];
            ok &= !vis[b.x + newsz - 1][b.y + i];
        }
        if (ok) ++sol;
        else break;
    }
    return sol;
}

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    int t; scanf("%d", &t);
    for (int test = 0; test < t; ++test) {
        memset(vis, 0, sizeof(vis));

        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < (m / 4); ++j) {
                char ch;
                scanf(" %c" , &ch);

                int val;
                if ('0' <= ch && ch <= '9')
                    val = ch - '0';
                else
                    val = ch - 'A' + 10;

                for (int stp = 3; stp >= 0; --stp)
                    a[i][j * 4 + 3 - stp] = (val >> stp) & 1;
            }
        }

        for (int i = n - 1; i >= 0; --i)
            for (int j = m - 1; j >= 0; --j)
                if (i == n - 1 || j == m - 1)
                    best[i][j] = 1;
                else
                    if (a[i][j] == a[i + 1][j + 1] && a[i][j] != a[i + 1][j] && a[i][j] != a[i][j + 1])
                        best[i][j] = 1 + min(best[i][j + 1], min(best[i + 1][j + 1], best[i + 1][j]));
                    else
                        best[i][j] = 1;


         priority_queue<Board, vector<Board> > heap;
         map<int, int> sizes;
         for (int i = 0; i < n; ++i)
             for (int j = 0; j < m; ++j) {
                 Board b(best[i][j], i, j);
                 heap.push(b);
             }

         map<int, int> dims;
         while (!heap.empty()) {
             Board b = heap.top();
             heap.pop();

             int sz = getsize(b);
             if (sz == b.size) {
                ++dims[sz];
                for (int i = 0; i < sz; ++i)
                    for (int j = 0; j < sz; ++j)
                        vis[b.x + i][b.y + j] = true;
             } else if (sz > 0) {
                 Board newb(sz, b.x, b.y);
                 heap.push(newb);
             }
         }

         printf("Case #%d: %d\n", test+1, dims.size());
         for (map<int, int>::reverse_iterator it = dims.rbegin(); it != dims.rend(); ++it)
             printf("%d %d\n", it->first, it->second);
    }
}
