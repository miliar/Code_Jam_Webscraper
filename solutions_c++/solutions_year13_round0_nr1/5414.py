#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

char ch[5][5];

int full,xw,ow;
int T;

int xj(char c){
    if(c=='X'||c=='T') return 1;
    return 0;
}

int oj(char c){
    if(c=='O'||c=='T') return 1;
    return 0;
}
void judgex(){
    if(xj(ch[0][0])&&xj(ch[0][1])&&xj(ch[0][2])&&xj(ch[0][3])){
        xw=1;return;
    }
    if(xj(ch[1][0])&&xj(ch[1][1])&&xj(ch[1][2])&&xj(ch[1][3])){
        xw=1;return;
    }
    if(xj(ch[2][0])&&xj(ch[2][1])&&xj(ch[2][2])&&xj(ch[2][3])){
        xw=1;return;
    }
    if(xj(ch[3][0])&&xj(ch[3][1])&&xj(ch[3][2])&&xj(ch[3][3])){
        xw=1;return;
    }
    if(xj(ch[0][0])&&xj(ch[1][0])&&xj(ch[2][0])&&xj(ch[3][0])){
        xw=1;return;
    }
    if(xj(ch[0][1])&&xj(ch[1][1])&&xj(ch[2][1])&&xj(ch[3][1])){
        xw=1;return;
    }if(xj(ch[0][2])&&xj(ch[1][2])&&xj(ch[2][2])&&xj(ch[3][2])){
        xw=1;return;
    }if(xj(ch[0][3])&&xj(ch[1][3])&&xj(ch[2][3])&&xj(ch[3][3])){
        xw=1;return;
    }
    if(xj(ch[0][0])&&xj(ch[1][1])&&xj(ch[2][2])&&xj(ch[3][3])){
        xw=1;return;
    }
    if(xj(ch[0][3])&&xj(ch[1][2])&&xj(ch[2][1])&&xj(ch[3][0])){
        xw=1;return;
    }
}

void judgeo(){
    if(oj(ch[0][3])&&oj(ch[1][2])&&oj(ch[2][1])&&oj(ch[3][0])){
        ow=1;return;
    }
    if(oj(ch[0][0])&&oj(ch[1][1])&&oj(ch[2][2])&&oj(ch[3][3])){
        ow=1;return;
    }
    if(oj(ch[0][0])&&oj(ch[0][1])&&oj(ch[0][2])&&oj(ch[0][3])){
        ow=1;return;
    }
    if(oj(ch[1][0])&&oj(ch[1][1])&&oj(ch[1][2])&&oj(ch[1][3])){
        ow=1;return;
    }
    if(oj(ch[2][0])&&oj(ch[2][1])&&oj(ch[2][2])&&oj(ch[2][3])){
        ow=1;return;
    }
    if(oj(ch[3][0])&&oj(ch[3][1])&&oj(ch[3][2])&&oj(ch[3][3])){
        ow=1;return;
    }
    if(oj(ch[0][0])&&oj(ch[1][0])&&oj(ch[2][0])&&oj(ch[3][0])){
        ow=1;return;
    }
    if(oj(ch[0][1])&&oj(ch[1][1])&&oj(ch[2][1])&&oj(ch[3][1])){
        ow=1;return;
    }
    if(oj(ch[0][2])&&oj(ch[1][2])&&oj(ch[2][2])&&oj(ch[3][2])){
        ow=1;return;
    }
    if(oj(ch[0][3])&&oj(ch[1][3])&&oj(ch[2][3])&&oj(ch[3][3])){
        ow=1;return;
    }
}

int main()
{
    int T,cs=0;
    cin>>T;
    while(T--){
        cs++;
        getchar();
        for(int i=0;i<4;++i) scanf("%s",ch[i]);
        full=1;xw=0;ow=0;
        judgex();judgeo();
        if(xw){
            printf("Case #%d: X won\n",cs);
            continue;
        }
        else if(ow){
            printf("Case #%d: O won\n",cs);
            continue;
        }
        else{
            for(int i=0;i<4;++i)
            for(int j=0;j<4;++j){
                if(ch[i][j]=='.'){
                    full=0;
                    break;
                }
            }
            if(full) printf("Case #%d: Draw\n",cs);
            else printf("Case #%d: Game has not completed\n",cs);
        }
    }
    return 0;
}
