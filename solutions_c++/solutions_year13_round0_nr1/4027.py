//
//  main.cpp
//  TT
//
//  Created by jiusi on 4/13/13.
//  Copyright (c) 2013 jiusi. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<char> res_set;

string check(char matrix[4][4]) {
    int tdc = 0;
    int gpx = 0;
    int gpo = 0;
    for(int i=0; i<4; i++) {
        
        int xc = 0;
        int oc = 0;
        
        for(int j=0; j<4; j++) {
            
            if(matrix[i][j] == 'X') {
                xc++;
            } else if(matrix[i][j] == 'O') {
                oc++;
            } else if(matrix[i][j] == '.') {
                tdc++;
            } else if(matrix[i][j] == 'T') {
                xc++;
                oc++;
            }
        }
        if(xc == 4) {
            return "X won";
        } else if (oc == 4) {
            return "O won";
        } else {
            if(xc == 3)
                gpx++;
            if(oc == 3)
                gpo++;
        }
    }
    
    for(int i=0; i<4; i++) {
        
        int xc = 0;
        int oc = 0;
        
        for(int j=0; j<4; j++) {
            
            if(matrix[j][i] == 'X') {
                xc++;
            } else if(matrix[j][i] == 'O') {
                oc++;
            } else if(matrix[j][i] == 'T') {
                xc++;
                oc++;
            }
        }
        if(xc == 4) {
            return "X won";
        } else if (oc == 4) {
            return "O won";
        } else {
            if (xc == 3) {
                gpx++;
            } else {
                gpo++;
            }
        }
    }
    
    
    int xc = 0;
    int oc = 0;
    for(int i=0; i<4; i++) {
        if(matrix[i][i] == 'T') {
            xc++;
            oc++;
        } else if(matrix[i][i] == 'X') {
            xc++;
        } else if(matrix[i][i] == 'O') {
            oc++;
        }
    }
    if(xc == 4) {
        return "X won";
    } else if(oc == 4) {
        return "O won";
    } else {
        if(xc == 3){
            gpx ++;
        } else if(oc == 3) {
            gpo ++;
        }
    }
    
    xc = 0;
    oc = 0;
    for(int i=0; i<4; i++) {
        if(matrix[3-i][i] == 'T') {
            xc++;
            oc++;
        } else if(matrix[3-i][i] == 'X') {
            xc++;
        } else if(matrix[3-i][i] == 'O') {
            oc++;
        }
    }
    if(xc == 4) {
        return "X won";
    } else if(oc == 4) {
        return "O won";
    }  else {
        if(xc == 3){
            gpx ++;
        } else if(oc == 3) {
            gpo ++;
        }
    }

    
    if(tdc == 0) {
        return "Draw";
    }

//    if(gpx > gpo) {
//        return "X won";
//    } else if (gpo > gpx) {
//        return "O won";
//    }
//    
    return "continue";
}


string cal(char matrix[4][4], char s) {
    
    string result = check(matrix);
    if (result != "continue") {
//        cout << "result:" << result << endl;
        return result;
    }
    
    vector<pair<int, int>> dots;
    for(int i = 0; i < 4; i++) {
        for( int j = 0; j<4 ;j ++) {
            if(matrix[i][j] == '.') {
                dots.push_back(make_pair(i, j));
            }
        }
    }
    
    string last = "";
    for(int count =0; count < 2; count++){
        int index = rand() % dots.size();
        int i = dots[index].first;
        int j = dots[index].second;

        string c1;
        if(s == 'X') {
            char newmatrix[4][4];
            for(int x = 0; x < 4; x++) {
                for(int y = 0; y < 4; y++) {
                    newmatrix[x][y] = matrix[x][y];
                }
            }
            newmatrix[i][j] = 'O';
            c1 = cal(newmatrix, 'O');
        } else if (s == 'O') {
            char newmatrix[4][4];
            for(int x = 0; x < 4; x++) {
                for(int y = 0; y < 4; y++) {
                    newmatrix[x][y] = matrix[x][y];
                }
            }
            newmatrix[i][j] = 'X';
            c1 = cal(newmatrix, 'X');
        }
        
        if(last == "") {
            last = c1;
        }
        
        if(c1 != last) {
            return "continue";
        }
    }
    
    return last;
}


int main(int argc, const char * argv[])
{
    ifstream cin("/Users/jiusi/Downloads/A-small-attempt0.in");
//    ifstream cin("/Users/jiusi/test.in");
    ofstream cout("/Users/jiusi/workspace-cv/TT/TT/res.out");
    
    int n;
    cin >> n;
    int count = 0;
    for(int c = 0; c < n; c++) {
        
        char matrix[4][4];
        for(int i= 0; i<4;i++) {
            string line;
            cin >> line;
            for(int j=0; j<4; j++) {
                matrix[i][j] = line[j];
            }
        }

//        string re = check(matrix);
        string re = cal(matrix, 'X');
        string re1 =cal(matrix, 'O');
        
        if(re == "continue" && re == re1) {
            cout << "Case #" << ++count << ": Game has not completed" << endl;            
        } else if (re != re1) {
            cout << "Case #" << ++count << ": Game has not completed" << endl;
        } else {
            cout << "Case #" << ++count << ": " << re << endl;
        }
        
        
    }

    return 0;
}

