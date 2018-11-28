#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <string>
#include <vector>
#include <string.h>
using namespace std;
#define in_range(x, y) ((x) >= 0 && (x) < (n) && (y) >= 0 && (y) < (n))

int a[1000][1000];
int k;

int calc_num(int n) {
    return n*(n+1)/2 + n*(n-1)/2;
}

bool check_center(int x, int y) {
    int n = 2 * k - 1;
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (a[i][j] == -1) continue;
            if (!in_range(2*x-i, j) || a[2*x-i][j] == -1 || a[2*x-i][j] == a[i][j]) {
            }
            else return false;
            if (!in_range(i, 2*y-j) || a[i][2*y-j] == -1 || a[i][2*y-j] == a[i][j]) {}
            else return false;
            
        }
    }
    return true;
}

int main() {
    int T;
    scanf("%d", &T);
    int c, i, j;
    int res;
    int start = 0;
    for (c = 1; c <= T; c++) {
        scanf("%d", &k);
        start = k - 1;
        for (i = 0; i < 2 * k - 1; i++) {
            for (j = 0; j < 2 * k - 1; j++) {
                a[i][j] = -1;
            }
        }
        res = 1000;
        for (i = 0; i < 2 * k - 1; i++) {
            for (j = 0; j <= i && j < 2 * k - 1 - i; j++) {
          //      printf("%d %d\n", i, start + j * 2);
                scanf("%d", &a[i][start + j * 2]);
            }
            if (i < k - 1) start--;
            else start++;
        }
        int posi, posj;
        for (i = 0; i < (2*k - 1); i++) {
            for (j = 0; j < (2*k - 1); j++) {
                //printf("%d %d\n", i, j);
                if (check_center(i, j)) {
                    //printf("yes\n");
                    int tmp;
                    tmp = abs(i - k + 1) + abs(j - k + 1);
                    //printf("tmp = %d\n", tmp);
                    if (res > tmp) {
                        res = tmp;
                        posi = i;
                        posj = j;
                    }
                }
            }
        }
        //printf("%d %d\n", posi, posj);
        //printf("res = %d\n", res);
        printf("Case #%d: %d\n", c, calc_num(k + res) - calc_num(k));
    }
    return 0;
}
