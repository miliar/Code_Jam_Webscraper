#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;

char map[6][6];
char *res1 = "X won";
char *res2 = "O won";
char *res3 = "Draw";
char *res4 = "Game has not completed";

int dir[10][4][2] = {
{{1,1},{2,2},{3,3},{4,4}},
{{1,4},{2,3},{3,2},{4,1}},
{{1,1},{1,2},{1,3},{1,4}},
{{2,1},{2,2},{2,3},{2,4}},
{{3,1},{3,2},{3,3},{3,4}},
{{4,1},{4,2},{4,3},{4,4}},
{{1,1},{2,1},{3,1},{4,1}},
{{1,2},{2,2},{3,2},{4,2}},
{{1,3},{2,3},{3,3},{4,3}},
{{1,4},{2,4},{3,4},{4,4}}
};

void Input(){
    for(int i = 1 ;i <= 4 ; i ++)
        for (int j = 1 ; j <= 4 ; j ++)
            cin >> map[i][j];
}

const char X  =  'X';
const char O = 'O';
const char T = 'T';
const char blank = '.';
int x1;        int y1;
int x2;        int y2;
int x3;        int y3;
int x4;        int y4;
const int x = 0;
const int y = 1;

bool X_won(){
    for(int i = 0 ;i < 10 ; i ++){
        x1 = dir[i][0][x];         y1 = dir[i][0][y];
        x2 = dir[i][1][x];         y2 = dir[i][1][y];
        x3 = dir[i][2][x];         y3 = dir[i][2][y];
        x4 = dir[i][3][x];         y4 = dir[i][3][y];
    if((map[x1][y1] == X && map[x2][y2]==X && map[x3][y3]==X && map[x4][y4]==X ) ||
           (map[x1][y1] == T && map[x2][y2]==X && map[x3][y3]==X && map[x4][y4]==X ) ||
           (map[x1][y1] == X && map[x2][y2]==T && map[x3][y3]==X && map[x4][y4]==X ) ||
           (map[x1][y1] == X && map[x2][y2]==X && map[x3][y3]==T && map[x4][y4]==X ) ||
           (map[x1][y1] == X && map[x2][y2]==X && map[x3][y3]==X && map[x4][y4]==T ))
           return true;
    }
    return false;
 }

bool O_won(){
    for(int i = 0 ;i < 10 ; i ++){
        x1 = dir[i][0][x];         y1 = dir[i][0][y];
        x2 = dir[i][1][x];         y2 = dir[i][1][y];
        x3 = dir[i][2][x];         y3 = dir[i][2][y];
        x4 = dir[i][3][x];         y4 = dir[i][3][y];
    if((map[x1][y1] == O && map[x2][y2]==O && map[x3][y3]==O && map[x4][y4]==O ) ||
           (map[x1][y1] == T && map[x2][y2]==O && map[x3][y3]==O && map[x4][y4]==O ) ||
           (map[x1][y1] == O && map[x2][y2]==T && map[x3][y3]==O && map[x4][y4]==O ) ||
           (map[x1][y1] == O && map[x2][y2]==O && map[x3][y3]==T && map[x4][y4]==O ) ||
           (map[x1][y1] == O && map[x2][y2]==O && map[x3][y3]==O && map[x4][y4]==T ))
           return true;
    }
    return false;
 }
bool noblank(){
    for(int i = 1 ;i <= 4 ; i ++)
        for (int j = 1 ; j <= 4 ; j ++)
            if(map[i][j] == blank)
                return false;
    return true;
}
char* bfs(){
    bool r1;
    bool r2;
    bool r3;
    bool r4;
    char * res;
    if((X_won() && O_won()) || (!X_won() && !O_won() && noblank()))
        return res = res3;
    if(X_won())
        return res = res1;
    if(O_won())
        return res = res2;
    if(!noblank())
        return res = res4;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int Ncase;
    cin >> Ncase;
    int ans = 0;
    while(Ncase--){
        Input();
        cout <<"Case #" << ++ans << ": "<< bfs() << endl;
    }
    return 0;
}
