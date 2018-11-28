#include <iostream>
using namespace std;

char a[50][50], b[50][50];
int n, k, t;
bool blue, red;

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        printf("Case #%d: ", i + 1);
        blue = red = 0; scanf("%d%d\n", &n, &k);
        memset(b, '.', sizeof(b));
        for (int i = 0; i < n; ++i) gets(a[i]);
        int x = n - 1, y = n - 1;
        for (int i = 0; i < n; ++i) {
            for (int j = n - 1; j >= 0; --j)
                if (a[i][j] == 'B' || a[i][j] == 'R')
                   b[y--][x] = a[i][j];
            --x; y = n - 1;
        }
        int tmp;
        for (int i = 0; i < n; ++i) {
            tmp = 0;
            for (int j = 0; j < n; ++j) {
                if (b[i][j] == 'R') if (tmp < 0) tmp = 1; else ++tmp;
                if (b[i][j] == 'B') if (tmp > 0) tmp = -1; else --tmp;
                if (b[i][j] == '.') tmp = 0;
                if (tmp == k) red = 1;
                if (tmp == -k) blue = 1;
            }
        }
        for (int j = 0; j < n; ++j) {
            tmp = 0;
            for (int i = 0; i < n; ++i) {
                if (b[i][j] == 'R') if (tmp < 0) tmp = 1; else ++tmp;
                if (b[i][j] == 'B') if (tmp > 0) tmp = -1; else --tmp;
                if (b[i][j] == '.') tmp = 0;
                if (tmp == k) red = 1;
                if (tmp == -k) blue = 1;
            }
        }
        x = n - 1, y = 0;
        while (y < n) {
              int i = x, j = y; tmp = 0;
              while (i < n && j < n) {
                    if (b[i][j] == 'R') if (tmp < 0) tmp = 1; else ++tmp;
                    if (b[i][j] == 'B') if (tmp > 0) tmp = -1; else --tmp;
                    if (b[i][j] == '.') tmp = 0;
                    if (tmp == k) red = 1;
                    if (tmp == -k) blue = 1;
                    ++i; ++j;
              }
              if (!x) ++y; else --x;
        }
        x = n - 1, y = n - 1;
        while (y >= 0) {
              int i = x, j = y; tmp = 0;
              while (i < n && j >= 0) {
                    if (b[i][j] == 'R') if (tmp < 0) tmp = 1; else ++tmp;
                    if (b[i][j] == 'B') if (tmp > 0) tmp = -1; else --tmp;
                    if (b[i][j] == '.') tmp = 0;
                    if (tmp == k) red = 1;
                    if (tmp == -k) blue = 1;
                    ++i; --j;
              }
              if (!x) --y; else --x;
        }
        if (blue && red) printf("Both\n");
        if (!blue && !red) printf("Neither\n");
        if (red && !blue) printf("Red\n");
        if (!red && blue) printf("Blue\n");
    }
    return 0;
}
