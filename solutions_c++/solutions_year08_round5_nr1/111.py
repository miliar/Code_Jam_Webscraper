#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

using namespace std;

typedef long long int64;

bool x_grid[8001][8001];
bool y_grid[8001][8001];
bool is_inside[8001][8001];
int max_y[8001];
int max_x[8001];

int dir, x, y;

void walk(char c)
{
    if (c == 'F') {
        if (dir == 0) {
            x_grid[x][y] = true;
            y++;
        }
        if (dir == 1) {
            y_grid[x][y] = true;
            x++;
        }
        if (dir == 2) {
            y--;
            x_grid[x][y] = true;
        }
        if (dir == 3) {
            x--;
            y_grid[x][y] = true;
        }
    }
    if (c == 'L') {
        dir = (dir - 1 + 4) % 4;
    }
    if (c == 'R') {
        dir = (dir + 1 + 4) % 4;
    }
}

void solve()
{
    int l;
    scanf("%d", &l);
    
    memset(x_grid, 0, sizeof(x_grid));
    memset(y_grid, 0, sizeof(y_grid));
    memset(is_inside, 0, sizeof(is_inside));
    memset(max_x, 255, sizeof(max_x));
    memset(max_y, 255, sizeof(max_y));
    x = 4000, y = 4000, dir = 0;

    for (int i = 0; i < l; i++) {
        char str[33]; int t=-1;
        scanf("%s %d", str, &t);
        //fprintf(stderr, "%s %d\n", str, t);
        
        int str_l = strlen(str);
        for (int j = 0; j < t; j++)
        for (int k = 0; k < str_l; k++)
            walk(str[k]);
    }

    for (int x = 0; x <= 8000; x++)
    for (int y = 0; y <= 8000; y++) {
        if (x_grid[x][y])
            max_x[y] = max(max_x[y], x);

        if (y_grid[x][y])
            max_y[x] = max(max_y[x], y);
    }
        
    for (int y = 0; y <= 8000; y++) {
        bool inside = false;
        bool been_inside = false;
        for (int x = 0; x <= 8000; x++) {
            if (x_grid[x][y])
                inside = !inside;
            if (inside)
                been_inside = true;
            if (!inside && been_inside && max_x[y] > x)
                is_inside[x][y] = true;
        }
        if (inside) {
            fprintf(stderr, "ERROR\n");
            exit(0);
        }
    }

    for (int x = 0; x <= 8000; x++) {
        bool inside = false;
        bool been_inside = false;
        for (int y = 0; y <= 8000; y++) {
            if (y_grid[x][y])
                inside = !inside;
            if (inside)
                been_inside = true;
            if (!inside && been_inside && max_y[x] > y)
                is_inside[x][y] = true;
        }
        if (inside) {
            fprintf(stderr, "ERROR\n");
            exit(0);
        }
    }

    int ans = 0;
    for (int x = 0; x <= 8000; x++)
    for (int y = 0; y <= 8000; y++)
        if (is_inside[x][y])
            ans++;

    printf("%d", ans);
}

int main()
{
    int n_cases;
    scanf("%d", &n_cases);

    for (int i = 0; i < n_cases; i++) {
        fprintf(stderr, "Processing case #%d..\n", i+1);
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
}

