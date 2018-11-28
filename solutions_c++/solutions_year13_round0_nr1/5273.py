#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;


int win(vector<char> vec, char ch) {
    
    vector<char>::iterator it;
    for (it = vec.begin(); it < vec.end(); it++) {
        if (! ((*it) == ch || (*it) == 'T') ) return 0;
    }
    return 1;
}



int process(char* array[]) {
    
    
    for (int r = 0; r < 4; r++) {
        vector<char> row;
        for (int c = 0; c < 4; c++) {
            row.push_back(array[r][c]);
        }
        if (win(row, 'X')) return -1;
        if (win(row, 'O')) return 1;        
    }
    
    for (int c = 0; c < 4; c++) {
        vector<char> col;
        for (int r = 0; r < 4; r++) {
            col.push_back(array[r][c]);
        }
        if (win(col, 'X')) return -1;
        if (win(col, 'O')) return 1;
    }
    
    
    vector<char> fDiag;
    for (int r = 0; r < 4; r++) {
        for (int c = 0; c < 4; c++) {
            if (r == c) fDiag.push_back(array[r][c]);
        }
    }
    
    if (win(fDiag, 'X')) return -1;
    if (win(fDiag, 'O')) return 1;
    
    vector<char> bDiag;
    for (int r = 0; r < 4; r++) {
        for (int c = 0; c < 4; c++) {
            if (r + c == 3) bDiag.push_back(array[r][c]);
        }
    }
    
    if (win(bDiag, 'X')) return -1;
    if (win(bDiag, 'O')) return 1;
    
    return 0;
    
}


int main() {
    
    ifstream myReadFile;
    myReadFile.open("A-large.in");
    
    ofstream myWriteFile;
    myWriteFile.open("output.out");
    
    int testCases;
    string buffer;
    
    
    if (myReadFile.is_open()) {
        
        getline(myReadFile , buffer);
        testCases = atoi(buffer.c_str());
        
       
        
        for (int i = 0; i<testCases; i++) {
            
            int empty = 0;
            char* array[4];
            for (int it = 0; it < 4; it++)
                array[it] = new char[4];
            
            
            for (int r = 0; r < 4; r++) {
                getline(myReadFile , buffer);
                istringstream stream(buffer);
                for (int c = 0; c < 4; c++) {
                    stream >> array[r][c];
                    if (array[r][c] == '.') empty = 1;
                }
                    
            }
            
            int ret = process(array);
            
            string result;
            
            if (ret == -1) result = "X won";
            else if (ret == 1) result = "O won";
            else if (ret == 0 && empty) result = "Game has not completed";
            else result = "Draw";
            
            
            myWriteFile<<"Case #"<<i+1<<": "<<result<<endl;
            
            getline(myReadFile , buffer);
            
        }
    }
    
    myReadFile.close();
    myWriteFile.close();
    return 0;
}
