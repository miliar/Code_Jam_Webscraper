#include <cstdio>
#include <cstdlib>
using namespace std;


int main()
{
    FILE * input = fopen("input", "r");
    FILE * output = fopen("output", "w");
    int precalcul[501];
    int coeff[501][501];
    coeff[0][0] = 1;
    for(int n = 1; n <= 500; n++)
    {
        coeff[0][n] = 1;
        coeff[n][n] = 1;
        for(int k = 1; k < n; k++)
        {
            coeff[k][n] = (coeff[k-1][n-1] + coeff[k][n-1]) % 100003;
        }
        for(int k = n + 1; k < 501; k++) coeff[k][n] = 0;
    }
    int reponse[501][501]; //nb sous sets en fonction du nb à droite (pas toujours defini : de 0 à n - 2)
    reponse[2][0] = 1;
    precalcul[2] = 1;
    for(int n = 3; n <= 500; n++)
    {
        reponse[n][0] = 1;
        for(int d = 1; d <= n-2; d++)
        {
            reponse[n][d] = 0;
            for(int k = 0; k <= d - 1; k++)
                reponse[n][d] += (reponse[d+1][k] * coeff[d-1-k][n - d - 2]) % 100003;
        }
        printf("%d\n", n);
        int valeurn = 0;
        for(int i = 0; i <= n - 2; i++) valeurn = (valeurn + reponse[n][i]) % 100003;
        precalcul[n] = valeurn % 100003;
    }
    //for(int i = 2; i < 501; i++) fprintf(output,"%d\n", precalcul[i]);
    //fin des precalculs
    int T;
    fscanf(input, "%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        int n;
        fscanf(input, "%d", &n);
        fprintf(output, "Case #%d: %d\n", cas, precalcul[n]);
    }
    printf("done");
}
