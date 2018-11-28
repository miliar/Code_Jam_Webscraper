#include <cstdio>
using namespace std;

int f(char c)
{
    return c - 'A';
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int testnum = 1; testnum <= T; testnum++)
    {
        char buf[128];

        printf("Case #%d: ", testnum);

        char comb[32][32] = {};
        bool opp[32][32] = {};

        int C;
        scanf("%d", &C);
        while(C--)
        {
            scanf("%s", buf);
            comb[f(buf[0])][f(buf[1])] = comb[f(buf[1])][f(buf[0])] = buf[2];
        }

        int D;
        scanf("%d", &D);
        while(D--)
        {
            scanf("%s", buf);
            opp[f(buf[0])][f(buf[1])] = opp[f(buf[1])][f(buf[0])] = true;
        }

        int N;
        scanf("%d", &N);

        int total = 0;
        for(int i = 0; i < N; i++)
        {
            scanf(" %c", buf + total);

            while(total)
            {
                char c = comb[f(buf[total])][f(buf[total - 1])];
                if(c)
                    buf[--total] = c;
                else
                    break;
            }

            total++;
            for(int j = 0; j < total - 1; j++)
                if(opp[f(buf[j])][f(buf[total - 1])])
                {
                    total = 0;
                    break;
                }
        }

        printf("[");
        for(int i = 0; i < total; i++)
        {
            if(i)
                printf(", ");
            printf("%c", buf[i]);
        }
        printf("]\n");
    }
    return 0;
}
