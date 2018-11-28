#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

int counter(int* num,char a) {
    if(a == 'X') ++num[0];
    else if(a == 'O') ++num[1];
    else if(a == 'T') ++num[2];
    else ++num[3];
}

int check(const vector<string>& grid) {
    bool dot = false;
    int num[4];// x o t d
    for(int i = 0; i < 4; i++) {
        fill(num,num+4,0);
        for(int j = 0; j < 4; j++) {
            counter(num,grid[i][j]);
        }
        if(num[3] > 0) {
            dot = true;
        } else {
            if(num[0] + num[2] == 4) return 0;
            else if(num[1] + num[2] == 4) return 1;
        }
    }
    
    for(int i = 0; i < 4; i++) {
        fill(num,num+4,0);
        for(int j = 0; j < 4; j++) {
            counter(num,grid[j][i]);
        }
        if(num[3] > 0) {
            dot = true;
        } else {
            if(num[0] + num[2] == 4) return 0;
            else if(num[1] + num[2] == 4) return 1;
        }
    }
    fill(num,num+4,0);
    for(int i = 0; i < 4; i++) {
        counter(num,grid[i][i]);
        if(num[3] > 0) {
            dot = true;
        } else {
            if(num[0] + num[2] == 4) return 0;
            else if(num[1] + num[2] == 4) return 1;
        }
    }
    fill(num,num+4,0);
    for(int i = 0; i < 4; i++) {
        counter(num,grid[i][3-i]);
        if(num[3] > 0) {
            dot = true;
        } else {
            if(num[0] + num[2] == 4) return 0;
            else if(num[1] + num[2] == 4) return 1;
        }
    }   
    if(dot) return 3;
    else return 2;
}

int main(int argc, char* argv[]) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    
    int T = 0;
    fin >> T;
    vector<string> grid(4,"");
    for(int tt = 1; tt <= T; tt++) {
        string tmp = "";
        for(int i = 0; i < 4; i++) {
            fin >> tmp;
            grid[i] = tmp;
        }
        int rt = check(grid);
        fout << "Case #" << tt << ": ";
        if(rt == 0) {
            fout << "X won" << endl;
        } else if(rt == 1) {
            fout << "O won" << endl;
        } else if(rt == 2) {
            fout << "Draw" << endl;
        } else if(rt == 3) {
            fout << "Game has not completed" << endl;
        }
    }
    
    
    return 0;
}
