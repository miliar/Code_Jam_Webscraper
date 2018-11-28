/*
 * Author: xay
 * Created Time:  2010-5-23 18:55:50
 * File Name: c.cpp
 * Description: 
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
#define move(x) (1<<(x))
const int maxint = -1u>>1;
const int maxn = 520;

bool r[maxn][maxn * 4];
bool used[maxn][maxn * 4];
int h[maxn][maxn * 4], v[maxn][maxn * 4], num[maxn][maxn * 4];
int n, m;
int ans[maxn];

int map(char c) {
    if (isdigit(c)) return c - '0';
    return c - 'A' + 10;
}
int main() {
    freopen("c.out", "w", stdout);
    int t, ca = 0;
    char s[maxn];
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d", &n, &m);
        m /= 4;
        for (int i = 0; i < n; ++i) {
            scanf("%s", s);
            for (int j = 0; j < m; ++j) {
                int tmp = map(s[j]);
                for (int k = 3; k >= 0; --k) {
                    r[i][j * 4 + 3 - k] = (tmp&move(k));
                }
            }
        }
        m *= 4;
//        for (int i = 0; i < n; ++i) {
//            for (int j = 0; j < m; ++j) {
//                printf("%d", r[i][j]);
//            }printf("\n");
//        }
        memset(used, 0, sizeof(used));
        int size = n * m;
        memset(ans, 0, sizeof(ans));
        while (size) {
            int rec = 0, recx, recy;
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < m; ++j) {
                    if (used[i][j]) continue;
                    if (j == 0 || used[i][j - 1] || r[i][j] == r[i][j - 1]) h[i][j] = 1;
                    else h[i][j] = h[i][j - 1] + 1;
                    if (i == 0 || used[i - 1][j] || r[i][j] == r[i - 1][j]) v[i][j] = 1;
                    else v[i][j] = v[i - 1][j] + 1;
                    num[i][j] = min(h[i][j], v[i][j]);
                    if (i > 0 && j > 0) {
                        if (used[i - 1][j - 1] || r[i - 1][j - 1] != r[i][j]) num[i][j] = 1;
                        else num[i][j] = min(num[i][j], num[i - 1][j - 1] + 1);
                    }
                    if (rec < num[i][j]) {
                        rec = num[i][j];
                        recx = i;
                        recy = j;
                    }
                }
            }
//            printf("%d %d\n", rec, size);
            ans[rec] ++;
            size -= rec * rec;
            for (int i = 0; i < rec; ++i) {
                for (int j = 0; j < rec; ++j) {
                    used[recx - i][recy - j] = true;
                }
            }
        }
        int cnt = 0;
        for (int i = 1; i <= n; ++i) {
            if (ans[i]) ++cnt;
        }
        printf("Case #%d: %d\n", ++ca, cnt);
        for (int i = n; i > 0; --i) {
            if (ans[i]) {
                printf("%d %d\n", i, ans[i]);
            }
        }
    }
    return 0;
}

