#include <stdio.h>
#include <string.h>

char str[1000];
int tb[40][1000];

char* pattern = "welcome to code jam";

int main() {
    int n;
    scanf("%d\n", &n);
    for (int t=1; t<=n; t++) {
        gets(str);
        int l = strlen(str);
        for (int i=0; i<l; i++) {
            tb[0][i] = 1;
        }
        int lp=strlen(pattern);
        for (int k=1; k<=lp; k++) {
            tb[k][0] = 0;
            for (int i=1; i<=l; i++) {
                if (pattern[k-1] == str[i-1]) {
                    tb[k][i] = (tb[k-1][i-1] + tb[k][i-1])%10000;
                } else {
                    tb[k][i] = tb[k][i-1];
                }
            }
        }
        /*for (int k=0; k<=lp; k++) {
            for (int i=0; i<=l; i++) {
                printf("%04d ", tb[k][i]);
            }
            printf("\n");
        }*/
        printf("Case #%d: %04d\n", t, tb[lp][l]);

    }
}
