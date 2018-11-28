#include <iostream>
#include <cstdio>

using namespace std;

int check(int b[][6]);

int main(void)
{
    int T;
    char buf[32];
    int board[6][6];
    scanf("%d", &T);
    for(int round=1;round<=T;round++) {
        for(int i=0;i<sizeof(board);i++)
            ((char *)board)[i] = 0;
        cin.getline(buf, 32); 
        for(int i=1;i<=4;i++) {
            cin.getline(buf, 32); 
            for(int j=1;j<=4;j++) {
                board[i][j] = buf[j-1];
            }
        }
        printf("Case #%d: ", round);
        switch(check(board)) {
        case 0: printf("X won\n"); break;
        case 1: printf("O won\n"); break;
        case 2: printf("Draw\n"); break;
        case 3: printf("Game has not completed\n"); break;
        default: break;
        }
    }
    return 0;
}

int check(int b[][6])
{
    for(int i=1;i<5;i++)
        for(int j=1;j<5;j++)
            b[i][0] += b[i][j];
    for(int j=1;j<5;j++)
        for(int i=1;i<5;i++)
            b[0][j] += b[i][j];
    for(int i=1;i<5;i++)
        b[0][0] += b[i][i];
    for(int i=1;i<5;i++)
        b[0][5] += b[i][5-i];

    for(int i=0;i<6;i++)
        if(b[0][i] == 'X' * 4 || b[0][i] == 'X' * 3 + 'T')
            return 0;
    for(int i=1;i<5;i++)
        if(b[i][0] == 'X' * 4 || b[i][0] == 'X' * 3 + 'T')
            return 0;

    for(int i=0;i<6;i++)
        if(b[0][i] == 'O' * 4 || b[0][i] == 'O' * 3 + 'T')
            return 1;
    for(int i=1;i<5;i++)
        if(b[i][0] == 'O' * 4 || b[i][0] == 'O' * 3 + 'T')
            return 1;

    for(int i=0;i<6;i++)
        for(int j=0;j<6;j++)
            if(b[i][j] == '.')
                return 3;

    return 2;
}

