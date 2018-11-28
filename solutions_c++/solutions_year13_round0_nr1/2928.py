#include<cstdio>
#include<algorithm>

int T;
char board[5][5];
char result(){
    int i,j;
    for(i=0;i<4;i++){
        for(j=1;j<4;j++){
            if(board[i][j]!=board[i][j-1]||board[i][j]=='.')break;
        }
        if(j==4){
            return board[i][0];
        }
    }
    for(i=0;i<4;i++){
        for(j=1;j<4;j++){
            if(board[j][i]!=board[j-1][i]||board[j][i]=='.')break;
        }
        if(j==4){
            return board[0][i];
        }
    }
    for(j=1;j<4;j++){
        if(board[j][j]!=board[j-1][j-1]||board[j][j]=='.')break;
    }
    if(j==4){
        return board[0][0];
    }

    for(j=1;j<4;j++){
        if(board[j][3-j]!=board[j-1][4-j]||board[j][3-j]=='.')break;
    }
    if(j==4){
        return board[0][3];
    }
    return 0;
}
bool complete(){
    int i,j;
    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            if(board[i][j]=='.')return false;
        }
    }
    return true;
}

int main(){
    int i,j,k;
    scanf("%d",&T);
    int t;
    int p;
    for(t=1;t<=T;t++){
        printf("Case #%d: ",t);
        for(i=0;i<4;i++){
            scanf("%s",board[i]);
        }
        scanf("\n");
        for(p=0;p<16;p++){
            if(board[p/4][p%4]=='T')break;
        }
        board[p/4][p%4]='X';
        char r=result();
        if(r==0){
            board[p/4][p%4]='O';
            r=result();
        }
        bool c=complete();
        if(r!=0)printf("%c won\n",r);
        else if(c)printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}

