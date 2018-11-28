#include<iostream>
#include<cstdio>
using namespace std;
int t;
char p[10][10];
bool lft, down, gg, minor, major;
int main(){
    scanf("%d", &t);
    for(int tc = 0; tc < t; ++tc){
        gg = true;
        for(int i = 0; i < 4; ++i) scanf("%s", p[i]);
        //check O
        for(int i = down = lft = 0; i < 4 && gg; ++i){
            lft = down = false;
            for(int j = 0; j < 4; ++j){
                if(p[i][j] != 'T' && p[i][j] != 'O') lft = true;
                if(p[j][i] != 'T' && p[j][i] != 'O') down = true;
            }
            if(!lft||!down) gg = false;
        }
        //check diagonal
        for(int i = major = minor = 0; gg && i < 4; ++i){
            if(p[i][i] != 'T' && p[i][i] != 'O') major = true;
            if(p[3-i][i] != 'T' && p[3-i][i] != 'O') minor = true;
        }
        if(!minor||!major) gg = false;
        if(!gg){
            printf("Case #%d: O won\n", tc+1);
            continue;
        }
        
        
        //check X
        for(int i = down = lft = 0; i < 4 && gg; ++i){
            lft = down = false;
            for(int j = 0; j < 4; ++j){
                if(p[i][j] != 'T' && p[i][j] != 'X') lft = true;
                if(p[j][i] != 'T' && p[j][i] != 'X') down = true;
            }
            if(!lft||!down) gg = false;
        }
        //check diagonal
        for(int i = major = minor = 0; gg && i < 4; ++i){
            if(p[i][i] != 'T' && p[i][i] != 'X') major = true;
            if(p[3-i][i] != 'T' && p[3-i][i] != 'X') minor = true;
        }
        if(!minor||!major) gg = false;
        if(!gg) printf("Case #%d: X won\n", tc+1);
        else{
            bool nodraw = false;
            for(int i = 0; i < 4; ++i)
                for(int j = 0; j < 4; ++j)
                    nodraw |= p[i][j] == '.';
            if(nodraw) printf("Case #%d: Game has not completed\n", tc+1);
            else printf("Case #%d: Draw\n", tc+1);
        }
    }
}
