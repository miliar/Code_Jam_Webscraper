#include <stdio.h>

unsigned long long calc(unsigned long long A, unsigned long long B)
{
    unsigned long long total = 0;
    unsigned long long mult[8] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};
    unsigned long long recycles[10];

    for(unsigned long long i = A; i < B; i++)
    {
        int digitos = 0;
        unsigned long long temp = i;
        while(temp)
        {
            digitos ++;
            temp = temp / 10;
        }

        for(int j = 1; j < digitos; j++)
        {
            // recycle j
            unsigned long long recycle = i / mult[j] +  (mult[digitos - j])*(i % mult[j]);
            recycles[j] = recycle;
            bool repetido = false;

            for(int k = 1; k < j; k++)
            {
                if(recycles[k] == recycle)
                {
                    repetido = true;
                }
            }

            if(!repetido && recycle > i && recycle <= B && (i % mult[j]) >= (mult[j - 1]))
            {
                total++;
            }
        }

    }

    return total;
}


int main()
{
    int T = 0;
    unsigned long long A;
    unsigned long long B;

    scanf("%d", &T);

    for(int test = 1; test <= T; test++)
    {
        printf("Case #%d: ", test);

        scanf("%llu", &A);
        scanf("%llu", &B);

        printf("%llu", calc(A, B));

        if(test != T)
        {
            printf("\n");
        }
    }

    return 0;
}