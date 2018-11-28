#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>

using namespace std;

char board[5][5];
int ticTacCount(char ch){
    int mx = -1;
    int colsum[] = {0,0,0,0};
    int ldsum = 0, rdsum = 0;
    for(int i = 0; i < 4; i++){
        int rowSum = 0;
        for(int j = 0; j < 4; j++){
            if(board[i][j] == ch || board[i][j] == 'T'){
                rowSum++;
                colsum[j]++;
                if(i+j ==3){
                    ldsum++;
                    mx = max(ldsum, mx);
                }
                else if(i == j){
                    rdsum++;
                    mx = max(rdsum, mx);
                }
                mx = max(rowSum, mx);
                mx = max(colsum[j], mx);
            }
        }
    }
    return mx;
}

int main(){
    int t=1,T;
    scanf("%d",&T);
    while(t <= T){
        int dot = 0;
        for(int i=0; i <4; i++){
            scanf("%s",board[i]);
            if(NULL != strchr(board[i],'.')){
                dot++;
                //cerr<<board[i]<<"\n";
            }
        }
        int x = ticTacCount('X');
        int o = ticTacCount('O');
        if(x == 4)
            printf("Case #%d: %s\n",t,"X won");
        else if(o == 4)
            printf("Case #%d: %s\n",t,"O won");
        else if(dot >0)
            printf("Case #%d: %s\n",t,"Game has not completed");
        else if(dot == 0)
            printf("Case #%d: %s\n",t,"Draw");
        t++;
    }
}
