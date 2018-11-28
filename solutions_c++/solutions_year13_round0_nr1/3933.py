#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

bool checkX(vector<vector<string> > grid){
    bool win = false;
    for(int i = 0; i < 4; i++){
        if((grid[i][0] == "X" || grid[i][0] == "T") && (grid[i][1] == "X" || grid[i][1] == "T")
          && (grid[i][2] == "X" || grid[i][2] == "T") && (grid[i][3] == "X" || grid[i][3] == "T")){
            win = true;
        }
        if((grid[0][i] == "X" || grid[0][i] == "T") && (grid[1][i] == "X" || grid[1][i] == "T")
          && (grid[2][i] == "X" || grid[2][i] == "T") && (grid[3][i] == "X" || grid[3][i] == "T")){
            win = true;
        }
    }    
    if((grid[0][0] == "X" || grid[0][0] == "T") && (grid[1][1] == "X" || grid[1][1] == "T")
      && (grid[2][2] == "X" || grid[2][2] == "T") && (grid[3][3] == "X" || grid[3][3] == "T")){
        win = true;
    }
    if((grid[3][0] == "X" || grid[3][0] == "T") && (grid[2][1] == "X" || grid[2][1] == "T")
      && (grid[1][2] == "X" || grid[1][2] == "T") && (grid[0][3] == "X" || grid[0][3] == "T")){
        win = true;
    }
    return win;
}

bool checkO(vector<vector<string> > grid){
    bool win = false;
    for(int i = 0; i < 4; i++){
        if((grid[i][0] == "O" || grid[i][0] == "T") && (grid[i][1] == "O" || grid[i][1] == "T")
          && (grid[i][2] == "O" || grid[i][2] == "T") && (grid[i][3] == "O" || grid[i][3] == "T")){
            win = true;
        }
        if((grid[0][i] == "O" || grid[0][i] == "T") && (grid[1][i] == "O" || grid[1][i] == "T")
          && (grid[2][i] == "O" || grid[2][i] == "T") && (grid[3][i] == "O" || grid[3][i] == "T")){
            win = true;
        }
    }    
    if((grid[0][0] == "O" || grid[0][0] == "T") && (grid[1][1] == "O" || grid[1][1] == "T")
      && (grid[2][2] == "O" || grid[2][2] == "T") && (grid[3][3] == "O" || grid[3][3] == "T")){
        win = true;
    }
    if((grid[3][0] == "O" || grid[3][0] == "T") && (grid[2][1] == "O" || grid[2][1] == "T")
      && (grid[1][2] == "O" || grid[1][2] == "T") && (grid[0][3] == "O" || grid[0][3] == "T")){
        win = true;
    }
    return win;
}

bool checkD(vector<vector<string> > grid){
    bool win = true;
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            if(grid[i][j] == "."){
                win = false;
                break;
            }
        }
        if(!win){
            break;
        }
    }
    return win;
}

int main(){
    ofstream fout ("tictac.out");
    ifstream fin ("tictac.in");
    int N;
    fin >> N;
    
    for(int i = 0; i < N; i++){
        vector<vector<string> > grid;
        for(int j = 0; j < 4; j++){
            string temp;
            fin >> temp;
            vector<string> temp2;
            for(int k = 0; k < 4; k++){
                temp2.push_back(temp.substr(k,1));
            }
            grid.push_back(temp2);
        }
        if(checkX(grid)){
            fout << "Case #" << (i + 1) << ": X won" << endl;
        }else if(checkO(grid)){
            fout << "Case #" << (i + 1) << ": O won" << endl;
        }else if(checkD(grid)){
            fout << "Case #" << (i + 1) << ": Draw" << endl;
        }else{
            fout << "Case #" << (i + 1) << ": Game has not completed" << endl;
        }
    }
}
            
            
    
