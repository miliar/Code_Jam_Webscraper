#include <iostream> 
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long int64;

int mass[550][550];
int row_count, col_count, value_d;

void init() {
    scanf("%d%d%d", &row_count, &col_count, &value_d);
    for (int i = 1; i <= row_count; i ++) {
        char buf[550];
        scanf("%s", buf);
        for (int j = 1; j <= col_count; j ++)
            mass[i][j] = value_d + (int)(buf[j-1] - '0');
    }
}

int64 sm[550][550], sx[550][550], sy[550][550];

void solve(int case_index) {
    cerr << case_index << endl;
    memset(sm, 0, sizeof(sm));
    memset(sx, 0, sizeof(sx));
    memset(sy, 0, sizeof(sy));
    for (int i = 1; i <= row_count; i ++)
        for (int j = 1; j <= col_count; j ++) {
            sm[i][j] = sm[i-1][j] + sm[i][j-1] - sm[i-1][j-1] + mass[i][j];
            sx[i][j] = sx[i-1][j] + sx[i][j-1] - sx[i-1][j-1] + mass[i][j] * i;
            sy[i][j] = sy[i-1][j] + sy[i][j-1] - sy[i-1][j-1] + mass[i][j] * j;
        }
    int max_width = -1;
    for (int x1 = 1; x1 <= row_count; x1 ++)
        for (int y1 = 1; y1 <= col_count; y1 ++)
            for (int width = 3; ; width ++) {
                int x2 = x1 + width - 1, y2 = y1 + width -1;
                if (x2 > row_count || y2 > col_count) 
                    break;
                int64 sum_mass = sm[x2][y2] - sm[x2][y1-1] - sm[x1-1][y2] + sm[x1-1][y1-1];
                int64 sum_x = sx[x2][y2] - sx[x2][y1-1] - sx[x1-1][y2] + sx[x1-1][y1-1];
                int64 sum_y = sy[x2][y2] - sy[x2][y1-1] - sy[x1-1][y2] + sy[x1-1][y1-1];
                sum_mass -= mass[x1][y1] + mass[x1][y2] + mass[x2][y1] + mass[x2][y2];
                sum_x -= x1*mass[x1][y1] + x1*mass[x1][y2] + x2*mass[x2][y1] + x2*mass[x2][y2];
                sum_y -= y1*mass[x1][y1] + y2*mass[x1][y2] + y1*mass[x2][y1] + y2*mass[x2][y2];
                
                if (sum_x*2 == sum_mass * (x1+x2) && sum_y*2 == sum_mass * (y1+y2)) {
                    //printf("mx = %d my = %d width = %d\n", mx, my, width);
                    max_width = max(max_width, width);                
                }
            }
    printf("Case #%d: ", case_index);
    if (max_width > 0)
        printf("%d\n", max_width);
    else
        printf("IMPOSSIBLE\n");
}

int main() {
    //freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
    freopen("B-large.in", "r", stdin);freopen("b_large_out.txt", "w", stdout);
    int case_count;
    scanf("%d", &case_count);
    for (int i = 1; i <= case_count; i ++) {
        init();
        solve(i);
    }
    return 0;
}
