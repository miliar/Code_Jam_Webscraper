#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

const int N = 8;
const char ansStr[N][N * 4] =
{
    "X won",
    "O won",
    "Draw",
    "Game has not completed"
};

char board[N][N];

bool judgeWin(int sx, int sy, int dx, int dy, char player)
{
    int count = 0;
    for(int i = 0; i < 4; i++)
        if(board[sx + i * dx][sy + i * dy] == player ||
           board[sx + i * dx][sy + i * dy] == 'T')
            count++;
    return count == 4 ? true : false;
}

bool judgeWin(char player)
{
    bool re = false;
    re = judgeWin(0, 0, 1, 1, player) ? true : re;
    re = judgeWin(0, 3, 1, -1, player) ? true : re;
    for(int i = 0; i < 4; i++)
    {
        re = judgeWin(0, i, 1, 0, player) ? true : re;
        re = judgeWin(i, 0, 0, 1, player) ? true : re;
    }
    return re;
}

bool judgeFull()
{
    bool re = true;
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            if(board[i][j] == '.')
                re = false;
    return re;
}

int main()
{
    freopen("out.txt", "w", stdout);
    int tcas, cas = 0;
    scanf("%d", &tcas);
    while(tcas --)
    {
            for(int i = 0; i < 4; i++)
                scanf("%s", board[i]);
            bool isXWin = judgeWin('X');
            bool isOWin = judgeWin('O');
            bool isFull = judgeFull();
            int idx = 3;
            if(isXWin)
                idx = 0;
            else if(isOWin)
                idx = 1;
            else if(isFull)
                idx = 2;
            printf("Case #%d: %s\n", ++cas, ansStr[idx]);
    }
    return 0;
}
