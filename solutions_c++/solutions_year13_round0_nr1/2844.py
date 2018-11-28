#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<list>
#include<utility>
#include<string.h>
using namespace std;
char data[4][4];
int charsInRow(int row, char ch){
    int cnt = 0;
    for(int i=0;i<4;i++) if(data[row][i]==ch || data[row][i]=='T'){
        cnt++;
    }
    return cnt;
}
int charsInCol(int col, char ch){
    int cnt = 0;
    for(int i=0;i<4;i++) if(data[i][col]==ch || data[i][col]=='T'){
        cnt++;
    }
    return cnt;
}

int charsIn1Diag(char ch){
    int cnt = 0;
    for(int i=0;i<4;i++) if(data[i][i]==ch || data[i][i]=='T'){
        cnt++;
    }
    return cnt;
}
int charsIn2Diag(char ch){
    int cnt = 0;
    for(int i=0;i<4;i++) if(data[i][3-i]==ch || data[i][3-i]=='T'){
        cnt++;
    }
    return cnt;
}


int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    char line[4], ch;
    scanf("%d", &T);
    for(int c=0;c<T;c++){
        bool completed = true;
        for(int i=0;i<4;i++){
            scanf("%s",&line);
            for(int j=0;j<4;j++){
                ch = line[j];
                if(ch=='.') completed = false;
                data[i][j] = ch;
            }
        }

        int winner = -1;
        for(int i=0;i<4 && winner==-1;i++){
            int rxs =  charsInRow(i,'X');
            int cxs =  charsInCol(i,'X');

            int ros =  charsInRow(i,'O');
            int cos =  charsInCol(i,'O');
            if(rxs==4 || cxs==4) winner = 1;
            else if(ros==4 || cos==4) winner = 0;
        }
        /*
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++) printf("%c",data[i][j]);
            printf("\n");
        }
        */
        if(winner==-1){
            int d1xs = charsIn1Diag('X');
            int d2xs = charsIn2Diag('X');

            int d1os = charsIn1Diag('O');
            int d2os = charsIn2Diag('O');
            if(d1xs==4 || d2xs==4) winner = 1;
            else if(d1os==4 || d2os==4) winner = 0;
        }

        if(winner==-1 && completed) printf("Case #%d: Draw\n",c+1);
        else if(winner==0) printf("Case #%d: O won\n",c+1);
        else if(winner==1) printf("Case #%d: X won\n",c+1);
        else printf("Case #%d: Game has not completed\n",c+1);
    }
    return 0;
}
