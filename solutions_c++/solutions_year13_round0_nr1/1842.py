#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
    int t;
    int count = 0;

    char chessboard[4][4];
    freopen("data.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    scanf("%d",&t);

    while (t--)
    {
        count ++;
        scanf("%c",&chessboard[0][0]);
        memset(chessboard,sizeof(chessboard),0);
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                scanf("%c",&chessboard[i][j]);
            }
            char temp;
            scanf("%c",&temp);
        }
        bool xcheck,ocheck;
        bool flag = false;
        bool endcheck = true;
        for (int i = 0; i < 4; i++)
        {
            xcheck = true;
            ocheck = true;
            for (int j = 0; j < 4; j++)
            {
                if (chessboard[i][j] == '.' || chessboard[i][j] == 'X') ocheck = false;
                if (chessboard[i][j] == '.' || chessboard[i][j] == 'O') xcheck = false;
                if (chessboard[i][j] == '.' ) endcheck = false;

            }
            if (xcheck) {
                printf("Case #%d: X won\n",count);flag = true;break;}
            if (ocheck) {printf("Case #%d: O won\n",count);flag = true;break;}
        }
        if (flag) continue;
        for (int i = 0; i < 4; i++)
        {
            xcheck = true;
            ocheck = true;
            for (int j = 0; j < 4; j++)
            {
                if (chessboard[j][i] == '.' || chessboard[j][i] == 'X') ocheck = false;
                if (chessboard[j][i] == '.' || chessboard[j][i] == 'O') xcheck = false;
            }
            if (xcheck) {
                printf("Case #%d: X won\n",count);flag = true;break;}
            if (ocheck) {printf("Case #%d: O won\n",count);flag = true;break;}
        }
        if (flag) continue;
        xcheck = true;
        ocheck = true;
        for (int i = 0;i < 4; i++)
        {
            if (chessboard[i][i] == '.') {xcheck= false;ocheck=false;}
            if (chessboard[i][i] == 'X') ocheck = false;
            if (chessboard[i][i] == 'O') xcheck = false;
        }
        if (xcheck) {
            printf("Case #%d: X won\n",count);flag = true;}
        if (ocheck) {printf("Case #%d: O won\n",count);flag = true;}
        if (flag) continue;
        xcheck = true;
        ocheck = true;
        for (int i = 0;i < 4; i++)
        {
            if (chessboard[i][3-i] == '.') {xcheck = false;ocheck = false;}
            if (chessboard[i][3-i] == 'X') ocheck = false;
            if (chessboard[i][3-i] == 'O' ) xcheck = false;
        }
        if (xcheck) {
            printf("Case #%d: X won\n",count);flag = true;}
        if (ocheck) {printf("Case #%d: O won\n",count);flag = true;}
        if (flag) continue;
        if (!endcheck) {printf("Case #%d: Game has not completed\n",count);continue;}
        else {printf("Case #%d: Draw\n",count); continue;}
    }
}
