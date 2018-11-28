#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <string>
#include <vector>
#include <string.h>
using namespace std;


int a[102][102];
int a2[102][102];
int count;

int main() {
    int T;
    scanf("%d", &T);
    int c, i, j, k;
    int res;
    int R;
    int n1, n2;
    int start = 0;
    int j1,k1,j2,k2;
    for (c = 1; c <= T; c++) {
        scanf("%d", &R);
        for (i = 0; i < 102; i++) {
            for (j = 0; j < 102; j++) {
                a[i][j] = 0;
            }
        }
        for (i = 0; i < R; i++) {
            scanf("%d%d%d%d", &j1, &k1, &j2, &k2);
            for (j = j1; j <= j2; j++) {
                for (k = k1; k<= k2; k++) {
                    a[j][k] = 1;
                    
                }
            }
            
        }
        n1=0;
            for (i = 1; i < 101; i++) {
                for (j = 1; j < 101; j++) {
                    if (a[i][j] == 1) n1++;
                }
            }
        count = 0;
        while(n1 > 0) {
            count++;
            memset(a2, 0, sizeof(a2));
            n2 = 0;

            
            for (j = 1; j < 101; j++) {
                for (k = 1; k < 101; k++) {
                    a2[j][k] = a[j][k];
                    if (a[j][k] == 1 && a[j - 1][k] == 0 && a[j][k - 1] == 0) {
                        a2[j][k] = 0;
                    }
                    else if (a[j][k] == 0 &&  a[j - 1][k] == 1 && a[j][k - 1] == 1) {
                        a2[j][k] = 1;
                    }
                    if(a2[j][k] == 1) n2++;
                }
            }
            
            /*
            for (i = 1; i < 6; i++) {
                for (j = 1; j < 6; j++) {
                    printf("%d ", a[i][j]);
                }
                putchar(10);
            }*/
            
            n1 = n2;
            memcpy(a, a2, sizeof(a2));
        }
        printf("Case #%d: %d\n", c, count);
    }
    return 0;
}
