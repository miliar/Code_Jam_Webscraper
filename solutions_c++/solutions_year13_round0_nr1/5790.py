#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("A.in");
ofstream fout("A.out");

int T;
char Board[4][4];
string status[4] = {"Draw\n", "Game has not completed\n", "O won\n", "X won\n"};

int main() {
    fin >> T;
    
    for(int it=1; it<=T; it++) 
    {
    
        fout << "Case #" << it << ": ";
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                fin >> Board[i][j];
        bool determined = false;
        
        for(int i=0; i<4; i++) 
        {
            char R = (Board[i][0]!='T')? Board[i][0]: Board[i][1];
            if(R=='.') continue;
            bool winR= true;
            for(int j=1; j<4; j++) 
            {
                if(Board[i][j] !=R && Board[i][j]!='T') {
                    winR= false;
                    break;
                }
            }
            if(winR) 
            {
                determined = true;
                int message = (R == 'O')? 2: 3;
                fout << status[message];
                break;
            }
        }
        
        if(determined) continue;
        for(int j=0; j<4; j++) 
        {
            char C = (Board[0][j]!='T')? Board[0][j]: Board[1][j];
            if(C=='.') continue;
            bool winC= true;
            for(int i=1; i<4; i++) 
            {
                if(Board[i][j] !=C && Board[i][j]!='T') {
                    winC= false;
                    break;
                }
            }
            if(winC) {
                determined = true;
                int message = (C == 'O')? 2: 3;
                fout << status[message];
                break;
            }
        }
        
        if(determined) continue;               
        char D1 = (Board[0][0]!='T')? Board[0][0]: Board[1][1];
        if(D1 != '.') {
            bool winD = true;        
            for(int j=1; j<4; j++) {
                if(Board[j][j] !=D1 && Board[j][j]!='T') {
                    winD= false;
                    break;
                }
            }
            if(winD) {
                determined = true;
                int message = (D1 == 'O')? 2: 3;
                fout << status[message];
            }
        }
        
        if(determined) continue;               
        char D2 = (Board[3][0]!='T')? Board[3][0]: Board[2][1];
        if(D2!='.') {
            bool winD2 = true;
            for(int j=1; j<4; j++) {
                if(Board[3-j][j] !=D2 && Board[3-j][j]!='T') {
                    winD2= false;
                    break;
                }
            }
            if(winD2) {
                determined = true;
                int message = (D2 == 'O')? 2: 3;
                fout << status[message];
            }
        }
        
        if(determined) continue; 
        int message = 0;
        for(int j=0; j<16; j++) {
            if(Board[j/4][j%4] == '.') {
                message = 1;
                break;
            }
        }                       
        fout << status[message];   
    }
}
