#include <cstdio>
#include <iostream>
using namespace std;

int main(){
    int _test;
    scanf("%d",&_test);
    
    for(int tc = 1; tc<= _test; tc++){
        char grid[10][10];
        char winner = 'N';
        bool hasdot=0;
        
        for(int i=0; i<4; i++)
            scanf("%s",grid[i]);
        
        for(int r=0;r<4;r++)
            for(int c=0;c<4;c++)
                if(grid[r][c]=='.')hasdot=1;
            
        for(int row=0; row < 4; row++){
            char player=grid[row][0];
            bool valid=1;
            for(int i=1; i < 4; i++){
                char g = grid[row][i];
                if(g == '.')valid=0;
                else if(player == 'T')player = g;
                else if(g != player && g!='T')valid=0;
            }
            
            if(valid){
                winner = player;
                break;
            }
        }
        
        for(int col=0; col < 4; col++){
            char player=grid[0][col];
            bool valid=1;
            for(int i=1; i < 4; i++){
                char g = grid[i][col];
                if(g == '.')valid=0;
                else if(player == 'T')player = g;
                else if(g != player && g!= 'T')valid=0;
            }
            
            if(valid){
                winner = player;
                break;
            }
        }
        
        char player = grid[0][0];
        bool valid=1;
        for(int i=1; i<4; i++){
            char g=grid[i][i];
            if(g=='.')valid=0;
            else if(player == 'T')player=g;
            else if(g != player && g!='T')valid=0;            
        }
        
        if(valid)
            winner=player;
            
        player = grid[3][0];
        valid = 1;
        for(int i=1; i<4; i++){
            int r = i, c = 3 - i;
            char g = grid[r][c];
            
            if(g == '.')valid=0;
            else if(player == 'T')player = g;
            else if(g != player && g!='T')valid=0;
        }
        
        if(valid)
            winner = player;
            
        printf("Case #%d: ",tc);
        if(winner == 'X')puts("X won");
        else if(winner == 'O')puts("O won");
        else if(hasdot)puts("Game has not completed");
        else puts("Draw");
    }
    
    return 0;
}
