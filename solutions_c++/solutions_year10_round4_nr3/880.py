#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;
#define SIZE 104

#define REP(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define REP1(i,n) for (int (i)=1;(i)<(int)(n);++(i))

int alive(int board[][SIZE]){
    int sum=0;
    REP1(i,SIZE) REP1(j,SIZE){
        sum+=board[i][j];
    }
    return sum;
}

int main(){
    int cases=0;
    int casenr=0;
    scanf("%d", &cases);

    while (--cases >=0){
        ++casenr;
        int blocks=0;
        scanf("%d", &blocks);
        int board[SIZE][SIZE] = {0};
        REP(i, blocks){
            int x1,y1,x2,y2;
            scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
            for (int j=x1;j<=x2;j++){
                for (int k=y1;k<=y2;k++){
                    board[j][k]=1;
                }
            }
        }
        //ITERATE!!!!!
        int reps=0;
        while (alive(board)>0){
            int newboard[SIZE][SIZE] = {0};
            REP(i, SIZE) REP(j, SIZE){
                newboard[i][j]=board[i][j];
                if (!((i>=0 && board[i-1][j] == 1) ||
                    (j>=0 && board[i][j-1] == 1))) newboard[i][j]=0;
                if (((i>=0 && board[i-1][j] == 1) &&
                    (j>=0 && board[i][j-1] == 1))) newboard[i][j]=1;
            }
            //board=newboard;
            //CPP sucks!
            REP(i, SIZE) REP(j, SIZE){
                board[i][j] = newboard[i][j];
            }
            ++reps;
        }
        printf("Case #%d: %d\n", casenr, reps);
    }

    return 0;
}
