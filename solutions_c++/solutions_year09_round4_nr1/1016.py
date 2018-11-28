#include <stdio.h>
#include <stdlib.h>

int main() {
    int t;
    scanf("%d\n", &t);
    for (int tt=1; tt<=t; tt++) {
        int res;
        int n;
        scanf("%d\n", &n);
        char str[500];
        int a[500];
        for (int i=0; i<n; i++) {
            gets(str);
            a[i] = 0;
            for (int j=n-1; j>=0; j--) {
                if (str[j]=='1') {
                    a[i] = j;
                    break;
                }
            }
            //printf("%d\n", a[i]);
        }
        res = 0;
        for (int k=0; k<n; k++) {
            if (a[k] > k) {
                for (int j=k+1; j<n; j++) {
                    if (a[j] <= k) {
                        //printf ("> %d\n", j);
                        int m = a[j];
                        for (int l=j; l>=k+1; l--) {
                            a[l] = a[l-1];
                            res++;
                        }
                        a[k] = m;
                        /*for (int o=0; o<n; o++) printf("%d ", a[o]);
                        printf("\n");*/
                        break;
                    }
                }
            }
        }

        printf("Case #%d: %d\n", tt, res);
    }
}

