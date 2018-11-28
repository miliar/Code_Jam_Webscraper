#include <stdio.h>
#include <math.h>

void main()
{
    int t,n;
    unsigned long k;
    FILE *fp1, *fp2;

    fp1 = fopen("A-large.in", "r");
    fp2 = fopen("a.out.txt", "w+");

    fscanf(fp1, "%d", &t);

    for (int i=0; i<t; i++)
    {
        fscanf(fp1, "%d %lu", &n, &k);

        unsigned long min_step = pow((double)2, n);

        if ((k+1) % min_step == 0)
        {
            fprintf(fp2, "Case #%d: ON\n", i+1);
        }
        else
        {
            fprintf(fp2, "Case #%d: OFF\n", i+1);
        }
    }

    fclose(fp1);
    fclose(fp2);
 }