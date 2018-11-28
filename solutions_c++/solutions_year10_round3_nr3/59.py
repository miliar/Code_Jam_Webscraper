//============================================================================
// Name        : C.cpp
// Author      : Artem A. Khizha
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstdio>
#include <utility>
#include <algorithm>
#include <cstring>
using namespace std;

int n, m;
int a[512][512];
int cnt[513];

bool check(int x, int y, int s) {
    if (a[x][y] == 2)
        return false;
    for (int i = 1; i < s; i++)
        if (a[x + i][y] == a[x + i - 1][y] || a[x + i][y] == 2)
            return false;
    for (int i = 1; i < s; i++)
        if (a[x][y + i - 1] == a[x][y + i] || a[x][y + i] == 2)
            return false;
    for (int i = 1; i < s; i++)
        for (int j = 1; j < s; j++)
            if (a[x + i][y + j] == a[x + i - 1][y + j] ||
                a[x + i][y + j] == a[x + i][y + j - 1] ||
                a[x + i][y + j] != a[x + i - 1][y + j - 1] ||
                a[x + i][y + j] == 2)
                return false;
    for (int i = 0; i < s; i++)
        for (int j = 0; j < s; j++)
            a[x+i][y+j] = 2;
    return true;
}

int main() {
    int tnum;
    scanf("%d", &tnum);
    for (int ti = 1; ti <= tnum; ti++) {
        scanf("%d%d", &m, &n);
        memset(a, 0, sizeof(a));
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < m; i++) {
            char c[512];
            int x;
            scanf("%s", c);
            for (int j = 0; j < n / 4; j++) {
                if (c[j] >= '0' && c[j] <= '9')
                    x = c[j] - '0';
                else
                    x = c[j] - 'A' + 10;
                for (int k = 3; k >= 0; k--) {
                    a[i][4 * j + k] = x % 2;
                    x /= 2;
                }
            }
        }
//        for (int i = 0; i < m; i++) {
//            for (int j = 0; j < n; j++)
//                printf("%d", ((int) a[i][j]));
//            puts("");
//        }
        int s = min(n, m);
        int count = 0;
        for (int k = s; k > 0; k--) {
            for (int i = 0; i < m - k + 1; i++)
                for (int j = 0; j < n - k + 1; j++)
                    if (check(i, j, k)) {
                        //printf("\tsize %d succeeded at (%d, %d)\n", k, i+1, j+1);
                        cnt[k]++;
                        if (cnt[k] == 1)
                            count++;
                    }   else    {
                        //printf("\tsize %d failed at (%d, %d)\n", k, i+1, j+1);
                        ;
                    }
        }
        printf("Case #%d: %d\n", ti, count);
        for (int i = 512; i > 0; i--)
            if (cnt[i])
                printf("%d %d\n", i, cnt[i]);
    }
    return 0;
}
