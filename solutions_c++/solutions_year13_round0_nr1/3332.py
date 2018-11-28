#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
char chkwon(char board[][4],char ch,int crr,int corr)
{
    if(corr==1)
    {
        for(int i=1;i<4;i++)
        {
            if(board[crr][i]!=ch&&board[crr][i]!='T')return '.';
        }
    }
    else if(corr==2)
    {
        for(int i=1;i<4;i++)
        {
            if(board[i][crr]!=ch&&board[i][crr]!='T')return '.';
        }
    }
    else if(corr==3)
    {
        for(int i=1;i<4;i++)
        {
            if(board[i][i]!=ch&&board[i][i]!='T')return '.';
        }
    }
    else if(corr==4)
    {
        for(int i=1;i<4;i++)
        {
            //printf("%c %c\n",board[i][4-i-1],ch);
            if(board[i][4-i-1]!=ch&&board[i][4-i-1]!='T')return '.';
        }
    }
    return ch;
}
char won(char board[][4])
{
    char winner='.';
    for(int i=0;i<4;i++)
    {
        if(board[i][0]=='X')winner=chkwon(board,'X',i,1);
        else if(board[i][0]=='O')winner=chkwon(board,'O',i,1);
        else if(board[i][0]=='T')
        {
            winner=chkwon(board,'X',i,1);
            if(winner!='.')return  winner;
            winner=chkwon(board,'O',i,1);
        }
        if(winner!='.')return winner;
        if(board[0][i]=='X')winner=chkwon(board,'X',i,2);
        else if(board[0][i]=='O')winner=chkwon(board,'O',i,2);
        else if(board[0][i]=='T')
        {
            winner=chkwon(board,'X',i,2);
            if(winner!='.')return  winner;
            winner=chkwon(board,'O',i,2);
        }
        if(winner!='.')return winner;
    }
    if(board[0][0]=='T')
    {
        winner=chkwon(board,'X',0,3);
        if(winner!='.')return winner;
        winner=chkwon(board,'O',0,3);
    }
    else if(board[0][0]!='.')winner=chkwon(board,board[0][0],0,3);
    if(winner!='.')return winner;
    if(board[0][3]=='T')
    {
        winner=chkwon(board,'X',0,4);
        //printf("%c\n",winner);
        if(winner!='.')return winner;
        winner=chkwon(board,'O',0,4);
        //if(winner!='.')return winner;
    }
    else if(board[0][3]!='.')
    {
        //printf("test\n");
        winner=chkwon(board,board[0][3],0,4);
    }
    return winner;
}
main()
{
	int n;
	scanf("%d",&n);
	for(int k=1;k<=n;k++)
	{
		char board[4][4];
		bool isfin=true;
		for(int i=0;i<4;i++)
		{
		    scanf(" ");
		    for(int j=0;j<4;j++)
		    {
		        scanf("%c",&board[i][j]);
		        if(board[i][j]=='.')isfin=false;
		    }
		}
		char chk=won(board);
		printf("Case #%d: ",k);
		if(chk!='.')printf("%c won\n",chk);
		else if(!isfin)printf("Game has not completed\n");
		else  printf("Draw\n");
	}
}
