#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
    int numcases;
    int numvines;
    int pos[60005];
    int len[60005];
    int best[60005];
    int dist;
    bool possible;
    int cur;
    int i, j, k;
    scanf("%d", &numcases);
    for (i = 0; i < numcases; i++){
        possible = false;
        scanf("%d", &numvines);
        for (j = 0; j < numvines; j++){
            scanf("%d %d", &pos[j], &len[j]);
            best[j] = -1;
        }
        scanf("%d", &dist);
        best[0] = min(len[0], pos[0]);
        for (j = 0; j < numvines; j++){
            cur = pos[j] + best[j];
            for (k = j+1; k < numvines && pos[k] <= cur; k++){
                best[k] = max(best[k], min(pos[k] - pos[j], len[k]));
            }
            if (best[j] + pos[j] >= dist){
                possible = true;
                break;
            }
        }
        printf("Case #%d: ", i+1);
        if (possible){
            printf ("YES\n");
        } else {
            printf("NO\n");
        }
    }
    return 0;
}
