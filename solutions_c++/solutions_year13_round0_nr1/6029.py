//
//  main.cpp
//  GCJ2013QAA
//


#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

void win(string str, bool &x, bool &o) {
    int xcount = 0, ocount = 0, tcount = 0;
    for (int i = 0; i < str.size(); i++) {
        switch (str[i]) {
            case 'X':
                xcount++;
                break;
            case 'O':
                ocount++;
                break;
            case 'T':
                tcount++;
                break;
            default:
                break;
        }
    }
    
    if (xcount == 4 || (xcount == 3 && tcount == 1)) {
        x = true;
    }
    
    if (ocount == 4 || (ocount == 3 && tcount == 1)) {
        o = true;
    }
    
}

int main(int argc, const char * argv[])
{
    ifstream ifs( "large.in" );
	int T = 0;
    
	ifs >> T;
    
    for (int testcase = 0; testcase < T; testcase++) {
        vector<string> board;
        for (int i = 0; i < 4; i++) {
            string row;
            ifs >> row;
            board.push_back(row);
        }
        
        bool x = false ,o = false;
        
        string diag1, diag2;
        int remspace = 0;
        for (int i = 0; i < 4; i++) {
            win(board[i], x, o);
            string col;
            for (int j = 0; j<4; j++) {
                col += board[j][i];
                if (board[i][j] == '.') {
                    remspace++;
                }
            }
            win(col, x, o);
            
            diag1 += board[i][i];
            diag2 += board[i][3-i];
        }
        win(diag1, x, o);
        win(diag2, x, o);
        
        string result;
        if (x && o) {
            result = "Draw";
        }else if (x) {
            result = "X won";
        }else if (o) {
            result = "O won";
        }else if (remspace) {
            result = "Game has not completed";
        }else {
            result = "Draw";
        }
        
        cout << "Case #" << testcase+1 << ": " << result << endl;
     }

	return 0;
}

