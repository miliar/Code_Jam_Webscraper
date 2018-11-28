#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

double wp[1000];
double owp[1000];
double oowp[1000];

char score[1000][1000];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    int cases = 1;

    scanf("%d", &T);

    while (T-- > 0)
    {
        int N;
        scanf("%d\n", &N);
        for (int i = 0; i < N; i++)
        {
            scanf("%s\n", score[i]);
//            printf("%s\n", score[i]);
        }

        int countW, countT;
        int countOW, countOT;
        for (int i = 0; i < N; i++)
        {
            countW = 0;
            countT = 0;
            for (int j = 0; j < N; j++)
            {
                if (score[i][j] == '0')
                {
                    countT++;
                }
                else if (score[i][j] == '1')
                {
                    countW++;
                    countT++;
                }
            }
//            printf("%d %d ", countW, countT);
            wp[i] = (double)countW / countT;
//           printf("%f\n", wp[i]);
        }

        double temp;
        int op;
        for (int i = 0; i < N; i++)
        {
            temp = 0.0;
            op = 0;
            for (int j = 0; j < N; j++)
            {
                if (j == i)
                {
                    continue;
                }
                if (score[j][i] == '.')
                {
                    continue;
                }
                op++;
                countOW = 0;
                countOT = 0;
                for (int k = 0; k < N; k++)
                {
                    if (k == i)
                    {
                        continue;
                    }
                    if (score[j][k] == '0')
                    {
                        countOT++;
                    }
                    else if (score[j][k] == '1')
                    {
                        countOW++;
                        countOT++;
                    }
                }
                temp += (double)countOW / countOT;
            }
            owp[i] = (double)temp / op;
//            printf("%f %d %f\n", temp, op, owp[i]);
        }

        for (int i = 0; i < N; i++)
        {
            double tempOwp = 0.0;
            op = 0;
            for (int j = 0; j < N; j++)
            {
                if (i == j)
                {
                    continue;
                }
                if (score[j][i] == '.')
                {
                    continue;
                }
                op++;
                tempOwp += owp[j];
            }
            oowp[i] = (double) tempOwp / op;
        }
        printf("Case #%d:\n", cases++);
        for (int i = 0; i < N; i++)
        {
            printf("%f\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
        }
    }
    return 0;
}
