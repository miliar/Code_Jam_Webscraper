#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<cstdio>
#include <algorithm>
#include<cstring>
#include<cmath>
#include <fstream>
using namespace std;
int N=0,p=0;
int main () {
    freopen("Tic-Tac-Toe-Tomek.in","r",stdin);
    freopen("Tic-Tac-Toe-Tomek.out","w",stdout);
    scanf("%d\n",&N);
    for(p=1;p<=N;p++){
        int i=0,j=0,X=0,O=0,T=0,stop=0;
        char board[10][10];
        for(i=0;i<4;i++){
            cin.getline(board[i],10);
        }
        scanf("\n");
        printf("Case #%d: ",p);
        //printf("Start\n");for(i=0;i<4;i++){printf("%s\n",board[i]);}
        for(i=0;i<4;i++){
            X=0;O=0;T=0;
            for(j=0;j<4;j++){
                if(board[i][j]=='X'){X++;}
                if(board[i][j]=='O'){O++;}
                if(board[i][j]=='T'){T++;}
            }
            if((X==3&&T==1)||(X==4)){printf("X won\n");goto end;}
            if((O==3&&T==1)||(O==4)){printf("O won\n");goto end;}
        }
        for(j=0;j<4;j++){
            X=0;O=0;T=0;
            for(i=0;i<4;i++){
                if(board[i][j]=='X'){X++;}
                if(board[i][j]=='O'){O++;}
                if(board[i][j]=='T'){T++;}
            }
            if((X==3&&T==1)||(X==4)){printf("X won\n");goto end;}
            if((O==3&&T==1)||(O==4)){printf("O won\n");goto end;}
        }
        j=-1;
        X=0;O=0;T=0;
        for(i=0;i<4;i++){
            j++;
            if(board[i][j]=='X'){X++;}
            if(board[i][j]=='O'){O++;}
            if(board[i][j]=='T'){T++;}
        }
        if((X==3&&T==1)||(X==4)){printf("X won\n");goto end;}
        if((O==3&&T==1)||(O==4)){printf("O won\n");goto end;}
        j=4;
        X=0;O=0;T=0;
        for(i=0;i<4;i++){
            j--;
            if(board[i][j]=='X'){X++;}
            if(board[i][j]=='O'){O++;}
            if(board[i][j]=='T'){T++;}
        }
        if((X==3&&T==1)||(X==4)){printf("X won\n");goto end;}
        if((O==3&&T==1)||(O==4)){printf("O won\n");goto end;}
        stop=0;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                if(board[i][j]=='.'){
                    stop++;
                }
            }
        }
        if(stop==0)printf("Draw\n");
        else printf("Game has not completed\n");
        end:;
    }
    return 0;
}
