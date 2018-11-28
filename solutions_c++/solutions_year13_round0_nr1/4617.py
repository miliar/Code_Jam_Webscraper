#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#define DIM 4
using namespace std;

int T, Winner;
char Tab[DIM][DIM+1], first;
bool test, help, Complete;

int main(void){

    scanf("%d", &T);
    for(int t = 1; t <= T; t ++){
        for(int i = 0; i < DIM; i ++)
            scanf(" %s", Tab[i]);

        Winner = 0;

        // Lines:
        for(int i = 0; i < DIM && Winner == 0; i ++){
            test = true;
            help = false;
            first = '-';
            for(int j = 0; j < DIM; j ++){
                if(Tab[i][j] == 'T'){
                    if(help){
                        test = false;
                        break;
                    }
                    help = true;
                }
                else if(Tab[i][j] == '.'){
                    test = false;
                    break;
                }
                else{
                    if(first == '-')
                        first = Tab[i][j];
                    else if(first != Tab[i][j]){
                        test = false;
                        break;
                    }
                }
            }
            if(test)
                Winner = (first == 'X') ? 1 : 2;
        }

        // Columns:
        for(int i = 0; i < DIM && Winner == 0; i ++){
            test = true;
            help = false;
            first = '-';
            for(int j = 0; j < DIM; j ++){
                if(Tab[j][i] == 'T'){
                    if(help){
                        test = false;
                        break;
                    }
                    help = true;
                }
                else if(Tab[j][i] == '.'){
                    test = false;
                    break;
                }
                else{
                    if(first == '-')
                        first = Tab[j][i];
                    else if(first != Tab[j][i]){
                        test = false;
                        break;
                    }
                }
            }
            if(test)
                Winner = (first == 'X') ? 1 : 2;
        }

        // Diagonal \:
        if(Winner == 0){
            test = true;
            help = false;
            first = '-';
            for(int i = 0; i < DIM; i ++){
                if(Tab[i][i] == 'T'){
                    if(help){
                        test = false;
                        break;
                    }
                    help = true;
                }
                else if(Tab[i][i] == '.'){
                    test = false;
                    break;
                }
                else{
                    if(first == '-')
                        first = Tab[i][i];
                    else if(first != Tab[i][i]){
                        test = false;
                        break;
                    }
                }
            }
            if(test)
                Winner = (first == 'X') ? 1 : 2;
        }

        // Diagonal /:
        if(Winner == 0){
            test = true;
            help = false;
            first = '-';
            for(int i = 0; i < DIM; i ++){
                if(Tab[i][DIM-1-i] == 'T'){
                    if(help){
                        test = false;
                        break;
                    }
                    help = true;
                }
                else if(Tab[i][DIM-1-i] == '.'){
                    test = false;
                    break;
                }
                else{
                    if(first == '-')
                        first = Tab[i][DIM-1-i];
                    else if(first != Tab[i][DIM-1-i]){
                        test = false;
                        break;
                    }
                }
            }
            if(test)
                Winner = (first == 'X') ? 1 : 2;
        }

        // Complete:
        if(Winner == 0){
            Complete = true;
            for(int i = 0; i < DIM && Complete; i ++)
                for(int j = 0; j < DIM; j ++)
                    if(Tab[i][j] == '.'){
                        Complete = false;
                        break;
                    }
        }

        if(Winner == 1)
            printf("Case #%d: X won\n", t);
        else if(Winner == 2)
            printf("Case #%d: O won\n", t);
        else if(Complete)
            printf("Case #%d: Draw\n", t);
        else
            printf("Case #%d: Game has not completed\n", t);
    }

    return 0;
}
