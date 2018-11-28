#include <stdio.h>

int main()
{
    int T, N, K;
    scanf("%d", &T);

    for (int i = 1; i <= T; ++i)
    {
        scanf("%d %d", &N, &K);
        printf("Case #%d: ", i);

        int modulus = 1 << N;
        K %= modulus;

        if (K + 1 == modulus)
        {
            printf("ON\n");
        }
        else
        {
            printf("OFF\n");
        }
    }

    return 0;
}
