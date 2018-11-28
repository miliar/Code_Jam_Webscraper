#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

#include <ext/hash_set>
using namespace __gnu_cxx;

const int dx[3] = {0, 0, 1}, dy[3] = {1, -1, 0};

struct hashf {
    size_t operator()(const vector< pair<int, int> > &p) const
    {
        size_t ret = 0;
        for (int i = 0; i < p.size(); ++i)
            ret += ret * 3607 + p[i].first * 60 + p[i].second;
        return ret;
    }
};

const int maxn = 60 + 5;

int n;
char a[maxn][maxn];
bool v[maxn][maxn];
vector< pair<int, int> > p;
hash_set< vector< pair<int, int> >, hashf> H;

void dfs(int x, int y)
{
    if (a[x][y] == '#' || v[x][y])
        return;
    p.push_back(make_pair(x, y));
    v[x][y] = true;
    dfs(x - 1, y);
    dfs(x, y + 1);
    dfs(x, y - 1);
}

bool check(vector< pair<int, int> > &p)
{
    if (p.size() == 1)
        return true;
    sort(p.begin(), p.end());
    p.erase(unique(p.begin(), p.end()), p.end());
    if (!H.insert(p).second)
        return false;
    for (int k = 0; k < 3; ++k) {
        vector< pair<int, int> > q;
        bool ok = true;
        for (int i = 0; i < p.size(); ++i) {
            int x = p[i].first + dx[k], y = p[i].second + dy[k];
            if (a[x][y] == '#') {
                x = p[i].first;
                y = p[i].second;
            }else
            if (!v[x][y]) {
                ok = false;
                break;
            }
            q.push_back(make_pair(x, y));
        }
        if (ok && check(q))
            return true;
    }
    return false;
}

int main()
{
    freopen("d1.in", "r", stdin);
    freopen("d1.out", "w", stdout);

    int t2;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: \n", t1);

        int R, C;
        cin >> R >> C;
        for (int i = 0; i < R; ++i)
            for (int j = 0; j < C; ++j)
                cin >> a[i][j];
        for (char c = '0'; c <= '9'; ++c)
            for (int i = 0; i < R; ++i)
                for (int j = 0; j < C; ++j)
                    if (a[i][j] == c) {
                        memset(v, 0, sizeof(v));
                        H.clear();
                        p.clear();
                        dfs(i, j);
                        cout << char(c) << ": " << p.size() << " " << (check(p) ? "Lucky" : "Unlucky") << endl;
                    }

        printf("\n");
    }
    
    return 0;
}
