#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int main() {
    int T,pos1,pos2;
    char ch;
    string str[5];
    bool draw,x,o,t;
    scanf("%d",&T);
    for(int z=1;z<=T;z++) {
        draw=true;
        t=false;
        for(int a=0;a<4;a++) {
            cin >> str[a];
        }
        for(int a=0;a<4;a++) for(int b=0;b<4;b++) {
            if(str[a][b]=='T') {
                t=true;
                pos1=a;
                pos2=b;
            }
            if(str[a][b]=='.') draw=false;
        }
        if(t) str[pos1][pos2]='X';
        x=false;
        o=false;
        for(int a=0;a<4;a++) {
            if(str[a][0]=='X' && str[a][0]==str[a][1] && str[a][0]==str[a][2] && str[a][0]==str[a][3]) {x=true;break;}
            if(str[0][a]=='X' && str[0][a]==str[1][a] && str[0][a]==str[2][a] && str[0][a]==str[3][a]) {x=true;break;}
        }
        if(str[0][0]=='X' && str[0][0]==str[1][1] && str[0][0]==str[2][2] && str[0][0]==str[3][3]) x=true;
        if(str[3][0]=='X' && str[3][0]==str[2][1] && str[3][0]==str[1][2] && str[3][0]==str[0][3]) x=true;
        if(t)str[pos1][pos2]='O';
        for(int a=0;a<4;a++) {
            if(str[a][0]=='O' && str[a][0]==str[a][1] && str[a][0]==str[a][2] && str[a][0]==str[a][3]) {o=true;break;}
            if(str[0][a]=='O' && str[0][a]==str[1][a] && str[0][a]==str[2][a] && str[0][a]==str[3][a]) {o=true;break;}
        }
        if(str[0][0]=='O' && str[0][0]==str[1][1] && str[0][0]==str[2][2] && str[0][0]==str[3][3]) o=true;
        if(str[3][0]=='O' && str[3][0]==str[2][1] && str[3][0]==str[1][2] && str[3][0]==str[0][3]) o=true;
        if(o) printf("Case #%d: O won\n",z);
        if(x) printf("Case #%d: X won\n",z);
        if(!o && !x && draw) printf("Case #%d: Draw\n",z);
        if(!o && !x && !draw) printf("Case #%d: Game has not completed\n",z);
    }
    return 0;
} 
        
