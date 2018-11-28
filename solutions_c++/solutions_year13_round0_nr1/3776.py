#include <iostream>
#include <stdio.h>

using namespace std;


int main() {
int testNum ;
char tab[4][4]={{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
char code[255];
int isDot = 0;
int isSolved = 0;
int row, col, diag1, diag2;
string mesg[5] = {
                    "Draw",
                    "X won",
                    "O won",
                    "Game has not completed",
                    "?"
                 };

//00 - dot
//01 - X
//10 - O
//11 - T

code['O']= 2;
code['X']= 1;
code['T']= 3;
code['.']= 0;


cin >> testNum;


for(int i = 1;i<=testNum;i++){
    isDot = 0;
    isSolved = 0;
    for(int kr=0;kr<4;kr++){
        for(int kc=0;kc<4;kc++){
            cin >> tab[kr][kc];
            if (tab[kr][kc] == '.') isDot = 3;
        }
    }

    diag1 = code[tab[0][0]] & code[tab[1][1]] & code[tab[2][2]] & code[tab[3][3]];
    diag2 = code[tab[0][3]] & code[tab[1][2]] & code[tab[2][1]] & code[tab[3][0]];



   if(diag1 >0 || diag2 >0  ) {
       cout <<"Case #" << i << ": " << mesg[diag1 | diag2] << endl;
        isSolved = 1;
    }
    else {

        for(int kr=0;kr<4;kr++){
            row = code[tab[kr][0]]&code[tab[kr][1]]&code[tab[kr][2]]&code[tab[kr][3]];
            col = code[tab[0][kr]]&code[tab[1][kr]]&code[tab[2][kr]]&code[tab[3][kr]];
            if(row >0 || col > 0) {
                cout <<"Case #" << i << ": " << mesg[row|col] << endl;
                isSolved = 1;
                break;
            }
        }
    }

if (isSolved == 0 ){
    cout <<"Case #" << i << ": "  << mesg[isDot]  << endl;
}

}


return 0;
}
