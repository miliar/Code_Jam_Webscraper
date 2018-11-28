//
//  main.cpp
//  Tic-tac-toe
//
//  Created by Sava Gerov on 13/04/13.
//  Copyright (c) 2013 Sava Gerov. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

inline int min(int i, int j) {
    return i<j?i:j;
}
inline int max(int i, int j) {
    return i>j?i:j;
}

int main(int argc, const char * argv[])
{

    ifstream input;
    ofstream output;
    int nCases;
    char boardO[4][4];
    char boardX[4][4];
    bool X,O,INCOMPLETE;
    X=O=INCOMPLETE=false;
    
    input.open(argv[1]);
    output.open(argv[2]);
    input >> nCases;
    
    for(int i=0;i<nCases;i++) {
        output << "Case #" << i+1 << ": ";
        for (int j=0; j<4; j++) {
            input >> boardX[j][0] >> boardX[j][1] >> boardX[j][2] >> boardX[j][3];
            boardO[j][0]=boardX[j][0];
            boardO[j][1]=boardX[j][1];
            boardO[j][2]=boardX[j][2];
            boardO[j][3]=boardX[j][3];
            if (boardO[j][0]=='T') {
                boardO[j][0]='O';
                boardX[j][0]='X';
            }
            if (boardO[j][1]=='T') {
                boardO[j][1]='O';
                boardX[j][1]='X';
            }
            if (boardO[j][2]=='T') {
                boardO[j][2]='O';
                boardX[j][2]='X';
            }
            if (boardO[j][3]=='T') {
                boardO[j][3]='O';
                boardX[j][3]='X';
            }
        }
        int succesiveRowsX,succesiveColumnsX,succesiveDiagX,succesiveDiagX2;
        int succesiveRowsO,succesiveColumnsO,succesiveDiagO,succesiveDiagO2;
       
        succesiveDiagX=succesiveDiagX2=0;
        succesiveDiagO=succesiveDiagO2=0;

            
        for (int j=0; j<4; j++) {
            succesiveRowsX=0;
            succesiveColumnsX=0;
            succesiveRowsO=0;
            succesiveColumnsO=0;
            
            for(int k=0;k<4;k++) {
                if (boardX[j][k]=='.') {
                    INCOMPLETE=true;
                }
                if (boardX[j][k]=='X') //check row X
                    succesiveColumnsX++; 
                if (boardO[j][k]=='O') //check row O
                    succesiveColumnsO++;

                if (boardX[k][j]=='X') //check column X
                    succesiveRowsX++; 
                if (boardO[k][j]=='O') //check column O
                    succesiveRowsO++; 
                
                
            }
            
            if (boardX[j][j]=='X') //check first diagonal X
                succesiveDiagX++;
            if (boardO[j][j]=='O') //check first diagonal O
                succesiveDiagO++;
            
            if (boardX[j][3-j]=='X') //check second diagonal X
                succesiveDiagX2++;
            if (boardO[j][3-j]=='O') //check second diagonal O
                succesiveDiagO2++;
            
            
            if (succesiveColumnsX==4 || succesiveRowsX==4) {
                X=true;
            } else if (succesiveColumnsO==4 || succesiveRowsO==4)
                O=true;
        }
            if(succesiveDiagX==4 || succesiveDiagX2==4) X=true;
            else if (succesiveDiagO==4 || succesiveDiagO2==4) O=true;
        
            if (X)
                output << "X won" << endl;
            else if (O)
                output << "O won" << endl;
            else if (INCOMPLETE)
                output << "Game has not completed" << endl;
            else
                output << "Draw" << endl;
            
            
            X=O=INCOMPLETE=false;
    }

    return 0;
}