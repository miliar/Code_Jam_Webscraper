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
    input = freopen("C-small-attempt0.in","r", stdin);
    output = freopen("C-small-attempt0.out","w+", stdout);

    int varT;
    int numNotas, minimo, maximo, musicos[100];

    scanf("%d", &varT);

    for(int i = 1; i <= varT; i++){
        scanf("%d", &numNotas);
        scanf("%d", &minimo);
        scanf("%d", &maximo);
        int aux;
        for(int j = 0; j < numNotas; j++){
            scanf("%d", &aux);
            musicos[j] = aux;
        }

        int nota;
        bool end;
        for(int j = minimo; j <= maximo; j++){
            end = true;
            for(int k = 0; k < numNotas; k++){
                if(musicos[k] % j == 0 || j % musicos[k] == 0){
                    //end = true;
                    //break;
                }
                else{
                    end = false;
                }

            }
            if(end){
                nota = j;
                break;
            }
        }

        if(!end){
            printf("Case #%d: NO\n", i);
        }
        else{
            printf("Case #%d: %d\n", i, nota);
        }
    }

    fclose(input);
    fclose(output);
    return 0;
}
