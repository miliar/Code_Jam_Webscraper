#include <stdio.h>
#include <string.h>
int pack[20][555];
char ss[20] = "welcome to code jam";
char s[555];
int main() {
    freopen("out.txt", "w", stdout);
    int ca;
    scanf("%d", &ca);
    gets(s);
    for(int v=1; v<=ca; v++) {
        gets(s);
        memset(pack, 0, sizeof(pack));
        for(int j=0; s[j] != 0; j++) {
            if(j > 0) pack[0][j] = pack[0][j-1];
            if(s[j] == ss[0]) {
                pack[0][j]++;
            }
        }
        for(int i=1; i<19; i++) {
            for(int j=1; s[j] != 0; j++) {
                pack[i][j] = pack[i][j-1];
                if(ss[i] == s[j]) {
                    pack[i][j] += pack[i-1][j-1];
                    pack[i][j] %= 10000;
                }
            }
        }
        printf("Case #%d: %04d\n", v, pack[18][strlen(s)-1]);
    }
    return 0;
}
