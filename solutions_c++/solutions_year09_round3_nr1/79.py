#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>



int main() {
    int t;
    scanf("%d\n", &t);
    printf("use bignum;\n");
    for (int tt=1; tt<=t; tt++) {
        char str[500];
        char used[255];
        int count = 0;

        memset(used, 0, sizeof(used));

        gets(str);
        int l = strlen(str);
        for (int i=0; i<l; i++) {
            int c = str[i];
            if (!used[c]) {
                used[c] = (count<=1?1-count:count)+1;
                count++;
            }
        }
        if (count==1) count=2;

        int num=0;
        printf("print \"Case #%d: \"\n;", tt);
        for (int i=0; i<l; i++) {
            if (i) printf("+"); else printf("print (");
            int c = str[i];
            printf("(%d * (%d**%d))", used[c]-1, count, (l-1)-i);
        }
        printf(");\n");
        printf("print \"\\n\";\n");

    }
}
