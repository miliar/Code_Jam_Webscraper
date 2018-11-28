#include <stdio.h>

#define MAX_n 1000

int T, n, X[MAX_n], Y[MAX_n], menor;

void swap(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

void perms(int p)
{
    if (p == n)
    {
        /*
        printf("Permutacion: ");
        for (int x = 0; x < n; x++)
            printf("%d ", Y[x]);
        printf("\n");
        */
        int t = 0;
        for (int x = 0; x < n; x++)
            t += X[x] * Y[x];
        if (t < menor)
            menor = t;
        return;
    }
    for (int x = p; x < n; x++)
    {
        swap(&Y[p], &Y[x]);
        perms(p+1);
        swap(&Y[p], &Y[x]);
    }
}

int main(void)
{
    FILE *in = fopen("asmall.in", "r");

    fscanf(in, "%d\n", &T);
    for (int x = 0; x < T; x++)
    {
        fscanf(in, "%d\n", &n);
        for (int t = 0; t < n; t++) fscanf(in, "%d", &X[t]); fscanf(in, "\n"); 
        for (int t = 0; t < n; t++) fscanf(in, "%d", &Y[t]); fscanf(in, "\n"); 
        menor = 10000000;
        perms(0);
        printf("Case #%d: %d\n", x+1, menor);
    }   

    fclose(in);
    return 0;
}
