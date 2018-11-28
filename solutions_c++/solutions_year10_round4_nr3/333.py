

#include <cstdio>

const int
    MAXCORD = 105;

int T, tc, R;
bool cells[2][MAXCORD][MAXCORD];

bool has_cell(int x, int r, int c){
    if (r < 0 || r >= MAXCORD || c < 0 || c >= MAXCORD) return false;
    return cells[x][r][c];
}

int main(){

    scanf("%d", &T);
    
    for (tc = 1; tc <= T; tc++){
    
        for (int i = 0 ; i < MAXCORD; i++)
            for (int j = 0; j < MAXCORD; j++)
                cells[0][i][j] = false;
    
        scanf("%d", &R);
        
        int cant = 0;
        
        for (int i = 0; i < R; i++){
        
            int x1, y1, x2, y2;
            
            scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
            
            for (int j = y1; j <= y2; j++)
                for (int k = x1; k <= x2; k++)
                    if (cells[0][j][k] == false){
                        cells[0][j][k] = true;
                        cant++;
                    }
        
        }
        
        int x = 1, sol = 0;
        
        while (cant > 0){
        
            for (int i = 0; i < MAXCORD; i++)
                for (int j = 0; j < MAXCORD; j++){
                
                    cells[x][i][j] = cells[x^1][i][j];
                
                    if (cells[x^1][i][j] && !has_cell(x^1, i - 1, j) && !has_cell(x^1, i, j - 1)){
                        cells[x][i][j] = false;
                        cant--;
                    }
                        
                    if (!cells[x^1][i][j] && has_cell(x^1, i - 1, j) && has_cell(x^1, i, j - 1)){
                        cells[x][i][j] = true;
                        cant++;
                    }
                
                }
        
            x ^= 1;
            sol++;
        }
        
                
        printf("Case #%d: %d\n", tc, sol);
    
    }

    return 0;
}
