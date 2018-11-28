/*
    Qualification Round 2011 -
    GoroSort
    by Dave Chang
*/
#include <cstdio>
#include <algorithm>

using namespace std ;

    int T, N, arr[1000];
    int pos[1000];
    double ans;

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    scanf("%d", &T);
    for(int z=1; z<=T; ++z) {
        ans = 0.0;
        scanf("%d", &N);
        for(int i=0; i<N; ++i) {
            scanf("%d", arr+i);
            --arr[i];
            pos[arr[i]] = i;
        }
        for(int i=0; i<N; ++i) {
            if(arr[i]!=i) {
                ans += 1.0;
            }
        }
        printf("Case #%d: %.6lf\n", z, ans);
    }
    return 0;
}
