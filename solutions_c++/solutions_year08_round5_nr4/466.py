#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<vector>
#include<string>
#include<set>
using namespace std;

#define MOD 10007

int T, w, h, n;
int board[101][101];


int main() {
    scanf("%d",&T);
    for(int z=0;z<T;z++) {
        scanf("%d %d %d",&h,&w,&n);
        memset(board,0,sizeof(board));
        board[1][1] = 1;
        for(int i=0;i<n;i++) {
            int t1, t2;
            scanf("%d %d",&t1,&t2);
            board[t1][t2] = -1;
        }
        for(int i=1;i<=h;i++) {
            for(int j=1;j<=w;j++) {
                if(board[i][j] == -1) continue;
                if(i+1 <= h && j+2 <= w && board[i+1][j+2] != -1) {
                    board[i+1][j+2] += board[i][j];
                    board[i+1][j+2] %= MOD;
                }
                if(i+2 <= h && j+1 <= w && board[i+2][j+1] != -1) {
                    board[i+2][j+1] += board[i][j];
                    board[i+2][j+1] %= MOD;
                }
            }
        }        
        printf("Case #%d: %d\n",z+1,board[h][w]);
    }
    return 0;
} 
            
        
