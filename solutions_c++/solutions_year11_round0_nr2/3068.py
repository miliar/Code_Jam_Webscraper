#include <stdio.h>

int c;
int d;
int n;
int t;
char opos[40][20];
char comb[40][20];
char lista[300];
FILE * ent, * sal;
int indice;

void solucion()
{
    char car;
    for(int i = 0; i < n; i++)
    {
        fscanf(ent, "%c", &car);
        lista[++indice] = car;
        for (int p = 1; p <= c; p++)
        {
            if ((comb[p][1] == lista[indice] && comb[p][0] == lista[indice-1]) || (comb[p][0] == lista[indice] && comb[p][1] == lista[indice-1]))
            {
                lista[--indice] = comb[p][2];
                break;
            }
        }


        for (int p = 1; p <= d; p++)
        {
            for (int k = indice-1; k >= 1; k--)
            {
                    if ((lista[k] == opos[p][0] && lista[indice] == opos[p][1]) || (lista[k] == opos[p][1] && lista[indice] == opos[p][0]))
                    {
                        indice = 0;
                        break;
                    }
            }
        }
    }
}

void imprime()
{
    if(indice == 0){
        fprintf(sal, "]\n");
        return;
    }
    if (indice > 1)
        fprintf(sal, "%c, ", lista[1]);
    for(int i = 2; i < indice; i++)
        fprintf(sal, "%c, ", lista[i]);
    fprintf(sal, "%c]\n", lista[indice]);
}
int main()
{
    ent = fopen("inputF.txt", "r");
    sal = fopen("outputF.txt", "w");

    fscanf(ent, "%d", &t);
    for(int caso = 1; caso <= t; caso++)
    {
            fscanf(ent, "%d", &c);
            for(int i = 1; i <= c; i++)
                fscanf(ent, "%s", comb[i]);
            fscanf(ent, "%d", &d);
            for(int j = 1; j <= d; j++)
                fscanf(ent, "%s", opos[j]);

            fscanf(ent, "%d", &n);

            char basura;
            fscanf(ent, "%c", &basura);

            fprintf(sal, "Case #%d: [", caso);
            solucion();
            imprime();
            indice = 0;
            for (int p = 1; p <= c; p++)
            {
                    for (int i = 0; i < 20; i++)
                    {
                        comb[p][i] = 0;
                    }
            }
            for (int p = 1; p <= d; p++)
            {
                    for (int i = 0; i < 20; i++)
                    {
                        opos[p][i] = 0;
                    }
            }
    }

    return 0;
}


