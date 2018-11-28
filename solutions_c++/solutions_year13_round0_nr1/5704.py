#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

#define SIZE 4

int T, dim = 4;

char board[SIZE+1][SIZE+1];

string state()
{
    int i, j;
    bool incomplete = false;
    char mark;

    for(i=0; i<SIZE; i++) {
        mark = '\0';
        
        //row
        for(j=0; j<SIZE; j++) {
            if(board[i][j] == '.'){
                incomplete = true;
                break;
            }
            
            if(mark == '\0'){
                if(board[i][j] != 'T'){
                    mark = board[i][j];
                }
            }
            else if(board[i][j] != mark && board[i][j] != 'T'){
                break;
            }
        }
        
        if(j == SIZE){
            return (mark == 'X') ? "X won" : "O won";
        }
        
        
        //col
        mark = '\0';
        
        for(j=0; j<SIZE; j++) {
            if(board[j][i] == '.'){
                incomplete = true;
                break;
            }
            
            if(mark == '\0'){
                if(board[j][i] != 'T'){
                    mark = board[j][i];
                }
            }
            else if(board[j][i] != mark && board[j][i] != 'T'){
                break;
            }
        }
        
        if(j == SIZE){
            return (mark == 'X') ? "X won" : "O won";
        }
    }
    
    
    //diag
    mark = '\0';
    
    for(j=0; j<SIZE; j++) {
        
        if(board[j][j] == '.'){
            incomplete = true;
            break;
        }
        
        if(mark == '\0'){
            if(board[j][j] != 'T'){
                mark = board[j][j];
            }
        }
        else if(board[j][j] != mark && board[j][j] != 'T'){
            break;
        }
    }
    
    if(j == SIZE){
        return (mark == 'X') ? "X won" : "O won";
    }
    
    //diag
    mark = '\0';
    
    for(j=0; j<SIZE; j++) {
        
        if(board[j][SIZE - 1 - j] == '.'){
            incomplete = true;
            break;
        }
        
        if(mark == '\0'){
            if(board[j][SIZE - 1 - j] != 'T'){
                mark = board[j][SIZE - 1 - j];
            }
        }
        else if(board[j][SIZE - 1 - j] != mark && board[j][SIZE - 1 - j] != 'T'){
            break;
        }
    }
    
    if(j == SIZE){
        return (mark == 'X') ? "X won" : "O won";
    }
    
    if(incomplete) {
        return "Game has not completed";
    }
    
    return "Draw";
}

int main()
{
    scanf("%d", &T);
    getchar();
    
    for(int t=1; t<=T; t++)
    {
        int i;
        
        char temp[SIZE + 2];
        
        for(i=0; i < SIZE; i++)
        {
            gets(temp);
            strcpy(board[i], temp);
        }
        
        gets(temp);
        
        printf("Case #%d: %s\n", t, state().c_str());
    }
    
    return 0;
}