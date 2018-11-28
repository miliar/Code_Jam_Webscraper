#include <cstdio>
#include <cstdlib>

int main()
{
    FILE * input = fopen("input", "r");
    FILE * output = fopen("output", "w");
    int T;
    fscanf(input, "%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        int n, k;
        fscanf(input, "%d%d", &n, &k);
        bool snapper[n];
        for(int i = 0; i < n; i++) snapper[i] = false;
        int indice = 0;
        for(int i = 0; i < k; i++)
        {
            for(int i = 0; i <= indice; i++) snapper[i] = !snapper[i];
            indice = 0;
            while(snapper[indice] && indice < n - 1)
            {
                indice++;
            }
        }
        fprintf(output, "Case #%d: ", cas);
        if(indice == n-1 && snapper[n-1])
            fprintf(output, "ON\n");
        else
            fprintf(output, "OFF\n");
    }
}
