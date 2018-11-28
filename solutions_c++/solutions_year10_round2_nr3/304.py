#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <string>
#include <vector>
#include <string.h>
#include <memory.h>
using namespace std;

int a[100];
char hash[100];
int table[26] = {0,0, 1,2,3,5,8,14,24,43,77,140,256,472,874,1628,3045,5719,10780,20388,38674,73562,140268,268066,513350,
984911};
int main() {
    int T, c, i, j, p, n;
    int res = 0;
    int now;
    scanf("%d" ,&T);
    for (c = 1; c <= T; c++) {
        scanf("%d", &n);/*
        res = 0;
        for (i = (1 << (n - 2)); i < (1 << (n - 1)); i++) {
            p = 1;
            for (j = 0; j <= n + 1; j++) hash[j] = -1;
            for (j = 0; j < n - 1; j++) {
                if (i & (1 << j)) {
                    a[p] = j + 2;
                    hash[j + 2] = p;
                    p++;
                }
            }
            if (a[p - 1] != n) continue;
            now = a[p - 1];
            for (j = p; j >= 0; j--) {
                if (now == -1 || now == 1) break;
                now = hash[now];
            }
            if (now == 1) {
            
                res++;
            }
        }*/
       
        printf("Case #%d: %d\n", c, table[n] % 100003);
        //printf("%d,", res);
    }
    return 0;
}
