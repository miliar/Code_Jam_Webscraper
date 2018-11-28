#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

//on remplace O par 1 et B par 0

int main()
{
    FILE * input = fopen("input", "r");
    FILE * output = fopen("output", "w");
    int T;
    fscanf(input, "%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        int n;
        fscanf(input, "%d", &n);
        int bouton[n][2];
        for(int i = 0; i< n; i++)
            fscanf(input,"%d%d", &bouton[i][0], &bouton[i][1]);
        int temps = 0;
        int pos[2]; pos[0] = 1; pos[1] = 1;
        for(int b = 0; b < n; b++)
        {
            int next = bouton[b][1];
            int nextr = bouton[b][0];
            int duree = abs(next - pos[nextr]) + 1;
            pos[nextr] = next;
            int indice = b;
            while(indice < (n-1) && bouton[indice][0] == nextr) indice++;
            int suivant = bouton[indice][1];
            if(suivant > pos[1 - nextr])
                pos[1 - nextr] = min(suivant, pos[1 - nextr] + duree);
            else
                pos[1 - nextr] = max(suivant, pos[1 - nextr] - duree);
            temps += duree;
        }
        fprintf(output, "Case #%d: %d\n", cas, temps);
    }
	return 0;
}
