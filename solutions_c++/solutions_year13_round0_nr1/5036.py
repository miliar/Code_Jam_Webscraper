#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

const char* str[] = {"Game has not completed", "X won", "O won", "Draw"};

int gao(char a, char b, char c, char d){
    int x=0,o=0,t=0;
    if(a=='X') x++; if(a=='O') o++; if(a=='T') t++;
    if(b=='X') x++; if(b=='O') o++; if(b=='T') t++;
    if(c=='X') x++; if(c=='O') o++; if(c=='T') t++;
    if(d=='X') x++; if(d=='O') o++; if(d=='T') t++;
    if(x==4 || (x==3 && t==1)) return 1;
    if(o==4 || (o==3 && t==1)) return 2;
    return 0;
}

int main(){
    int cs,no=0;
    scanf("%d",&cs);
    while(cs--){
        int ans=0;
        char a[4][6];
        for(int i=0;i<4;i++) scanf("%s",a[i]);
        for(int i=0;i<4;i++) ans|=gao(a[i][0],a[i][1],a[i][2],a[i][3]);
        for(int i=0;i<4;i++) ans|=gao(a[0][i],a[1][i],a[2][i],a[3][i]);
        ans|=gao(a[0][0],a[1][1],a[2][2],a[3][3]);
        ans|=gao(a[0][3],a[1][2],a[2][1],a[3][0]);
        if(!ans){
            int empty=0;
            for(int i=0;i<4;i++) for(int j=0;j<4;j++)
                if(a[i][j]=='.') empty=1;
            if(!empty) ans|=3;
        }
        printf("Case #%d: %s\n",++no,str[ans]);
    }
}
