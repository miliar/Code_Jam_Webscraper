#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
char grid[4][4];

char merge(char a,char b){
    if(a==b)
        return a;
    if(a=='T')
        return b;
    if(b=='T')
        return a;
    return '.';
}

void win(char w){
    printf("%c won\n",w);
}

void draw(){
    printf("Draw\n");
}
void not_complete(){
    printf("Game has not completed\n");
}

void check_grid(){
    //check vert and horizontal
    for(int i=0;i<4;i++){
        char currv=grid[0][i],currh=grid[i][0];
        for(int j=1;j<4;j++){
            currv = merge(currv,grid[j][i]);
            currh = merge(currh,grid[i][j]);
        }
        if(currv=='X' || currh=='X'){
            win('X');
            return;
        }
        if(currv=='O' || currh=='O'){
            win('O');
            return;
        }
    }
    //check diagonals
    char currl=grid[0][0],currr=grid[0][3];
    for(int i=1;i<4;i++){
        currl = merge(currl,grid[i][i]);
        currr = merge(currr,grid[i][3-i]);
    }
    if(currl=='X' || currr=='X'){
        win('X');
        return;
    }
    if(currl=='O' || currr=='O'){
        win('O');
        return;
    }
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(grid[i][j]=='.'){
                not_complete();
                return;
            }
        }
    }
    draw();
    return;
}

int main(){
    int T;
    cin >> T;
    for(int k=0;k<T;k++){
        string line;
        getline(cin,line);
        for(int i=0;i<4;i++){
            getline(cin,line);
            for(int j=0;j<4;j++){
                grid[i][j] = line[j];
            }
        }
        printf("Case #%d: ",k+1);
        check_grid();
    }
}
