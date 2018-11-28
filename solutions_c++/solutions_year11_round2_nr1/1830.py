#include<stdio.h>

int main(int argc, char **argv)
{
    int t;

    scanf("%d", &t);

    int casos;

    for (casos = 1; casos <= t; casos++)
    {
        int n;

        char resultados[105][105];

        int jogos[105];
        int vitorias[105];

        double wp[105];
        double owp[105];
        double oowp[105];

        scanf("%d", &n);

        for(int i = 0; i < n; i++)
        {
            vitorias[i] = 0;
            jogos[i] = 0;

            for(int j = 0; j < n; j++)
            {
                if(j == 0)
                {
                    scanf("%*c");
                }

                scanf("%c", &resultados[i][j]);

                if(resultados[i][j] == '1')
                {
                    vitorias[i]++;
                    jogos[i]++;
                }
                else if(resultados[i][j] == '0')
                {
                    jogos[i]++;
                }
            }
            if(jogos[i] != 0)
            {
                wp[i] = (double) vitorias[i]/ (double) jogos[i];
            }
            else
            {
                wp[i] = 0;
            }

            //printf("[%d]: %f\n", i, wp[i]);
        }

        for(int i = 0; i < n; i++)
        {
            double somaWP = 0;
            int qtdWP = 0;
            for(int k = 0; k < n; k++)
            {
                int tempV;
                int tempJ;

                if(resultados[k][i] == '1')
                {
                    tempV = vitorias[k]-1;
                    tempJ = jogos[k]-1;
                    qtdWP++;

                    double tempWP = 0;
                    if(tempJ != 0)
                    {
                        tempWP = (double) tempV / (double) tempJ;
                    }

                    somaWP += tempWP;
                }
                else if(resultados[k][i] == '0')
                {
                    tempV = vitorias[k];
                    tempJ = jogos[k]-1;

                    qtdWP++;

                    double tempWP = 0;
                    if(tempJ != 0)
                    {
                        tempWP = (double) tempV / (double) tempJ;
                    }

                    somaWP += tempWP;
                }
            }

            owp[i] = somaWP/qtdWP;
            //printf("[%d] : %f\n", i, owp[i]);
        }

        for(int i = 0; i < n; i++)
        {
            double somaOWP = 0;
            int qtd = 0;

            for(int k = 0; k < n; k++)
            {
                if(resultados[k][i] == '1' || resultados[k][i] == '0')
                {
                    somaOWP += owp[k];
                    qtd++;
                }
            }

            oowp[i] = somaOWP/qtd;

            //printf("[%d]: %f\n", i, oowp[i]);
        }

        printf("Case #%d:\n", casos);

        for(int i = 0; i < n; i++)
        {
            double temp = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
            printf("%f\n", temp);
        }
    }

    return 0;
}
