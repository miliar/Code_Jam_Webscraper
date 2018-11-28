#include <cstdio>

int T, N, S, p, t, answer;

int main()
{
    scanf("%d", &T);
    for (int i = 1; i <= T; i++)
    {
        scanf("%d%d%d", &N, &S, &p);
        if (p == 0)
        {
            for (int j = 0; j < N; j++)
                scanf("%d", &t);
            answer = N;
        }
        else
        if (p == 1)
        {
            answer = 0;
            for (int j = 0; j < N; j++)
            {
                scanf("%d", &t);
                if (t) answer++;
            }
        }
        else
        {
            int lowest = p * 3 - 4;
            int lower = p * 3 - 2;
            answer = 0;
            for (int j = 0; j < N; j++)
            {
                scanf("%d", &t);
                if (lowest <= t)
                {
                    if (lower <= t)
                        answer++;
                    else if (S)
                    {
                        S--;
                        answer++;
                    }
                }
            }
        }
        printf("Case #%d: %d\n", i, answer);
    }
    return 0;
}