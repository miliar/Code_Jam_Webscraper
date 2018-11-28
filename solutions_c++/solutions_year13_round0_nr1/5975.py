#include <iostream>
#include <string>
#include <string.h>
#include <sstream>
#include <vector>
#include <stdlib.h>
#include <fstream>

using namespace std;

/* Function Prototypes */
int charMapInt(char c);
void initBoardData();
void readBoardData();

bool findWinner(int num);
bool emptyFields();

string processTestCase();



/* Global Variables */
int T;

int board[4][4];


int main() {
    string str;

    cin >> T;
    getline(cin,str);
    if(T<1 && T>1000) return 1;
    
    for (int t=0;t<T;t++ ) {
        cout << "Case #" << t+1 << ": " << processTestCase() << endl;
        
	    getline(cin,str);
        str.erase();
    }

    return 0;
}

string processTestCase() {
    initBoardData();
    readBoardData();

    if(findWinner(1)){
        return "X won";
    }
    if(findWinner(2)){
        return "O won";
    }
    
    if(emptyFields()){
        return "Game has not completed";
    }

    return "Draw";
}


bool findWinner(int num) {
    int joker = 3;
    int counter = 0;
        
    // find in left diagonal
    counter = 0;
    for (int i=0;i<4;i++ ) {
        for (int j=0;j<4;j++ ) {
            if(i==j & (board[i][j] == num || board[i][j] == joker) ){
                counter++;
            }
        }
    }
    if(counter == 4){
        return true;
    }

    // find in right diagonal
    counter = 0;
    for (int i=3;i>=0;i-- ) {
        for (int j=0;j<4;j++ ) {
            if( (i+j)==3 & (board[i][j] == num || board[i][j] == joker) ){
                counter++;
            }
        }
    }
    if(counter == 4){
        return true;
    }


    // find in rows
    for (int i=0;i<4;i++ ) {
        counter = 0;
        for (int j=0;j<4;j++ ) {
            if(board[i][j] == num || board[i][j] == joker ){
                counter++;
            }
        }
        if(counter == 4){
            return true;
        }
    }
    
    // find in columns
    for (int j=0;j<4;j++ ) {
        counter = 0;
        for (int i=0;i<4;i++ ) {
            if(board[i][j] == num || board[i][j] == joker ){
                counter++;
            }
        }
        if(counter == 4){
            return true;
        }
    }
    
    return false;
}



bool emptyFields() {
    for (int i=0;i<4;i++ ) {
        for (int j=0;j<4;j++ ) {
            if(board[i][j] == 0){
                return true;
            }
        }
    }
    return false;
}



int charMapInt(char c) {
    switch (c) {
        case 'X': return 1;
        case 'O': return 2;
        case 'T': return 3;
        case '.': return 0;
        default : return -1;
    }
    return -1;
}


void initBoardData() {
    for (int i=0;i<4;i++ ) {
        for (int j=0;j<4;j++ ) {
            board[i][j]=0;
        }
    }
}


void readBoardData() {
    char temp;
    
    for (int i=0;i<4;i++ ) {
        for (int j=0;j<4;j++ ) {
            cin >> temp;
            board[i][j] = charMapInt(temp);
        }
    }
}


