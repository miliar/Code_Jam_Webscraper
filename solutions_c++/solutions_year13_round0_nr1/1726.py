#include<cstdio>
#include<cstring>
using namespace std;
//won==1 for X, 2 for O
char board[5][5];

int main()
{
    freopen("al.txt","r",stdin);
    freopen("ansl.txt","w",stdout);
    int T,tx,ty;
    scanf("%d",&T);
    for(int test=1;test<=T;test++)
    {

        int won=0,t_found=0,draw=1;
        tx=-1;ty=-1;
        for(int i=0;i<4;i++)
        scanf("%s",board[i]);

        /*for(int i=0;i<4;i++)
        {
            printf("%s\n",board[i]);
        }*/

        //search for T

        for(int i=0;i<4;i++)
        {
         for(int j=0;j<4;j++)
         {
             if(board[i][j]=='T')
             {
                 tx=i;ty=j;
                 break;
             }
         }
        }
        // for X
        if(tx!=-1 && ty!=-1)board[tx][ty]='X';
        //diagonals
        if(board[0][0]=='X' && board[1][1]=='X'&&board[2][2]=='X' && board[3][3]=='X')won=1;
        if(board[0][3]=='X' && board[1][2]=='X'&&board[2][1]=='X' && board[3][0]=='X')won=1;

        //rows

        for(int i=0;i<4;i++)
        {
            if(board[i][0]=='X' && board[i][1]=='X' && board[i][2]=='X' && board[i][3]=='X')
            won=1;
        }

        //cols
        for(int i=0;i<4;i++)
        {
            if(board[0][i]=='X' && board[1][i]=='X' && board[2][i]=='X' && board[3][i]=='X')
            won=1;
        }

        // for Y
        if(tx!=-1 && ty!=-1)board[tx][ty]='O';
        //diagonals
        if(board[0][0]=='O' && board[1][1]=='O'&&board[2][2]=='O' && board[3][3]=='O')won=2;
        if(board[0][3]=='O' && board[1][2]=='O'&&board[2][1]=='O' && board[3][0]=='O')won=2;

        //rows

        for(int i=0;i<4;i++)
        {
            if(board[i][0]=='O' && board[i][1]=='O' && board[i][2]=='O' && board[i][3]=='O')
            won=2;
        }

        //cols
        for(int i=0;i<4;i++)
        {
            if(board[0][i]=='O' && board[1][i]=='O' && board[2][i]=='O' && board[3][i]=='O')
            won=2;
        }

        if(won==1){
        printf("Case #%d: X won\n",test);
        }
        else if(won==2)
        {
            printf("Case #%d: O won\n",test);
        }
        else{

        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(board[i][j]=='.')
                {
                    draw=0;
                    break;
                }
            }
        }

        if(draw==1){printf("Case #%d: Draw\n",test);}
        else if(draw==0){
            printf("Case #%d: Game has not completed\n",test);
        }
        }


    }
    return 0;
}
