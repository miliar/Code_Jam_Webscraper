#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main()
{

    FILE *input, *output;
    input = freopen("B-small-attempt0.in","r", stdin);
    output = freopen("B-small-attempt0.out","w+", stdout);

    int varT;
    int numSpeedb, tempoConst, numEstrelas, distancias, arrayDist[1000], estrelas[1000];
    int starB1 = -1, starB2 = -1;

    scanf("%d", &varT);

    for(int i = 1; i <= varT; i++){
        scanf("%d", &numSpeedb);
        scanf("%d", &tempoConst);
        scanf("%d", &numEstrelas);
        scanf("%d", &distancias);
        int aux;
        for(int j = 0; j < distancias; j++){
            scanf("%d", &aux);
            arrayDist[j] = aux;
        }
        int dist = 0;
        for(int j = 0; j < numEstrelas; j++){
            estrelas[j] = arrayDist[dist] * 2;
            dist = (dist + 1) % distancias;
        }

        int maior = 0;
        int somat = 0;
        bool travel = false;
        tempoConst = tempoConst;

        if(numSpeedb > 0){
            for(int j = 0; j < numEstrelas; j++){
                if(somat + estrelas[j] > tempoConst && somat <= tempoConst){
                    if(somat + estrelas[j] - tempoConst > maior){
                        travel = true;
                        maior = somat + estrelas[j] - tempoConst;
                        starB1 = j;
                    }
                }
                else{
                    if(somat > tempoConst){
                        if(estrelas[j] > maior){
                            travel = false;
                            maior = estrelas[j];
                            starB1 = j;
                        }
                    }
                }
                somat+=estrelas[j];
            }
            if(travel){
                estrelas[starB1] = estrelas[starB1] - maior/2;
            }
            else{
                estrelas[starB1] = estrelas[starB1]/2;
            }
        }

        maior = 0;
        somat = 0;
        travel = false;
        if(numSpeedb > 1){
            for(int j = 0; j < numEstrelas; j++){
                if(somat + estrelas[j] > tempoConst && somat <= tempoConst){
                    if(somat + estrelas[j] - tempoConst > maior){
                        travel = true;
                        maior = somat + estrelas[j] - tempoConst;
                        starB2 = j;
                    }
                }
                else{
                    if(somat > tempoConst){
                        if(estrelas[j] > maior){
                            travel = false;
                            maior = estrelas[j];
                            starB2 = j;
                        }
                    }
                }

                somat+=estrelas[j];
            }
            if(travel){
                estrelas[starB2] = estrelas[starB2] - maior/2;
            }
            else{
                estrelas[starB2] = estrelas[starB2]/2;
            }
        }

        somat = 0;
        for(int j = 0; j < numEstrelas; j++){
            somat += estrelas[j];
        }
        printf("Case #%d: %d\n", i, somat);
    }

    fclose(input);
    fclose(output);
    return 0;
}
