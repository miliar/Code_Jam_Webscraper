/* 
 * File:   main.cpp
 * Author: mfatihuslu
 *
 * Created on April 13, 2013, 6:29 AM
 */
#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cmath>
using namespace std;
#define AND &&
#define OR ||

    fstream inputFile, outputFile, logFile;
    int caseNumber;
    char** board;

void printBoard() {
    
    for(int j=0;j<4;j++){
            
        for(int k=0;k<4;k++){
                
            logFile << board[j][k];
        }
        logFile << endl;
    }
    logFile << endl;
}

int valueBoard(){
    
    for(int i=0;i<4;i++){
        
        if((board[i][0]=='X' or board[i][0]=='T') and
           (board[i][1]=='X' or board[i][1]=='T') and 
           (board[i][2]=='X' or board[i][2]=='T') and
           (board[i][3]=='X' or board[i][3]=='T')){
            
            return 1;
        }
        if((board[i][0]=='O' or board[i][0]=='T') and
           (board[i][1]=='O' or board[i][1]=='T') and 
           (board[i][2]=='O' or board[i][2]=='T') and
           (board[i][3]=='O' or board[i][3]=='T')){
            
            return 2;
        }
        if((board[0][i]=='X' or board[0][i]=='T') and
           (board[1][i]=='X' or board[1][i]=='T') and 
           (board[2][i]=='X' or board[2][i]=='T') and
           (board[3][i]=='X' or board[3][i]=='T')){
            
            return 1;
        }
        if((board[0][i]=='O' or board[0][i]=='T') and
           (board[1][i]=='O' or board[1][i]=='T') and 
           (board[2][i]=='O' or board[2][i]=='T') and
           (board[3][i]=='O' or board[3][i]=='T')){
            
            return 2;
        }
    }
    
    if((board[0][0]=='X' or board[0][0]=='T') and
       (board[1][1]=='X' or board[1][1]=='T') and 
       (board[2][2]=='X' or board[2][2]=='T') and
       (board[3][3]=='X' or board[3][3]=='T')){
            
            return 1;
    }
    if((board[0][0]=='O' or board[0][0]=='T') and
       (board[1][1]=='O' or board[1][1]=='T') and 
       (board[2][2]=='O' or board[2][2]=='T') and
       (board[3][3]=='O' or board[3][3]=='T')){
            
            return 2;
    }
    if((board[0][3]=='X' or board[0][3]=='T') and
       (board[1][2]=='X' or board[1][2]=='T') and 
       (board[2][1]=='X' or board[2][1]=='T') and
       (board[3][0]=='X' or board[3][0]=='T')){
            
            return 1;
    }
    if((board[0][3]=='O' or board[0][3]=='T') and
       (board[1][2]=='O' or board[1][2]=='T') and 
       (board[2][1]=='O' or board[2][1]=='T') and
       (board[3][0]=='O' or board[3][0]=='T')){
            
            return 2;
    }
    for(int i=0;i<4;i++){
        
        for(int j=0;j<4;j++)
            
            if(board[i][j]=='.')
                return 3;
    }
    return 0;
}

/*
 * 
 */
int main(int argc, char** argv) {
    
    //for(int i=1;i<20;i++)
    //    cout << T(2147483627+i,2147483627+i)<<endl;
    
    inputFile.open("input",ios::in);
    outputFile.open("output",ios::out);
    logFile.open("log",ios::out);
    
    board = new char* [4];
        
    for(int j=0;j<4;j++){

        board[j] = new char[4];
    }
    
    inputFile >> caseNumber;
    
    for(int i=1; i<=caseNumber; i++) {
        
        
        for(int j=0;j<4;j++){
            
            for(int k=0;k<4;k++){
                
                inputFile >> board[j][k];
            }
        }
        
        printBoard();
        
        outputFile << "Case #"<<i<<": ";
        
        int result = valueBoard();
        
        switch(result){
            
            case 0: outputFile << "Draw"<<endl; break;
            case 1: outputFile << "X won"<<endl; break;
            case 2: outputFile << "O won"<<endl; break;
            case 3: outputFile << "Game has not completed"<<endl; break;
        }
    }
    //*/
    return 0;
}

