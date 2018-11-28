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
    input = freopen("A-large.in","r", stdin);
    output = freopen("A-large.out","w+", stdout);

    int varT;
    int numLinha, numColuna;
    char line[500], tabuleiro[500][500];

    scanf("%d", &varT);

    for(int i = 1; i <= varT; i++){
        scanf("%d", &numLinha);
        scanf("%d", &numColuna);
        for(int j = 0; j < numLinha; j++){
            scanf("%s", line);
            for(int k = 0; k < numColuna; k ++){
                tabuleiro[j][k] = line[k];
            }
        }



        for(int j = 0; j < numLinha - 1; j++){
            for(int k = 0; k < numColuna - 1; k ++){
                if(tabuleiro[j][k] == '#' && tabuleiro[j][k + 1] == '#' && tabuleiro[j + 1][k] == '#' && tabuleiro[j + 1][k + 1] == '#'){
                     tabuleiro[j][k] = '/';
                     tabuleiro[j][k+1] = '\\';
                     tabuleiro[j+1][k+1] = '/';
                     tabuleiro[j+1][k] = '\\';
                }
            }
        }

        bool possible = true;
        for(int j = 0; j < numLinha; j++){
            for(int k = 0; k < numColuna; k ++){
                if(tabuleiro[j][k] == '#'){
                    possible = false;
                    break;
                }
            }
            if(!possible){
                break;
            }
        }

        if(!possible){
            printf("Case #%d:\nImpossible\n", i);
        }
        else{
            printf("Case #%d:\n", i);
            for(int j = 0; j < numLinha; j++){
                for(int k = 0; k < numColuna; k ++){
                    printf("%c", tabuleiro[j][k]);
                }
                printf("\n");
            }
        }
    }

    fclose(input);
    fclose(output);
    return 0;
}
