#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int gi(){
    int t; scanf("%d",&t);
    return t;
}

int main(){
    for(int test=1, t=gi(); test<=t; test++){
        int h=gi(), w=gi();
        int board[h][w];
        memset(board, 0, h*w*4);
        for(int j=gi(); j--;){
            int rr=gi()-1, c=gi()-1;
            board[rr][c]=-1;
        }
        board[0][0]=1;

        for(int y=0; y<h; y++)
            for(int x=0; x<w; x++)
                if(board[y][x]!=-1){
                    if(x-2>=0 && y-1>=0 && board[y-1][x-2]!=-1)
                        board[y][x]+=board[y-1][x-2];
                    if(x-1>=0 && y-2>=0 && board[y-2][x-1]!=-1)
                        board[y][x]+=board[y-2][x-1];
                    board[y][x]%=10007;
                }

        printf("Case #%d: %d\n", test, board[h-1][w-1]);
    }
    return 0;
}
