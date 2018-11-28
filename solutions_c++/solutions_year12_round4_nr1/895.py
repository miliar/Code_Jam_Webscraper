#include <stdio.h>
#include <algorithm>
using namespace std;

int teste;
int D, n, T;

int earliest[10010];
int d[10010], l[10010];

int main() {
    for (scanf("%d", &T); T; T--) {
        printf("Case #%d: ", ++teste);
        
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            earliest[i] = -1;
            scanf("%d %d", &d[i], &l[i]);
        }
        scanf("%d", &D);
        
        bool found = false;
        earliest[0] = 0;
        for (int i = 0; i < n; i++) {
            if (earliest[i] == -1) continue;
            
            int dist = min(d[i]-earliest[i], l[i]);
            int reach = d[i]+dist;
            
            if (reach >= D) {
                found = true;
                break;
            }
            
            for (int j = i+1; j < n; j++) {
                if (d[j] <= reach && (earliest[j] == -1 || earliest[j] > d[i])) {
                    earliest[j] = d[i];
                }
            }
        }
        
        if (found) printf("YES\n");
        else printf("NO\n");
    }
}
