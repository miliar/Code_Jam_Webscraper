#include <stdio.h>

#include <algorithm>

long long sum[1000 + 1];
int R, k, N;

int main() {
    int caseSize;
    scanf("%d", &caseSize);
    for (int T = 1; T <= caseSize; T++) {
        int tmp;
        scanf("%d%d%d", &R, &k, &N);
        sum[0] = 0;
        for (int i = 0; i < N; i++) {
            scanf("%d", &tmp);
            sum[i + 1] = sum[i] + tmp;
        }
        long long result = 0;
        long long limit;
        for (int i = 0, begin = 0, end = N; i < R; i++) {
            if (sum[N] - sum[begin] < k) {
                result += sum[N] - sum[begin];
                limit = k - (sum[N] - sum[begin]);
                end = begin;
                begin = 0;
            } else {
                end = N;
                limit = k;
            }
            int next = std::upper_bound(sum + begin, sum + end, sum[begin] + limit) - sum;
            if (sum[next] - sum[begin] > limit) {
                next--;
            }
            result += sum[next] - sum[begin];
            begin = next;
            end = N;
        }
        printf("Case #%d: %lld\n", T, result);
    }
    return 0;
}
