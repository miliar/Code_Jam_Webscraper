#include <stdio.h>

int solve(int N, int S, int p, int *t)
{
    if(N > 1)
    {
        int surprise =  S > 0 ? solve(1, 1, p, t) + solve(N - 1, S - 1, p, t + 1) : 0;
        int not_surprise = solve(1, 0, p, t) + solve(N - 1, S, p, t + 1);

        return surprise > not_surprise ? surprise : not_surprise;
    }

    int total = t[0];

    if(S < 1)
    {
        int caso = total % 3 ? 1 : 0;
        int maior_nota = total / 3 + caso;

        if(maior_nota >= p)
        {
            return 1;
        }

    }
    else if(total >= 2 && total <= 28)
    {
        int caso = total % 3 == 2 ? 2 : 1;
        int maior_nota = total / 3 + (caso);

        if( maior_nota >= p)
        {
            return 1;
        }
    }

    return 0;
}




int main()
{
    int T = 0;
    int S = 0;
    int N = 0;
    int p = 0;
    int t[100];

    scanf("%d", &T);

    for(int test = 1; test <= T; test++)
    {
        printf("Case #%d: ", test);

        scanf("%d", &N);
        scanf("%d", &S);
        scanf("%d", &p);

        for(int i = 0; i < N; i++)
        {
            scanf("%d", &t[i]);
        }

        printf("%d", solve(N, S, p, t));

        if(test != T)
        {
            printf("\n");
        }
    }


    return 0;
}