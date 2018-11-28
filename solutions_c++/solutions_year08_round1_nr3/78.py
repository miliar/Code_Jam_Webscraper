#include <cstdio>
#include <cstring>

int N;
int Ans[2][2], Mat[2][2];
int Tmp[2][2];

void Power(int N)
{
    while (N)
    {
        if (N & 1)
        {
            memset(Tmp, 0, sizeof(Tmp));
            for (int i = 0; i < 2; i ++)
                for (int j = 0; j < 2; j ++)
                    for (int k = 0; k < 2; k ++)
                    {
                        Tmp[i][k] += Ans[i][j] * Mat[j][k];
                        Tmp[i][k] %= 1000;
                    }
            memcpy(Ans, Tmp, sizeof(Tmp));
        }
        memset(Tmp, 0, sizeof(Tmp));
        for (int i = 0; i < 2; i ++)
            for (int j = 0; j < 2; j ++)
                for (int k = 0; k < 2; k ++)
                {
                    Tmp[i][k] += Mat[i][j] * Mat[j][k];
                    Tmp[i][k] %= 1000;
                }
        memcpy(Mat, Tmp, sizeof(Tmp));
        N >>= 1;
    }
}

int main()
{
    int Cases;
    scanf("%d", &Cases);
    for (int Case = 1; Case <= Cases; Case ++)
    {
        scanf("%d", &N);
        Ans[0][0] = 6;
        Ans[0][1] = 28;
        Mat[0][0] = 0;
        Mat[0][1] = -4;
        Mat[1][0] = 1;
        Mat[1][1] = 6;
        Power(N - 1);
        Ans[0][0] += 100000;
        Ans[0][0] %= 1000;
        Ans[0][0] --;
        Ans[0][0] += 100000;
        Ans[0][0] %= 1000;
        printf("Case #%d: ", Case);
        if (Ans[0][0] < 100)
            printf("0");
        if (Ans[0][0] < 10)
            printf("0");
        printf("%d\n", Ans[0][0]);
    }
    return 0;
}
