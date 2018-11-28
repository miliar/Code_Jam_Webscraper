/* 
 * File:   main.cpp
 * Author: tuannguyen
 *
 * Created on April 13, 2013, 3:52 PM
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> GetAllLines(string match[]){
    vector<string> res = vector<string>();
    for(int i = 0; i < 4; i++)
        res.push_back( match[i]);
    for(int i = 0; i < 4; i++){
        string str = "";
        for(int j = 0; j < 4; j++)
            str+=match[j][i];
        res.push_back(str);
    }
    string firstDiagonal = "";
    string secondDiagonal = "";
    for(int i = 0; i < 4; i++){
        firstDiagonal += match[i][i];
        secondDiagonal += match[i][3-i];
    }
    res.push_back(firstDiagonal);
    res.push_back(secondDiagonal);
    return res;
    
}

/*
 * 
 */
int main(int argc, char** argv) {
    int test;
    cin >> test;
    cin.ignore(100, '\n');
    for(int t = 0; t < test; t++){
        string match[4];
        for(int i = 0; i < 4; i++)
            getline(cin, match[i]);
        cin.ignore(100, '\n');
        vector<string> lines = GetAllLines(match);
        bool isBreak = false;
        bool isNotComplete = false;
        for(int i = 0; i < 10; i++){
            int XCount = 0;
            int OCount = 0;
            int TCount = 0;
            for(int j = 0; j < 4; j++){
                if(lines[i][j] == 'O')
                    OCount++;
                if(lines[i][j] == 'X')
                    XCount++;
                if(lines[i][j] == 'T')
                    TCount++;
            }
            if(OCount == 4 || (OCount == 3 && TCount == 1)){
                cout << "Case #" << t+1 << ": " << "O won\n";
                isBreak = true;
                break;
            }
            if(XCount == 4 || (XCount == 3 && TCount == 1)){
                cout << "Case #" << t+1 << ": " << "X won\n";
                isBreak = true;
                break;
            }
            if(OCount + XCount + TCount < 4)
                isNotComplete = true;
        }
        if(!isBreak){
            if(isNotComplete)
                cout << "Case #" << t+1 << ": Game has not completed\n";
            else
                cout << "Case #" << t+1 << ": Draw\n";
        }
    }
    return 0;
}

