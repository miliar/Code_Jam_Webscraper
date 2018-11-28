#include <stdio.h>

char board[5][5];
int n[100];


void reset()
{
    n['O']=0;
    n['X']=0;
    n['T']=0;
}

int main()
{

    int file,nFile;
    scanf("%d",&nFile);
    for(file=1;file<=nFile;file++)
    {
        scanf("\n");

        int i,j,row,col,won=0;
        char temp;
        for(i=0;i<4;i++)
        {
            gets(board[i]);
        }
        printf("Case #%d: ",file);
        //printf(".%d O%d X%d T%d",'.','O','X','T');
        n['.']=0;
        //row
        for(row=0;row<4;row++)
        {
            reset();
            for(j=0;j<4;j++)
            {
                if(board[row][j]!='T')
                    temp=board[row][j];
                n[board[row][j]]++;
            }
            if(((n[temp]==4)||(n[temp]==3&&n['T']==1))&&temp!='.')
            {
                printf("%c won\n",temp);
                won=1;
                break;
            }
        }
        if(won==1)
            continue;

        //col
        for(col=0;col<4;col++)
        {
            reset();
            for(i=0;i<4;i++)
            {
                if(board[i][col]!='T')
                    temp=board[i][col];
                n[board[i][col]]++;
            }
            if(((n[temp]==4)||(n[temp]==3&&n['T']==1))&&temp!='.')
            {
                printf("%c won\n",temp);
                won=1;
                break;
            }
        }
        if(won==1)
            continue;

        //Diagonal
        reset();
        for(i=0;i<4;i++)
        {

            if(board[i][i]!='T')
                temp=board[i][i];
            n[board[i][i]]++;
            if(((n[temp]==4)||(n[temp]==3&&n['T']==1))&&temp!='.')
            {
                printf("%c won\n",temp);
                won=1;
                break;
            }
        }
        if(won==1)
            continue;

        reset();
        for(i=0;i<4;i++)
        {
            if(board[i][3-i]!='T')
                temp=board[i][3-i];
            n[board[i][3-i]]++;
            if(((n[temp]==4)||(n[temp]==3&&n['T']==1))&&temp!='.')
            {
                printf("%c won\n",temp);
                won=1;
                break;
            }
        }
        if(won==1)
            continue;

        //else
        if(n['.']==0)
            printf("Draw\n");
        else
           printf("Game has not completed\n");

    }

    scanf(" ");
    return 0;
}
