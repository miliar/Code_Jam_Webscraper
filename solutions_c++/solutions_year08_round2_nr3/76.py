#include <cstdio>

int probCount;
int n;
int m;
int a[5010];

int main() {
    scanf("%d", &probCount);
    for(int probIndex=1; probIndex<=probCount; probIndex++) {
        scanf("%d", &n);
        for(int i=0; i<n; i++) {
            a[i] = 0;
        }
        int pos = 1;
        a[0] = 1;
        for(int i=2; i<=n; i++) {
            int count = i;
            int left = n-i+1;
            count = count % left;
            if(count == 0) {
                count = left;
            }
            for(; ; pos=(pos+1)%n) {
                if(a[pos] != 0) {
                    continue;
                }
                count--;
                if(count == 0) {
                    break;
                }
            }
            a[pos] = i;
            pos = (pos+1)%n;

        }

        printf("Case #%d:", probIndex);
        int m;
        scanf("%d", &m);
        for(int i=0; i<m; i++) {
            int q;
            scanf("%d", &q);
            printf(" %d", a[q-1]);
        }
        printf("\n");
    }
    return 0;
}
