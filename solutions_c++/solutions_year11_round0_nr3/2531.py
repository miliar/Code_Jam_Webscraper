#include<algorithm>
#include<cstdio>

using namespace std;
int A[1005];
int main() {
    int T;
    scanf("%d", &T);
    for(int tt = 1 ; tt <= T ; tt++) {
        long long sum = 0;
        int N, check = 0, mn;
        scanf("%d\n", &N);
        for(int i = 0 ; i < N ; i++) {
            scanf("%d", A + i);
            if(i==0) mn = A[i];

            check ^= A[i];
            sum += A[i];
            mn = mn>A[i]?A[i]:mn;
        }
        if(!check) {
            printf("Case #%d: %lld\n", tt, sum - mn);
        }
        else {
            printf("Case #%d: NO\n", tt);
        }
    }
}
