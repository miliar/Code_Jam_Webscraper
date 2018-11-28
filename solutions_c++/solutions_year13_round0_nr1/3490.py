#include <iostream>
#include <string>
#include <fstream>
using namespace std;

ofstream out("output.txt");

char grid[4][5];
int cases;

int c(string s, char lol){
    int C=0;
    for(int i = 0; i < s.size(); i++){
        if(s[i] == lol) C++;
    }
    return C;
}
int g(char a, char b, char e, char d, char lol, char lol2){
    int C=0;
    if(a==lol||a==lol2) C++;
    if(b==lol||b==lol2) C++;
    if(e==lol||e==lol2) C++;
    if(d==lol||d==lol2) C++;
    return C;
}

int main(){
    cin>>cases;
    for(int d = 1; d <= cases; d++){
        for(int i = 0; i < 4; i++) cin>>grid[i];
        // check vert
        bool xwin = false, owin = false, hasEmpty = false;
        // check horizontal
        for(int i = 0; i < 4; i++){
            int xsum = c(grid[i],'X') + c(grid[i],'T');
            int osum = c(grid[i],'O') + c(grid[i],'T');
            int dot = c(grid[i],'.');
            if(dot) hasEmpty = true;
            if(xsum == 4) xwin = true;
            if(osum == 4) owin = true;
        }
        // check vertical
        for(int i = 0; i < 4; i++){
            int xsum = g(grid[0][i],grid[1][i],grid[2][i],grid[3][i],'X','T');
            int osum = g(grid[0][i],grid[1][i],grid[2][i],grid[3][i],'O','T');
            if(xsum == 4) xwin = true;
            if(osum == 4) owin = true;
        }
        // check diagonal

        int xsum = g(grid[0][0],grid[1][1],grid[2][2],grid[3][3],'X','T');
        int osum = g(grid[0][0],grid[1][1],grid[2][2],grid[3][3],'O','T');
        if(xsum == 4) xwin = true;
        if(osum == 4) owin = true;
        xsum = g(grid[0][3],grid[1][2],grid[2][1],grid[3][0],'X','T');
        osum = g(grid[0][3],grid[1][2],grid[2][1],grid[3][0],'O','T');
        if(xsum == 4) xwin = true;
        if(osum == 4) owin = true;

        // check status
        if(xwin){
            out<<"Case #"<<d<<": X won\n";
        }else if(owin){
            out<<"Case #"<<d<<": O won\n";
        }else if(hasEmpty){
            out<<"Case #"<<d<<": Game has not completed\n";
        }else{
            out<<"Case #"<<d<<": Draw\n";
        }
    }
}
