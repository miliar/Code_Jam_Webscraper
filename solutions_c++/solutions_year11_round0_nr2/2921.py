#include <stdio.h>

int main() {
    int ecase, ecount;
    char f[256][256];
    bool op[256][256];
    scanf("%d", &ecase);
    for (ecount = 1; ecount <= ecase; ecount++) {
        for (int i = 0; i < 256; i++)
            for (int j = 0; j < 256; j++) {
                f[i][j] = '\0';
                op[i][j] = false;
            }
        int ec;
        scanf("%d", &ec);
        while (ec > 0) {
            char ew[10];
            scanf("%s", ew);
            f[ ew[0] ][ ew[1] ] = ew[2];
            f[ ew[1] ][ ew[0] ] = ew[2];
            ec--;
        }
        
        int ed;
        scanf("%d", &ed);
        while (ed > 0) {
            char ew[10];
            scanf("%s", ew);
            op[ ew[0] ][ ew[1] ] = true;
            op[ ew[1] ][ ew[0] ] = true;
            ed--;
        }
        
        char list[1000];
        int lmany = 0;
        
        char einput[1000];
        scanf("%*d%s", einput);
        for (int i = 0; einput[i] != '\0'; i++) {
            list[lmany++] = einput[i];
            if (lmany >= 2) {
                char ta = list[lmany - 1];
                char tb = list[lmany - 2];
                if (f[ta][tb] != '\0') {
                    list[lmany - 2] = f[ta][tb];
                    lmany--;
                }
            }
            
            for (int j = 0; j < lmany - 1; j++) {
                char ta = list[j];
                char tb = list[lmany-1];
                if (op[ta][tb])
                    lmany = 0;
            }
        }
        
        printf("Case #%d: [", ecount);
        for (int i = 0; i < lmany; i++) {
            if (i > 0)
                printf(", ");
            printf("%c", list[i]);
        }
        printf("]\n");
    }
    return 0;
}
