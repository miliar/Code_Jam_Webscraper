#include<stdio.h>
using namespace std;

const int N = 110;

char map[N][N];

bool is_empty;

void read(){
    is_empty = false;
    char s[10];
    for(int i=0; i<4; i++){
        scanf("%s",map[i]);
        for(int j=0; j<4; j++)
            if(map[i][j]=='.') is_empty = true;
    }
}
bool judge(char who){
    for(int i=0; i<4; i++){
        int sum = 0;
        for(int j=0; j<4; j++)
            if(map[i][j]==who || map[i][j]=='T')
                sum++;
        if(sum==4)  return true;
    }
    for(int j=0; j<4; j++){
        int sum = 0;
        for(int i=0; i<4; i++)
            if(map[i][j]==who || map[i][j]=='T')
                sum++;
        if(sum==4)  return true;
    }
    for(int i=0; i<4; i++){
        int sum = 0;
        for(int j=0; j<4; j++)
            if(map[j][j]==who || map[j][j]=='T')
                sum++;
        if(sum==4)  return true;
    }
    for(int i=0; i<4; i++){
        int sum = 0;
        int x=0,y=3;
        for(int j=0; j<4; j++){
            if(map[x][y]==who || map[x][y]=='T')
                sum++;
            x++; y--;
        }
        if(sum==4)  return true;
    }
    return false;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int _, cnt=1;
    scanf("%d", &_);
    while(_--){
        read();
        bool X = judge('X');
        bool O = judge('O');
        printf("Case #%d: ", cnt++);
        if(X==false && O==false){
            if(is_empty)   printf("Game has not completed\n");
            else        printf("Draw\n");
        }
        else{
            if(X)   printf("X won\n");
            else    printf("O won\n");
        }
    }
    return 0;
}
