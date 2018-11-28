#include <cstdio>
#include <algorithm>
#include <functional>

using namespace std;

int N;
int A[10000], B[10000];

int main()
{
    int Cases;
    scanf("%d", &Cases);
    for (int Case = 1; Case <= Cases; Case ++)
    {
        scanf("%d", &N);
        for (int i = 0; i < N; i ++)
            scanf("%d", &A[i]);
        for (int i = 0; i < N; i ++)
            scanf("%d", &B[i]);
        sort(A, A + N);
        sort(B, B + N, greater <int> ());
        long long Ans = 0;
        for (int i = 0; i < N; i ++)
            Ans += ((long long) A[i]) * ((long long) B[i]);
        printf("Case #%d: %I64d\n", Case, Ans);
    }
    return 0;
}
