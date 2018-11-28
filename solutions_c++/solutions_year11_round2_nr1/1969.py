
#include <stdio.h>

#define Tmax  20
#define Nmax  100

double outcome[Nmax][Nmax];
double wp_sum[Nmax];
double wp_count[Nmax];
double OWP[Nmax];
double oowp_sum[Nmax];
double oowp_count[Nmax];

int main()
{
    unsigned long T, N, x, n, i, j;
    unsigned char c;
    double WP, OOWP, sum, count, summ, countt;

    scanf("%u ", &T);
    for (x = 0; x < T; x ++)
    {
        scanf("%u ", &N);
        for (n = 0; n < N; n ++)
        {
            wp_sum[n] = wp_count[n] = 0;
            for (i = 0; i < N; i ++)
            {
                do
                    scanf("%c", &c);
                while ((c != '0') && (c != '1') && (c != '.'));
                if (c != '.')
                {
                    outcome[n][i] = c - '0';

                    wp_sum[n] += outcome[n][i];
                    wp_count[n] += 1;
                }
                else
                {
                    outcome[n][i] = 100;
                }
            }
        }

        for (n = 0; n < N; n ++)
        {
            summ = countt = 0;
            for (i = 0; i < N; i ++) if (outcome[n][i] < 100)
            {
                sum = count = 0;
                for (j = 0; j < N; j ++) if ((j != n) && (outcome[i][j] < 100))
                {
                    sum += outcome[i][j];
                    count += 1;
                }
                summ += count == 0 ? 0 : sum / count;
                countt += 1;
            }
            OWP[n] = countt == 0 ? 0 : summ / countt;
        }

        for (n = 0; n < N; n ++)
        {
            oowp_sum[n] = oowp_count[n] = 0;
            for (i = 0; i < N; i ++) if (outcome[n][i] < 100)
            {
                oowp_sum[n] += OWP[i];
                oowp_count[n] += 1;
            }
        }

        printf("Case #%lu:\n", x + 1);
        for (n = 0; n < N; n ++)
        {
            WP = wp_count[n] == 0 ? 0 : wp_sum[n] / wp_count[n];
            OOWP = oowp_count[n] == 0 ? 0 : oowp_sum[n] / oowp_count[n];
            printf("%.12Lf\n", 0.25 * WP + 0.50 * OWP[n] + 0.25 * OOWP);
        }
    }
}
