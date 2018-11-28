#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <limits>

using namespace std;

typedef pair<int, int> ii;
typedef pair<int, ii> iii;

bool cmp(const iii& i1, const iii& i2) { return i1.first < i2.first; }

int m[100][100];
int a[100][100];
char mm[26];

const int dy[] = {-1, 0, 0, 1};
const int dx[] = {0, -1, 1, 0};

int T, H, W, idx;

bool inside(int x, int y)
{
    return 0 <= x && x < W && 0 <= y && y < H;
}

bool pours(int x, int y, int tx, int ty)
{
    int mn = INT_MAX;
    for (int i = 0; i < 4; ++i)
    {
        int xx = x + dx[i];
        int yy = y + dy[i];
        if (inside(xx, yy))
            mn = min(mn, m[yy][xx]);
    }

    for (int i = 0; i < 4; ++i)
    {
        int xx = x + dx[i];
        int yy = y + dy[i];
        if (inside(xx, yy) && m[yy][xx] == mn)
            return xx == tx && yy == ty && m[yy][xx] < m[y][x];
    }
    return false;
}

void dfs(int x, int y)
{
    for (int i = 0; i < 4; ++i)
    {
        int xx = x + dx[i];
        int yy = y + dy[i];
        if (inside(xx, yy) && pours(xx, yy, x, y))
            dfs(xx, yy);
    }

    a[y][x] = idx;
}

int main()
{
    scanf("%d", &T);
    for (int cs = 1; cs <= T; ++cs)
    {
        idx = 1;
        memset(a, 0, sizeof(a));
        vector<iii> vv;
        scanf("%d%d", &H, &W);
        for (int i = 0; i < H; ++i)
            for (int j = 0; j < W; ++j)
            {
                scanf("%d", &m[i][j]);
                vv.push_back(iii(m[i][j], ii(i, j)));
            }

        sort(vv.begin(), vv.end(), cmp);
        for (int i = 0; i < (int)vv.size(); ++i)
        {
            if (!a[vv[i].second.first][vv[i].second.second])
            {
                dfs(vv[i].second.second, vv[i].second.first);
                ++idx;
            }
        }

        memset(mm, 0, sizeof(mm));
        char ch = 'a';
        printf("Case #%d:\n", cs);
        for (int i = 0; i < H; ++i)
        {
            for (int j = 0; j < W; ++j)
            {
                int u = a[i][j];
                if (!mm[u]) mm[u] = ch++;
                printf("%c ", mm[u]);
            }
            printf("\n");
        }
    }
    return 0;
}