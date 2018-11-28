#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main()
{

    FILE *input, *output;
    input = freopen("A-small-attempt0.in","r", stdin);
    output = freopen("A-small-attempt0.out","w+", stdout);

    int varT;
    char line[100];
    int numberTeams;
    char teams[100][100];
    double varWP[100], varOWP[100], varOOWP, jogouA[100];

    scanf("%d", &varT);

    for(int i = 1; i <= varT; i++){
        printf("Case #%d:\n", i);

        scanf("%d", &numberTeams);

        for(int j = 0; j < numberTeams; j++){
            scanf("%s", line);
            for(int k = 0; k < numberTeams; k++){
                teams[j][k] = line[k];
            }
        }

        for(int j = 0; j < numberTeams; j++){
            double partidasJogadas = 0;
            double partidasGanhas = 0;
            for(int k = 0; k < numberTeams; k++){
                if(teams[j][k] != '.'){
                    partidasJogadas++;
                    if(teams[j][k] == '1'){
                        partidasGanhas++;
                    }
                }
            }
            varWP[j] = partidasGanhas/partidasJogadas;


            varOWP[j] = 0;
            double jogadas = 0;
            bool jogou = false;
            for(int k = 0; k < numberTeams; k++){
                jogou = false;
                if(k != j && teams[j][k] != '.'){
                    double pJog = 0;
                    double pGan = 0;
                    for(int y = 0; y < numberTeams; y++){
                        if(teams[k][y] != '.' && y != j){
                            if(!jogou){
                                jogou = true;
                                jogadas++;
                            }
                            pJog++;
                            if(teams[k][y] == '1'){
                                pGan++;
                            }
                        }
                    }
                    varOWP[j] = varOWP[j] + (pGan/pJog);
                }
            }
            varOWP[j] = varOWP[j] /jogadas;
        }

        for(int j = 0; j < numberTeams; j++){
            double total = 0;
            varOOWP = 0;
            double divisor = 0;
            for(int k = 0; k < numberTeams; k++){
                if(k != j && teams[j][k] != '.'){
                    varOOWP += varOWP[k];
                    divisor++;
                }
            }
            total = (0.25 * varWP[j]) + (0.5 * varOWP[j]) + (0.25 * (varOOWP / divisor));
            //total = varOWP[j];
            printf("%.10f\n",total);
        }

    }

    fclose(input);
    fclose(output);
    return 0;
}
