#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <utility>
#include <cstring>
#include <queue>

using namespace std;

typedef pair<int,int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<iii> viii;
int n,m,n1,n2,j,n11,n22;

char board[4][4];
int main()
{
    int casenum = 1;
    int TC,i,j;
    scanf("%d\n",&TC);
    while(TC--){
        bool period = false;
        for(i = 0; i < 4; i++){
            for(j = 0; j < 4; j++){
                char c = getchar();
                board[i][j] = c;
                //printf("%c\n",c);
                if(c == '.') period = true;
            }
            scanf("\n");
        }
        scanf("\n");
        char winner = '\0';
        // process board
        for(i = 0; i < 4; i++){
            char c = board[i][0];
            if(c == '.') continue;
            bool found = true;
            for(j = 0; j < 4; j++){
                if(c == 'T') c = board[i][j];
                if(board[i][j] != c && board[i][j] != 'T'){
                    found = false;   
                }
            }
            if(found){
                winner = c;
            }
            
        }
        for(i = 0; i < 4; i++){
            char c = board[0][i];
            if(c == '.') continue;
            bool found = true;
            for(j = 0; j < 4; j++){
                if(c == 'T') c = board[j][i];
                if(board[j][i] != c && board[j][i] != 'T'){
                    found = false;   
                }
            }
            if(found){
                winner = c;
            }
            
        }
        //check diagonal
        char c = board[0][0];
        bool found = true;
        for(i = 1; i < 4 && c != '.'; i++){
            if(c == 'T') c = board[i][i];
            if(board[i][i] != c && board[i][i] != 'T'){
                   found = false;
            }
        }
        if(found && c != '.') winner = c;
        c = board[3][0];
        found = true;
        for(i = 1; i < 4 && c != '.'; i++){
            if(c == 'T'){c = board[3-i][i];}
            
            if(board[3-i][i] != c && board[3-i][i] != 'T'){
                   found = false;
            }
        }
        if(found && c != '.') winner = c;
        if(winner != '\0'){
            printf("Case #%d: %c won\n",casenum++,winner);   
        }
        else if(period){
            printf("Case #%d: Game has not completed\n",casenum++);   
        }else{
                printf("Case #%d: Draw\n",casenum++);  
        }
    }
    return 0;
}
