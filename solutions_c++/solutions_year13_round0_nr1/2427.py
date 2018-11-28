#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

char board[4][4];
int dir[4][2]={1,1,
               1,0,
               0,1,
               1,-1};

int search( int x , int y , int direct ){
    char ch = board[x][y];
    for(int i=0;i<4;++i)
        if (board[ x+dir[direct][0]*i ][ y+dir[direct][1]*i ]!=ch &&
            board[ x+dir[direct][0]*i ][ y+dir[direct][1]*i ]!='T')
            return 0;
    return ch;
}
int work(){
    int win[255];
    memset(win,0,sizeof(win));
    for (int i=0;i<4;++i)
        if (board[0][i]=='T'){
            board[0][i]='O';
            win[ search(0,i,1) ] ++;
            board[0][i]='X';
            win[ search(0,i,1) ] ++;  
            board[0][i]='T';          
        }else
            win[ search(0,i,1) ]++;
            
    for (int i=0;i<4;++i)
        if (board[i][0]=='T'){
            board[i][0]='O';
            win[ search(i,0,2) ] ++;
            board[i][0]='X';
            win[ search(i,0,2) ] ++;  
            board[i][0]='T';          
        }else
            win[ search(i,0,2) ]++;

        if (board[0][3]=='T'){
            board[0][3]='O';
            win[ search(0,3,3) ] ++;
            board[0][3]='X';
            win[ search(0,3,3) ] ++;  
            board[0][0]='T';          
        }else
            win[ search(0,3,3) ]++;

        if (board[0][0]=='T'){
            board[0][0]='O';
            win[ search(0,0,0) ] ++;
            board[0][0]='X';
            win[ search(0,0,0) ] ++;  
            board[0][0]='T';          
        }else
            win[ search(0,0,0) ]++;

        if (win['X'] && !win['O'])
            printf("X won\n");
        else if (win['O'] && !win['X'])
            printf("O won\n");
        else{

            for (int i=0;i<4;++i)
            for (int j=0;j<4;++j)
                if (board[i][j]!='T' &&
                    board[i][j]!='O' &&
                    board[i][j]!='X'){
                        printf("Game has not completed\n");
                        return 0;
                    }

             printf("Draw\n");

             
         }
            
}
int init(){
    for (int i=0;i<4;++i){
        for (int j=0;j<4;++j)
            scanf("%c",&board[i][j]);
        scanf("\n");
    }
        scanf("\n");
}
int main(){
    int t;
    scanf("%d\n",&t);
    for(int i=1;i<=t;++i){
        init();
        printf("Case #%d: ",i);
        work();
    }
}
