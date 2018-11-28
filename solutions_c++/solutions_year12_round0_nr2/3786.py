#include <cstdio>
using namespace std;

int solve_test_case()
{
    int N, S, P; scanf("%d %d %d", &N, &S, &P);
    int result = 0;
    if (P == 1)
    {
        for(int i = 0; i < N; i++)
        {
            int x; scanf("%d", &x);
            result += (x != 0);
        }
    }
    else
    {
        for(int i = 0; i < N; i++)
        {
            int x; scanf("%d", &x);
            if (x >= 3*P-2) result++;
            else if (x >= 3*P-4 && S)
            {
                result++;
                S--;
            }
        }
    }
    return result;
}

int main()
{
    int T; scanf("%d", &T);
    for(int t = 1; t <= T; t++)
        printf("Case #%d: %d\n", t, solve_test_case());
    return 0;
}
