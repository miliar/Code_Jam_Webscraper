#include <cstdio>
#include <cstdlib>
using namespace std;


int main()
{
    FILE * input = fopen("input", "r");
    FILE * output = fopen("output", "w");
    int C;
    fscanf(input, "%d", &C);
    for(int cas = 1; cas <= C; cas++)
    {
        int N, K, B, T;
        fscanf(input, "%d%d%d%d", &N, &K, &B, &T);
        int x[N];
        int v[N];
        for(int i = 0; i < N; i++) fscanf(input, "%d", &x[i]);
        for(int i = 0; i < N; i++) fscanf(input, "%d", &v[i]);
        int nbsaut = 0;
        int nbmouton = 0;
        int nbok = 0;
        bool possible = false;
        for(int j = N-1; j>=0; j--)
        {
            if(nbok == K && possible == false)
            {
                fprintf(output, "Case #%d: %d\n", cas, nbsaut);
                possible = true;
            }
            if(x[j] + v[j]*T >= B)
            {
                nbok++;
                nbsaut += nbmouton;
            }
            else
            {
                nbmouton++;
            }
        }
        if(nbok == K && possible == false)
        {
            fprintf(output, "Case #%d: %d\n", cas, nbsaut);
            possible = true;
        }
        if(possible == false) fprintf(output, "Case #%d: IMPOSSIBLE\n", cas);
    }
    printf("done\n");
}
