#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string>
#include<string.h>
char board[10][10];
int checker(int x,int y){
    bool b1,b2,b3,b4;
    b1=b2=b3=b4=true;
    if(board[x][y]=='.')return false;
    for(int i=0;i<4;i++){
        if(x+i>4||(board[x+i][y]!=board[x][y]&&board[x+i][y]!='T')){
            b1=false;
        }
        if(y+i>4||(board[x][y+i]!=board[x][y]&&board[x][y+i]!='T')){
            b2=false;
        }
        if(x+i>4||y+i>4||(board[x+i][y+i]!=board[x][y]&&board[x+i][y+i]!='T')){
            b3=false;
        }

        if(x-i<0||y+i>4||(board[x-i][y+i]!=board[x][y]&&board[x-i][y+i]!='T')){
            b4=false;
        }
    }
    return b1||b2||b3||b4;
}
void solve(){
    for(int i=0;i<4;i++){
        scanf("%s",board[i]);
    }
    bool sp=false;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(board[i][j]=='.')sp=true;
            if(board[i][j]=='T'){
                board[i][j]='X';
                if(checker(i,j)){
                    printf("%c won\n",board[i][j]);
                    return ;
                }
                board[i][j]='O';
                if(checker(i,j)){
                    printf("%c won\n",board[i][j]);
                    return ;
                }
                board[i][j]='T';
            }
            if(checker(i,j)){
                printf("%c won\n",board[i][j]);
                return ;
            }
        }
    }
    if(sp){
        printf("Game has not completed\n");
    }
    else printf("Draw\n");
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d\n",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
    }
}
