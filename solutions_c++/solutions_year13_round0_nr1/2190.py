#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <vector>
using namespace std;


bool won(vector<string> board, char ch) {
     for (int i = 0; i < 4; i++) {
         bool ok = true;
         for (int j = 0; j < 4; j++) {
             if (board[i][j] != ch && board[i][j] != 'T') {ok = false;}                           
         }
         if (ok) return true;
     }
     
     for (int i = 0; i < 4; i++) {
         bool ok = true;
         for (int j = 0; j < 4; j++) {
             if (board[j][i] != ch && board[j][i] != 'T') {ok = false;}                           
         }
         if (ok) return true;
     }
     
     bool diagok = true;
     for (int i = 0; i < 4; i++) {
          if (board[i][i] != ch && board[i][i] != 'T') {diagok = false;}                           
     }
     if (diagok) return true;
     
     diagok = true;
     for (int i = 0; i < 4; i++) {
          if (board[i][3-i] != ch && board[i][3-i] != 'T') {diagok = false;}                           
     }
     
     return diagok;     
}

bool draw(vector<string> board) {
     for (int i = 0; i < 4; i++)
     for (int j = 0; j < 4; j++)
         if (board[i][j] == '.') return false;
     return true;
}


void doit(ofstream& outfile, int casenum, vector<string> board) {
     outfile << "Case #" << casenum << ": ";
     if (won(board, 'X'))
        outfile << "X won" << endl;
     else if (won(board, 'O'))
        outfile << "O won" << endl;
     else if (!draw(board)) 
        outfile << "Game has not completed" << endl;
     else
        outfile << "Draw" << endl;  
                    
}
     

int main() {
    ifstream infile("C:/a.in");
    ofstream outfile("C:/a.out");
    int numCases = 0;
    infile >> numCases;
    for (int i = 0; i < numCases; i++) {
        vector<string> vec;
        for (int j = 0; j < 4; j++) {
            string str;
            infile >> str;
            vec.push_back(str);
        }
        doit(outfile, i+1, vec);
    }    
    outfile.close();
    return 0;
    
}
