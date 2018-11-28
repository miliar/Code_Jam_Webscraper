#include <stdio.h>
#include <math.h>

long Gcd(long a, long b)
{
    if (b == 0)
    {
        return a;
    }
    else
    {
        return Gcd(b, a % b);
    }
}

int GcdN(long digits[], int length)
{
    if (1 == length)
    {
        return digits[0];
    }
    else
    {
        return Gcd(digits[length-1], GcdN(digits, length - 1));
    }
}

void main()
{
    FILE *fp1, *fp2;
    fp1 = fopen("b.in.txt", "r");
    fp2 = fopen("b.out.txt", "w+");

    int c;
    fscanf(fp1, "%d", &c);

    long num[10];

    for (int i=1; i<=c; i++)
    {
        int n;
        fscanf(fp1, "%d", &n);

        for (int j=0; j<n; j++)
        {
            fscanf(fp1, "%d", &num[j]);
        }

        long delta[10];
        int count = 0;
        for (int j=0; j<n-1; j++)
        {
            for (int k=j+1; k<n; k++)
            {
                
                delta[count] = abs(num[j] - num[k]);
                count++;
            }
        }

        long g = GcdN(delta, count);

        long max = -1;
        for (int j=0; j<n; j++)
        {
            if (num[j] > max)
            {
                max = num[j];
            }
        }

        if (max % g == 0)
        {
            fprintf(fp2, "Case #%d: %d\n", i, g * (max / g) - max);
        }
        else
        {
            fprintf(fp2, "Case #%d: %d\n", i, g * (max / g + 1) - max);
        }

        
    }

    fclose(fp1);
    fclose(fp2);
}