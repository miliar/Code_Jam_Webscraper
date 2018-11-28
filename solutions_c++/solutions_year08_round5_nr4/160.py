#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

using namespace std;

typedef long long int64;

int h, w, n;

int mem[100][100];
bool grid[100][100];

const int MOD = 10007;

int go(int x, int y)
{
    if (x < 0 || y < 0)
        return 0;
    if (x == 0 && y == 0)
        return 1;

    if (grid[x][y])
        return 0;

    int& ans = mem[x][y];
    if (ans != -1)
        return ans;
    ans = (go(x-2, y-1) + go(x-1, y-2)) % MOD;
    return ans;
}

void solve()
{
    scanf("%d%d%d", &h, &w, &n);
    memset(mem, 255, sizeof(mem));
    memset(grid, 0, sizeof(grid));

    for (int i = 0; i < n; i++) {
        int x, y;
        scanf("%d%d", &y, &x);
        grid[x-1][y-1] = true;        
    }

    int ans = go(w-1, h-1);

    printf("%d", ans);
}

int main()
{
    int n_cases;
    scanf("%d", &n_cases);

    for (int i = 0; i < n_cases; i++) {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
}

