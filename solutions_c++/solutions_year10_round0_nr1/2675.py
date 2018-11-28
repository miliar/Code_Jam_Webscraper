#include <iostream.h>

FILE *f = fopen("Snapper.in", "r");
FILE *g = fopen("Snapper.out", "w");

int T, N, K;


int main()
{
    
    fscanf(f, "%d", &T);
    
    for (int k =  0; k < T; ++k)
    {
        int p = 1, rest;
        fscanf(f, "%d %d", &N, &K);
        p = p << N;
        rest = K % p;
        if (rest == p - 1)
           fprintf(g, "Case #%d: ON\n", k + 1);
        else
           fprintf(g, "Case #%d: OFF\n", k + 1); 
    }
    
    
    fclose(f);
    fclose(g);
    
    
    return 0;
}
