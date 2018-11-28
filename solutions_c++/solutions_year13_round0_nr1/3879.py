#include<iostream>
#include<stdio.h>
using namespace std;
char board[4][4];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,tc,i,j,row_X,row_O,col_X,col_O,ldiag_X,ldiag_O,rdiag_X,rdiag_O,dots,flag;
    scanf("%d\n",&t);
    for(tc=1;tc<=t;tc++)
    {
        scanf("%c %c %c %c\n",&board[0][0],&board[0][1],&board[0][2],&board[0][3]);
        scanf("%c %c %c %c\n",&board[1][0],&board[1][1],&board[1][2],&board[1][3]);
        scanf("%c %c %c %c\n",&board[2][0],&board[2][1],&board[2][2],&board[2][3]);
        scanf("%c %c %c %c\n",&board[3][0],&board[3][1],&board[3][2],&board[3][3]);

        dots=0;   flag=0; ldiag_X=0;  ldiag_O=0;  rdiag_X=0; rdiag_O=0;
        for(i=0;i<4;i++)
        {
            row_X=0;  row_O=0;  col_X=0;  col_O=0;
            for(j=0;j<4;j++)
            {
                switch(board[i][j])
                {
                    case 'X': row_X++;  break;
                    case 'O': row_O++;  break;
                    case 'T': row_O++;  row_X++;  break;
                    default:  dots++;   break;
                }
                switch(board[j][i])
                {
                    case 'X': col_X++;  break;
                    case 'O': col_O++;  break;
                    case 'T': col_O++;  col_X++;  break;
                    default:  break;
                }
            }

            switch(board[i][i])
            {
                case 'X': ldiag_X++;  break;
                case 'O': ldiag_O++;  break;
                case 'T': ldiag_O++;  ldiag_X++;  break;
                default:  break;
            }

            switch(board[i][3-i])
            {
                case 'X': rdiag_X++;  break;
                case 'O': rdiag_O++;  break;
                case 'T': rdiag_O++;  rdiag_X++;  break;
                default:  break;
            }

            if (row_X==4 || col_X==4 || ldiag_X==4 || rdiag_X==4)
            flag=1;
            else if(row_O==4 || col_O==4 || ldiag_O==4 || rdiag_O==4)
            flag=2;
        }
        if(flag==1)
            printf("Case #%d: X won\n",tc);
        else if(flag==2)
            printf("Case #%d: O won\n",tc);
        else
        {
            if(dots)
            printf("Case #%d: Game has not completed\n",tc);
            else
            printf("Case #%d: Draw\n",tc);
        }
    }
    return 0;
}

