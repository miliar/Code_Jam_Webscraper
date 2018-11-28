#include<iostream>
#include<cstdio>
#include<string.h>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;

char s[10][10];

int win(char c){
    for(int i=0;i<4;i++){
        bool flag = true;
        for(int j=0;j<4;j++){
            if(s[i][j]!=c&&s[i][j]!='T')
                flag = false;
        }
        if(flag) return 1;
    }
    for(int j=0;j<4;j++){
        bool flag = true;
        for(int i=0;i<4;i++){
            if(s[i][j]!=c&&s[i][j]!='T')
                flag = false;
        }
        if(flag) return 1;
    }
    bool flag = true;
    for(int i=0;i<4;i++){
        if(s[i][i]!=c&&s[i][i]!='T')
            flag = false;
    }
    if(flag) return 1;
    flag = true;
    for(int i=0;i<4;i++){
        if(s[i][3-i]!=c&&s[i][3-i]!='T')
            flag = false;
    }
    if(flag) return 1;
    return 0;
}

int endGame(){
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(s[i][j]=='.') return 0;
        }
    }
    return 1;
}

int main(){
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        getchar();
        for(int i=0;i<4;i++)
            scanf("%s",s[i]);
        printf("Case #%d: ",cas);
        if(win('X')) printf("X won\n");
        else if(win('O')) printf("O won\n");
        else if(endGame()) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
