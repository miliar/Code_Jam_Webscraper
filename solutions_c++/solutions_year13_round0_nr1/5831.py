/* 
 * File:   main.cpp
 * Author: tbporter
 *
 * Created on April 12, 2013, 7:19 PM
 */

#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

#define BOARD_SIZE 4 //I shouldn't have done this, just made it messier

//Prototypes
char findWin(char board[][BOARD_SIZE]);
bool checkEq(char a, char b);
void setT(char &a,char b);

int main(int argc, char** argv) {

    char board[BOARD_SIZE][BOARD_SIZE], winner;
    int games;
    bool emptySpace;
    string line;
    std::ifstream inFile("A-large.in");
    std::ofstream oFile("out");
    inFile >> line;

    games = atoi(line.c_str());
    for(int curGame = 0; curGame < games; curGame++ ){
        emptySpace = false;
        //Read the board in
        for(int i =0;i<BOARD_SIZE;i++){
            inFile >> line;
            for(int j=0;j<BOARD_SIZE;j++){
                board[i][j]= line[j];
                if(line[j]=='.')
                    emptySpace = true; //lets put this here for fun 
            }
        }
        //check for wins
        winner = findWin(board);
        oFile << "Case #" << curGame+1 << ": ";
        switch(winner){
            case 'O':
            case 'X':
                oFile << winner << " won\n";
                break;
            case '.':
                if(emptySpace)
                    oFile << "Game has not completed\n";
                else
                    oFile << "Draw\n";
                
        }
    }
    return 0;
}


bool checkEq(char a, char b){
    if(a == '.' || b =='.')
        return false;
    if(a != 'T' && b != 'T'){
        return a == b;
    }
    return true;
}

void setT(char &a,char b){
    if(b != 'T')
        a = b;
}



char findWin(char board[][BOARD_SIZE]){
    char prev = '.';
    
    //Check the rows
    for(int i =0; i<BOARD_SIZE;i++){
        prev = board[i][0];
        for(int j =1;j<BOARD_SIZE;j++){
            if(!checkEq(board[i][j],prev)){
                prev = '.';
                break;
            }
            setT(prev,board[i][j]);
        }
        if(prev!='.')
            return prev;
    }
    
    //Check the columns
    for(int j =0; j<BOARD_SIZE;j++){
        prev = board[0][j];
        for(int i =1;i<BOARD_SIZE;i++){
            if(!checkEq(board[i][j],prev)){
                prev = '.';
                break;
            }
            setT(prev,board[i][j]);
        }
        if(prev!='.')
            return prev;
    }
    //check diagonally
    prev = board[0][0];
    for(int i=1;i<BOARD_SIZE;i++){
        if(!checkEq(board[i][i],prev)){
                prev = '.';
                break;
        }
        setT(prev,board[i][i]);
    }
    if(prev!='.')
        return prev;
    //check the other diagonally
    prev = board[0][BOARD_SIZE-1];
    for(int i=1; i<BOARD_SIZE;i++){
        if(!checkEq(board[i][BOARD_SIZE-1-i],prev)){
                prev = '.';
                break;
        }
        setT(prev,board[i][BOARD_SIZE-1-i]);
    }
    return prev;
}

