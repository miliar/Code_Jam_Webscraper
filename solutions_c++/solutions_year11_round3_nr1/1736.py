
#include <cstdio>

using namespace std;

char board[100][100];

int solve(int r, int c)
{
    int i, j;
    for(i = 0; i < r; i++)
        scanf("%s", board[i]);
    
    for(i = 0; i < r; i++){
        for(j = 0; j < c; j++){
            if(board[i][j] == '#'){
                board[i][j] = '/';
                if(j + 1 < c && board[i][j+1] == '#'){
                    board[i][j+1] = '\\';
                    if(i + 1 < r && board[i+1][j] == '#'){
                        board[i+1][j] = '\\';
                        if(board[i+1][j+1] == '#')
                            board[i+1][j+1] = '/';
                        else
                            return 0;
                    }
                    else
                        return 0;
                }
                else
                    return 0;
            }
        }
    }
    return 1;
}

int main()
{
    int i, j;
    int r, c;
    int m;
    scanf("%d", &i);
    for(j = 1; j <= i; j++){
        scanf("%d %d", &r, &c);
        int tmp = solve(r, c);
        printf("Case #%d:\n", j);
        if(tmp){
            for(m = 0; m < r; m++){
                printf("%s\n", board[m]); 
            } 
        }
        else
            printf("Impossible\n");    
    }
    //scanf(" ");
    return 0;
}
