#include <algorithm>
#include <numeric>
#include <cstdio>
#include <cstdlib>
#include <climits>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for(int numcase=1; numcase <= T; numcase++) {
        int N, X=0, sum=0, mn=INT_MAX;
        scanf("%d", &N);
        for(int i=0; i<N; i++) {
            int x;
            scanf("%d", &x);
            mn = min(mn, x);
            sum += x;
            X ^= x;
        }
        printf("Case #%d: ", numcase);
        if (X != 0) printf ("NO\n");
        else printf("%d\n", sum - mn);
    }
    return 0;
}
