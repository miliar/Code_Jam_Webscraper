#include<stdio.h>

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    
    
    bool winX,winO,end;
    char board[6][6];
    int T,cases,i,j;
    scanf("%d",&T);
    for(cases=1;cases<=T;cases++){
        for(i=0;i<4;i++)scanf("%s",board[i]);
        winX=winO=false;
        end=true;
        bool winx,wino;
        for(i=0;i<4;i++){
            winx=wino=true;
            for(j=0;j<4;j++){
                if(board[i][j]=='.')end=false;
                if(board[i][j]!='X' && board[i][j]!='T')winx=false;
                if(board[i][j]!='O' && board[i][j]!='T')wino=false;
            }
            winX|=winx;
            winO|=wino;
        }
        for(j=0;j<4;j++){
            winx=wino=true;
            for(i=0;i<4;i++){
                if(board[i][j]!='X' && board[i][j]!='T')winx=false;
                if(board[i][j]!='O' && board[i][j]!='T')wino=false;
            }
            winX|=winx;
            winO|=wino;
        }
            winx=wino=true;
            for(i=0;i<4;i++){
                if(board[i][i]!='X' && board[i][i]!='T')winx=false;
                if(board[i][i]!='O' && board[i][i]!='T')wino=false;
            }
            winX|=winx;
            winO|=wino;
            
            winx=wino=true;
            for(i=0;i<4;i++){
                if(board[i][4-i-1]!='X' && board[i][4-i-1]!='T')winx=false;
                if(board[i][4-i-1]!='O' && board[i][4-i-1]!='T')wino=false;
            }
            winX|=winx;
            winO|=wino;
            
        if(winX)printf("Case #%d: X won\n",cases);
        else if(winO)printf("Case #%d: O won\n",cases);
        else if(!end)printf("Case #%d: Game has not completed\n",cases);
        else printf("Case #%d: Draw\n",cases);
    }
}
