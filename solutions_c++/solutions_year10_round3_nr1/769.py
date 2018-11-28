#include <stdio.h>

int a[1005];
int b[1005];

int main () {
    
    int tc, n, hasil;
    
    scanf("%d",&tc);
    for(int cs=1; cs<=tc; cs++) {
        scanf("%d",&n);
        hasil = 0;
        for(int i=0;i<n;i++) {
            scanf("%d %d",&a[i], &b[i]);
        }
        for(int i=0;i<n-1;i++) {
            for(int j=i+1;j<n;j++) {
                if((a[i] < a[j] && b[i] > b[j]) || (a[i] > a[j] && b[i] < b[j])) {
                    hasil ++;
                }
            }
        }
        
        printf("Case #%d: %d\n",cs,hasil);
    }
    
    while (getchar()!=EOF);
    return 0;
}
