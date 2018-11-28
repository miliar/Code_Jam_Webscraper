#include <iostream>
#include <cmath>
using namespace std;
int vines[10000][2];
int ans[10000];
int main() {
    int T; scanf("%d",&T); for (int t=1; t<=T; t++) {
        int N; scanf("%d",&N); 
        for (int i=0; i<N; i++) {
            scanf("%d %d",&vines[i][0],&vines[i][1]);
        }
        int D; scanf("%d",&D);
        for (int i=N-1; i>=0; i--) {
//            printf("Holding %d\n",i);
            // suppose holding vine i
            ans[i] = D-vines[i][0];
//            printf("To recah end: %d\n",ans[i]);
            for (int j=i+1; j<N; j++) {
                // reach vine j at height vines[j][0]-vines[i][0]
                if (ans[j]==-1) continue;
                if (vines[j][0]-vines[i][0]<ans[j]) continue;
                // what is smallest distance to reach vine j?
                // vines[j][0]-vines[i][0]
                int need = max(vines[j][0]-vines[i][0],ans[j]);
//                printf("To reach %d: %d\n",j,need);
                ans[i] <?= need;
            }
            if (ans[i]>vines[i][1]) ans[i] = -1;
//            printf("ans[%d] = %d\n",i,ans[i]);
        }
        printf("Case #%d: ",t);
        if (ans[0]!=-1 && vines[0][0]>=ans[0]) {
            printf("YES\n");
        } else printf("NO\n");
    }
}
