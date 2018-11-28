/*
    ID: darkangl3
    LANG: C++
    PROB:
*/
#include<iostream>
#include<fstream>
#include<string>
#include<conio.h>

using namespace std;

class TicTac {
    int arr[4][4];
    
    public:
        TicTac(int a[4][4]) {
            for(int i = 0; i < 4; i++)
                for(int j = 0; j < 4; j++)
                    this->arr[i][j] = a[i][j];
        }
        
        //return 0: O win | 1: X win
        int findWin() {
            int ret = -1;
            
            int ch = 0;
            //find row || col || cross
            ret = findRow(ch) || findCol(ch) || findCross(ch);
            if (ret) {
                return ch;
            }
            
            ch = 1;
            ret = findRow(ch) || findCol(ch) || findCross(ch);
            if (ret) {
                return ch;
            }
            
            return -1;
        }
        
        int findRow(int ch) {
            //init
            int numCh = 0, numT = 0;
            for(int i = 0; i < 4; i++) {
                numCh = 0; numT = 0;
                for(int j = 0; j < 4; j++) {
                    if (arr[i][j] == ch) numCh++;
                    if (arr[i][j] == 2) numT++;
                }
                
                if (numCh == 4 || (numCh == 3 && numT == 1)) {
                    return 1;
                }
            }
            
            return 0;
        }
        
        int findCol(int ch) {
            //init
            int numCh = 0, numT = 0;
            
            for(int i = 0; i < 4; i++) {
                numCh = 0; numT = 0;
                for(int j = 0; j < 4; j++) {
                    if (arr[j][i] == ch) numCh++;
                    if (arr[j][i] == 2) numT++;
                }
                
                if (numCh == 4 || (numCh == 3 && numT == 1)) {
                    return 1;
                }
            }
            
            return 0;
        }
        
        int findCross(int ch) {
            //init
            int numCh = 0, numT = 0;
            
            //main cross
            for(int i = 0; i < 4; i++) {
                if (arr[i][i] == ch) numCh++;
                if (arr[i][i] == 2) numT++;
            }

            if (numCh == 4 || (numCh == 3 && numT == 1)) {
                return 1;
            }
            
            numCh = 0, numT = 0;
            //sub cross
            for(int i = 0; i < 4; i++) {
                if (arr[i][4-i-1] == ch) numCh++;
                if (arr[i][4-i-1] == 2) numT++;
            }
            if (numCh == 4 || (numCh == 3 && numT == 1)) {
                return 1;
            }
            
            return 0;
        }
};

char ch;
int arr[4][4];
string res;
int Test;

int main()
{
    ofstream fout ("test.out");
    ifstream fin ("test.in");

    fin >> Test;
    for(int t = 1; t <= Test; t++) {
        fout << "Case #" << t << ": ";
        int numDot = 0;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                fin >> ch;
                if (ch == 'O') arr[i][j] = 0;
                if (ch == 'X') arr[i][j] = 1;
                if (ch == 'T') arr[i][j] = 2;
                if (ch == '.') arr[i][j] = 3;
                if (arr[i][j] == 3) numDot++;
            }
        }
        
        TicTac a(arr);
        int win = a.findWin();
        
        if (win == 0) {
            res = "O won";
        } else if (win == 1) {
            res = "X won";
        } else {
            if (numDot == 0) {
                res = "Draw";
            } else {
                res = "Game has not completed";
            }
        }
        
        fout << res << endl;
    }

    return 0;
}
