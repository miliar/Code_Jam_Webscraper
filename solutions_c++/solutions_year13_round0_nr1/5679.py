/*
Problem A
Brendan Falk
*/

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;


bool squareIsFull;
char square[4][4];

bool caseTester (char c, int x, int y) {
    int checkDigit = 0;
    
    //This will check if a square in the first column is = to T
    for(int columns = 0 ; columns < 4 ; columns++) {
        if(square[x][columns] == 'T' || square[x][columns] == c) checkDigit++;
    }
    
    if(checkDigit == 4) return true;
    
    //Must reassign checkdigit for each new column
    checkDigit = 0;
    for(int row = 0 ; row < 4 ; row++){
        if(square[row][y] == 'T' || square[row][y] == c) checkDigit++;
    }
    
    if(checkDigit == 4) return true;
    
    checkDigit = 0;
    
    if(x+y == 3) {
        for(int looper = 0 ; looper < 4 ; looper++){
            for(int counter = 0 ; counter < 4 ; counter++) {
                if(looper+counter == 3){
                    if(square[looper][counter] == 'T' || square[looper][counter] == c) {
                      checkDigit++;  
                    }
                }
            }
        }
        if(checkDigit == 4) return true;
        checkDigit = 0;
    }
    
    if(x == y) {
        for(int looper = 0 ; looper < 4 ; looper++) {
            for(int counter = 0 ; counter < 4 ; counter++) {
                if(!(looper-counter)) {
                    if(square[looper][counter] == 'T' || square[looper][counter] == c) checkDigit++;
                }
            }
        }
        if(checkDigit == 4) return true;
        checkDigit = 0;
    }
    return false;
}



int main() {
    
    int testCases, count = 1;
    scanf("%d", &testCases);
    while(testCases--) {
        
        memset(square, 0, sizeof(square));
        
        for(int i = 0 ; i < 4 ; i++){
            scanf("%s", square[i]);
            
        }
        
        //It is a draw if the square is full and no winner has been determined
        string winner = "Draw";
        squareIsFull = true;
        
        for(int looper = 0 ; looper < 4 ; looper++) {
            for(int counter = 0 ; counter < 4 ; counter++) {
                if(square[looper][counter] == '.') squareIsFull = false;
                else if(square[looper][counter] == 'X' || square[looper][counter] == 'O') {
                    
                    bool iswin = caseTester(square[looper][counter], looper, counter);
                    
                    if(iswin) {
                        
                        winner = "";
                        winner += square[looper][counter];
                        break;
                        
                    }
                }
            }
        }
        
        printf("Case #%d: ", count++);
        
        //Will get the correct winner and print it out
        if(winner == "X" || winner == "O") printf("%s won\n", winner.c_str());
        else if(winner == "Draw") {
            
            //If it is a full square, print draw, otherwise, the game has not finished as there is no winner
            if(squareIsFull) puts("Draw");
            else puts("Game has not completed");
        }
    }
    return 0;
}