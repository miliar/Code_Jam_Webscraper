#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int top[2010];
int height[2010];

int list[2010][2];
int listcnt;
int main(void) {
    freopen("input.txt", "r", stdin);
    /* freopen("output.txt", "w", stdout); */
    int t, T, N, i, far, imp, mx, j;

    scanf("%d", &T);

    for (t=1; t<=T; ++t) {
        imp = 0;

        scanf("%d", &N);
        for (i=1; i<N; ++i) {
            scanf("%d", &top[i]);
        }

        // far = top[1];
        // for (i=2; i<N; ++i) {
        //     if ( top[i] > far && far > i ) { imp = 1; break; }
        //     far = max(top[i], far);
        // }

        mx = 1000000;

        height[N] = mx;
        height[N-1] = mx-100000;

        for (i=N-2; i>=1; i--) {
            listcnt = 0;
            // printf("%d\n------------\n", i);
            // for (j=i+1; j<=N; ++j) printf("%d ", height[j]);
            // printf("\n");

            for (j=i+1; j<N; j=top[j]) {
                list[listcnt][0] = top[j];
                list[listcnt][1] = height[j] - (j-i)*(height[top[j]]-height[j])/(top[j]-j);
                listcnt++;
            }
            // for (j=0; j<listcnt; ++j) {
            //     printf("%d: %d\n", list[j][0], list[j][1]);
            // }

            if ( top[i] == i+1 ) {
                height[i] = list[0][1] - 1000;
            }
            else if ( top[i] == N ) {
                height[i] = list[listcnt-1][1] + 5;
            }
            else {
                for(j=0; j<listcnt; ++j) {
                    if ( list[j][0] == top[i] ) break;
                }
                if ( j == listcnt ) { imp = 1; break; }

                height[i] = (list[j][1] + list[j+1][1]) / 2;
            }
            
            if ( imp ) break;
        }

        printf("Case #%d: ", t);
        if ( imp ) {
            printf("Impossible\n");
        }
        else {
            for (i=1; i<N; ++i) printf("%d ", height[i]);
            printf("%d\n", height[N]);
        }
    }

    return 0;
}
