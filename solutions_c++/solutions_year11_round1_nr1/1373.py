#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main()
{

    FILE *input, *output;
    input = freopen("A-small-attempt1.in","r", stdin);
    output = freopen("A-small-attempt1.out","w+", stdout);

    int varT;
    int varN, varPD, varPG;
    int partidasJogadasH, partidasGanhasH;

    scanf("%d", &varT);


    for(int i = 1; i <= varT; i++){
        scanf("%d", &varN);
        scanf("%d", &varPD);
        scanf("%d", &varPG);
        bool end = false;
        for(int j = 1; j <= varN; j++){
            for(int k = j; k >= 0; k--){
                float porc = ((float)k/j) * 100;
                if(porc == varPD){
                    partidasJogadasH = j;
                    partidasGanhasH = k;
                    end = true;
                    break;
                }
            }
            if(end){
                break;
            }
        }

        if(!end){
            printf("Case #%d: Broken\n", i);
        }
        else{
            if(varPG == 100 && varPD != 100){
                printf("Case #%d: Broken\n", i);
                continue;
            }
            if(varPG == 0 && varPD != 0){
                 printf("Case #%d: Broken\n", i);
                 continue;
            }
            printf("Case #%d: Possible\n", i);
        }
    }

    fclose(input);
    fclose(output);
    return 0;
}
