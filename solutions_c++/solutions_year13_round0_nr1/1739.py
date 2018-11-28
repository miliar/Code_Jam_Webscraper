
#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

using namespace std;

bool fourinarow(char grid[4][4], char c){
    for(int a=0; a<4; a++){
        if((grid[a][0]==c||grid[a][0]=='T') && (grid[a][1]==c||grid[a][1]=='T') && (grid[a][2]==c||grid[a][2]=='T') && (grid[a][3]==c||grid[a][3]=='T')){
            return true;
        }
        if((grid[0][a]==c||grid[0][a]=='T') && (grid[1][a]==c||grid[1][a]=='T') && (grid[2][a]==c||grid[2][a]=='T') && (grid[3][a]==c||grid[3][a]=='T')){
            return true;
        }
    }
    if((grid[0][0]==c||grid[0][0]=='T') && (grid[1][1]==c||grid[1][1]=='T') && (grid[2][2]==c||grid[2][2]=='T') && (grid[3][3]==c||grid[3][3]=='T')){
        return true;
    }
    if((grid[0][3]==c||grid[0][3]=='T') && (grid[1][2]==c||grid[1][2]=='T') && (grid[2][1]==c||grid[2][1]=='T') && (grid[3][0]==c||grid[3][0]=='T')){
        return true;
    }
    return false;
}

int filledin(char grid[4][4]){
    int total=0;
    for(int a=0; a<4; a++){
        for(int b=0; b<4; b++){
            if(grid[a][b]=='X' || grid[a][b]=='O' || grid[a][b]=='T'){
                total++;
            }
        }
    }
    return total;
}

int main()
{
    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    char grid[4][4];
    int cases;
    fin >> cases;
    for(int c=1; c<=cases; c++){
        for(int a=0; a<4; a++){
            for(int b=0; b<4; b++){
                fin >> grid[a][b];
            }
        }
        if(fourinarow(grid, 'X')){
            fout << "Case #"<< c <<": X won" << endl;
        }
        else{
            if(fourinarow(grid, 'O')){
                fout << "Case #"<< c <<": O won" << endl;
            }
            else{
                if(filledin(grid)==16){
                   fout << "Case #"<< c <<": Draw" << endl;
                }
                else {
                    fout << "Case #"<< c <<": Game has not completed" << endl;
                }
            }
        }

    }
}
