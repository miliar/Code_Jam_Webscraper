#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

using namespace std;

typedef long long int64;

int height, width;

bool grid[80][80];
int invalid[80];

int *curr, *next;

void solve()
{
    scanf("%d%d", &height, &width);

    for (int y = 0; y < height; y++) {
        char s[81];
        scanf("%s", s);
        for (int x = 0; x < width; x++)
            grid[x][y] = (s[x] == 'x');
        invalid[y] = 0;
        for (int x = 0; x < width; x++)
            if (grid[x][y])
                invalid[y] |= 1<<x;
    }

    fill_n(curr, 1<<width, 0);
    for (int y = 0; y < height; y++) {
        fill_n(next, 1<<width, 0);
        for (int i = 0; i < 1<<width; i++) {
            if ((i & invalid[y]) || (i & (i<<1 | i>>1)))
                continue;
            int count = 0;
            for (int j = 0; j < width; j++)
                if (i & 1<<j) count++;
            for (int j = 0; j < 1<<width; j++) {
                if (j & (i<<1 | i>>1))
                    continue;
                next[i] = max(next[i], curr[j]+count);
            }
        }
        swap(curr, next);
    }
    int ans = 0;
    for (int i = 0; i < 1<<width; i++)
        ans = max(ans, curr[i]);
    printf("%d", ans);
}

int main()
{
    int n_cases;
    scanf("%d", &n_cases);

    curr = new int[1024];
    next = new int[1024];

    for (int i = 0; i < n_cases; i++) {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
}

