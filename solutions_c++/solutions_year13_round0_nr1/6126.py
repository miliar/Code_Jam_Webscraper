#include <iostream>
#include <vector>
#include <string>

using namespace std;

#define XWin 0
#define OWin 1
#define Draw 2
#define Inco 3

char gb[4][4];

int checkWinner() {
   
    int noX = 0;
    int noO = 0;

    // rows
    for(int i = 0; i < 4; i++) {
        noX = 0;
        noO = 0;
        for(int j = 0; j < 4; j++) {
            if(gb[i][j] == 'T') {
               noX++;
               noO++;
            }
            if(gb[i][j] == 'X')
	       noX++;
            else if(gb[i][j] == 'O')
               noO++;
        }
        if(noX >= 4)
            return XWin;
        else if(noO >= 4)
            return OWin;
    }

    // column
    for(int j = 0; j < 4; j++) {
        noX = 0;
        noO = 0;
        for(int i = 0; i < 4; i++) {
            if(gb[i][j] == 'T') {
               noX++;
               noO++;
            }
            if(gb[i][j] == 'X')
               noX++;
            else if(gb[i][j] == 'O')
               noO++;
        }
        if(noX >= 4)
            return XWin;
        else if(noO >= 4)
            return OWin;
    }

    // top left diagonal
    noX = 0;
    noO = 0;
    for(int i = 0; i < 4; i++) {
        if(gb[i][i] == 'T') {
            noX++;
            noO++;
        } 
        else if(gb[i][i] == 'X')
            noX++;
        else if(gb[i][i] == 'O')
            noO++;
    } 
    if(noX >= 4)
        return XWin;
    else if(noO >= 4)
        return OWin;
       
    // bottom left diagonal
    noX = 0;
    noO = 0;
    for(int i = 0; i < 4; i++) {
        if(gb[i][3 - i] == 'T') {
            noX++;
            noO++;
        }
        else if(gb[i][3 - i] == 'X')
            noX++;
        else if(gb[i][3 - i] == 'O')
            noO++;
    }
    if(noX >= 4)
        return XWin;
    else if(noO >= 4)
        return OWin;

    // if game board filled
    for(int i = 0; i < 4; i++) 
        for(int j = 0; j < 4; j++) 
            if(gb[i][j] == '.')
               return Inco; 

    return Draw; 
}

int main() {
    string stmp;
    int noTests;
    cin >> noTests;
    getline(cin, stmp); 
    for(int i = 0; i < noTests; i++) {
	for(int j = 0; j < 4; j++) {
	    for(int k = 0; k < 4; k++) {
		cin >> gb[j][k];
            }
            getline(cin, stmp);
        }
        getline(cin, stmp);
        // output
        int state = checkWinner();
        string ss;
        switch(state) {
	    case(XWin):
                ss = "X won";
                break;
            case(OWin):
                ss = "O won";
                break;
            case(Draw):
                ss = "Draw";
                break;
            default:
                ss = "Game has not completed";
        }
        cout << "Case #" << i + 1 << ": " << ss << endl;
    }
}

