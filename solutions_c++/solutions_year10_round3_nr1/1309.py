#include <stdio.h>
#include <math.h>

void main()
{
    int t,n;
    FILE *fp1, *fp2;

    fp1 = fopen("a.in.txt", "r");
    fp2 = fopen("a.out.txt", "w+");

    fscanf(fp1, "%d", &t);

    for (int i=0; i<t; i++)
    {
        int w[10001][2] = {0};
        unsigned long total = 0;
        fscanf(fp1, "%d", &n);
        for (int j=0; j<n; j++)
        {
            fscanf(fp1, "%d %d", &w[j][0], &w[j][1]);
        }

        for (int j=0; j<n-1; j++)
        {
            for (int k=j+1; k<n; k++)
            {
                if ((w[j][0] - w[k][0]) * (w[j][1] - w[k][1]) < 0)
                {
                    total++;
                }
            }
        }

        fprintf(fp2, "Case #%d: %ld\n", i+1, total);
    }

    fclose(fp1);
    fclose(fp2);
}