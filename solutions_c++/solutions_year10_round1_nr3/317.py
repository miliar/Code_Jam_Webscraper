#include <stdio.h>

bool isWinning(int a, int b)
{
    if (b % a == 0)
    {
        return true;
    }
    else
    {
        int k = b / a;
        int c = b % a;

        if (k > 1)
        {
            return true;
        }
        else /* k == 1 */
        {
            if (c == a)
            {
                return false;
            }
            else
            {
                return !isWinning(c, a);
            }
        }
    }
}

int main()
{
    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; ++t)
    {
        int A1, A2, B1, B2;
        scanf("%d %d %d %d", &A1, &A2, &B1, &B2);

        int count = 0;

        // Naive solution
        for (int a = A1; a <= A2; ++a)
        {
            for (int b = B1; b <= B2; ++b)
            {
                if (a > b)
                {
                    if (isWinning(b, a)) count += 1;
                }
                else if (b > a)
                {
                    if (isWinning(a, b)) count += 1;
                }
            }
        }

        printf("Case #%d: %d\n", t, count);
    }

    return 0;
}
