#include <cstdio>
#include <cstring>
using namespace std;

char a[100][100];

int win(char x){
    for (int i = 0 ; i < 4; i++){
        int won = 1;
        for (int j = 0; won && j < 4; j++){
            if (a[i][j] != x && a[i][j] != 'T') won = 0;
            
        }
        if (won) return 1; 
    }
    for (int i = 0; i < 4; i++){
        int won = 1;
        for (int j = 0; won && j < 4; j++)
            if (a[j][i] != x && a[j][i] != 'T') won = 0;
        if (won) return 1;
    }
    int won = 1;
    for (int i = 0; won && i < 4; i++)
        if (a[i][i] != x && a[i][i] != 'T') won = 0;
    if (won) return 1;
    
    won = 1;
    for (int i = 0; won && i < 4; i++)
        if (a[i][3-i] != x && a[i][3-i] != 'T') won = 0;
    if (won) return 1;
    
    return 0;
}

int draw(){
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (a[i][j] == '.') return 0;
    return 1;
}

int main(){
    freopen("a.in", "r", stdin);
    freopen("a.txt", "w", stdout);
    int cases; scanf("%d", &cases);
    for (int tc = 1; tc <= cases; tc++){
        printf("Case #%d: ", tc);
        for (int i = 0; i < 4; i++)
            scanf("%s", &a[i]);
        if (win('X') ) puts("X won");
        else if (win('O') ) puts("O won");
        else if (draw() ) puts("Draw");
        else puts("Game has not completed");
    }
    return 0;   
}
