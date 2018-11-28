#include <iostream>
#include <fstream>
#include <map>
using namespace std;

int main(){
    ifstream inputFile("A-large.in");
    ofstream outputFile("googleCodeJamOUTPUTsmall.txt");
    int numExamples;
    inputFile >> numExamples;
    for(int i = 0; i < numExamples; i++){
        char** grid = new char*[4];
        for(int j = 0; j < 4; j++){
            grid[j] = new char[4];
            inputFile >> grid[j];
            //cout << grid[j][0] << " " << grid[j][1] << " " << grid[j][2] << " " << grid[j][3] << endl;
        }
        //check each row and column
        map<char,int> counts;
        bool xWon = false;
        bool oWon = false;
        int totalEmpty = 0;
        for(int j = 0; j < 4; j++){
            //check row
            counts['X'] = 0;
            counts['O'] = 0;
            counts['T'] = 0;
            counts['.'] = 0;
            for(int k = 0; k < 4; k++) counts[grid[j][k]]++;
            totalEmpty+=counts['.']; //also count up how many empty slots there are.
            if(counts['X']+counts['T'] == 4) {xWon = true; break;}
            if(counts['O']+counts['T'] == 4) {oWon = true; break;}
            
            //check column
            counts['X'] = 0;
            counts['O'] = 0;
            counts['T'] = 0;
            counts['.'] = 0;
            for(int k = 0; k < 4; k++) counts[grid[k][j]]++;
            if(counts['X']+counts['T'] == 4) {xWon = true; break;}
            if(counts['O']+counts['T'] == 4) {oWon = true; break;}
        }
        //check first diagonal
        counts['X'] = 0;
        counts['O'] = 0;
        counts['T'] = 0;
        counts['.'] = 0;
        for(int j = 0; j < 4; j++) counts[grid[j][j]]++;
        if(counts['X']+counts['T'] == 4) {xWon = true;}
        if(counts['O']+counts['T'] == 4) {oWon = true;}
        
        //check second diagonal
        counts['X'] = 0;
        counts['O'] = 0;
        counts['T'] = 0;
        counts['.'] = 0;
        for(int j = 0; j < 4; j++) counts[grid[j][3-j]]++;
        if(counts['X']+counts['T'] == 4) {xWon = true;}
        if(counts['O']+counts['T'] == 4) {oWon = true;}
        if(xWon){
            outputFile << "Case #" << i+1 << ": X won" << endl;
        } else if(oWon){
            outputFile << "Case #" << i+1 << ": O won" << endl;
        } else if(totalEmpty > 0){
            outputFile << "Case #" << i+1 << ": Game has not completed" << endl;
        } else{
            outputFile << "Case #" << i+1 << ": Draw" << endl;
        }
        //get rid of empty space
        string dummy;
        //inputFile >> dummy;
    }
    return 0;
}
