#include <stdio.h>
int main(){
    int test; scanf("%d", &test);
    for (int cas=1; cas<=test; cas++){
        int n; scanf("%d", &n); int crc=0, m=0x3f3f3f3f, ret=0;
        for (int i=0; i<n; i++){
            int p; scanf("%d", &p);
            crc^=p; m=p<m?p:m; ret+=p;
        }
        printf("Case #%d: ", cas);
        if (crc!=0) puts("NO"); else printf("%d\n", ret-m);
    }
}
