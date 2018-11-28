#include <cstdio>

using namespace std;

int T, yy, N, K;

int main(void)
{
    scanf("%d\n", &T);
    for (yy = 1; yy <= T; yy++)
    {
        scanf("%d %d\n", &N, &K);
        N = 1 << N;
        printf("Case #%d: %s\n", yy, ((K % N) == N - 1) ? "ON" : "OFF");
    }

    return 0;
}
