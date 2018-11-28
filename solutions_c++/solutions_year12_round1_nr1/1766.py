#include <cstdio>

const int A_SIZE_MAX = 99999;
float p[A_SIZE_MAX + 1];
double right[A_SIZE_MAX + 1];
double wrong[A_SIZE_MAX + 1];

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);

    int case_total;
    scanf("%d", &case_total);
    for (int case_i = 1; case_i <= case_total; case_i++)
    {
        int A, B;
        scanf("%d %d", &A, &B);
        for (int i = 1; i <= A; i++)
            scanf("%f", &p[i]);
        right[0] = wrong[0] = 1.0;
        for (int i = 1; i <= A; i++)
        {
            right[i] = right[i-1] * p[i];
            wrong[i] = 1.0 - right[i];
        }
        // clac
        double min = 1 + B + 1;
        double cur;
        for (int i = 0; i <= A; i++)
        {
            cur = right[A-i] * (B-A+2*i+1) +
                  wrong[A-i] * (2*B-A+2*i+2);
            if (cur < min)
            {
                min = cur;
//                printf("get min %d\n", i);
            }

        }
        printf("Case #%d: %.6f\n", case_i, min);
    }

    return 0;
}
