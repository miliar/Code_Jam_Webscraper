#include <stdio.h>

using namespace std;


char grid[4][4];

bool revisaDiagonal1(char car){
    for(int i = 0; i < 4; i++){
        if(grid[i][i] != car && grid[i][i] != 'T')
            return false;
    }
    return true;
}

bool revisaDiagonal2(char car){
    for(int i = 3, j = 0; i >= 0, j < 4; i--, j++){
        if(grid[i][j] != car && grid[i][j] != 'T')
            return false;
    }
    return true;
}

bool revisaFila(int fila, char car){
    for(int i = 0; i < 4; i++){
        if(grid[fila][i] != car && grid[fila][i] != 'T')
                return false;
    }
    return true;
}

bool revisaColumna(int col, char car){
    for(int i = 0; i < 4; i++){
        if(grid[i][col] != car && grid[i][col] != 'T')
                return false;
    }
    return true;
}

void imprime(){
    for(int i = 0; i < 4; i++){
        for(int j = 0 ; j < 4; j++){
            printf("%c", grid[i][j]);
        }
        printf("\n");
    }
}

int main(){
    int T;
    scanf("%d", &T);
    bool ganaO, ganaX, incompleto;
    
    for(int i = 1; i <= T; i++){
        ganaO = false;
        ganaX = false;
        incompleto = false;
        for(int j = 0; j < 4; j++){
                scanf("%s", &grid[j]);
             for(int k = 0; k < 4; k++){
                if(grid[j][k] == '.')
                    incompleto = true;
            }
        }
        
        //imprime();
        
        for(int j = 0; j < 4; j++){
            if(revisaColumna(j, 'X') || revisaFila(j, 'X'))
                ganaX = true;
            if(revisaColumna(j, 'O') || revisaFila(j, 'O'))
                ganaO = true;
        }
        if(revisaDiagonal1('X') || revisaDiagonal2('X'))    
            ganaX = true;
        if(revisaDiagonal1('O') || revisaDiagonal2('O'))    
            ganaO = true;
         
        printf("Case #%d: ", i);
        
        if((ganaX && ganaO) || (!ganaX && !ganaO && !incompleto))
            puts("Draw");
        else if(ganaX && !ganaO)
            puts("X won");
        else if(ganaO && !ganaX)
            puts("O won");
        else if(!ganaX && !ganaO && incompleto)
            puts("Game has not completed");
    }
    
    
    return 0;
}
