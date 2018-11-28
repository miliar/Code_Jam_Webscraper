#include <iostream>

using namespace std;

#define X_WON cout << "X won"
#define O_WON cout << "O won"
#define DRAW  cout << "Draw"
#define GHNC  cout << "Game has not completed"

int main() {

    char board[5][5];
    int t;
    char newline;
    bool found_dot = 0;
    int i, j, k;

    //read no test cases
    cin >> t;

    //init all to null
    for(i=0; i<5; i++) {
        for(j=0; j<5; j++) {
            board[i][j]='\0';
        }
    }

    for(i=1; i<=t; i++) {
        found_dot = false;
        
        //read testcase
        for(j=0; j<4; j++) {
            for(k=0; k<4; k++) {
                cin >> board[j][k];

                if(board[j][k]=='.') {
                    found_dot=true;
                }

            }
        }

        //print input
        //cout << endl;
        //for(j=0; j<4; j++) {
        //    for(k=0; k<4; k++) {
        //        cout << board[j][k];
        //    }

        //    cout << endl;
        //}
        //cout << endl;

        //print case number
        cout << "Case #" << i << ": ";

        //see if any row matches with X
        for(j=0; j<4; j++) {
            for(k=0; k<4; k++) {
                if(board[j][k] != 'X' && board[j][k] !='T') { break; }
            }
            
            if(k==4) { X_WON; goto end;}
        }

        //see if any row matches with X
        for(j=0; j<4; j++) {
            for(k=0; k<4; k++) {
                if(board[j][k] != 'O' && board[j][k] !='T') { break; }
            }
            
            if(k==4) { O_WON; goto end;}
        }

        //see if any col matches with X
        for(j=0; j<4; j++) {
            for(k=0; k<4; k++) {
                if(board[k][j] != 'X' && board[k][j] !='T') { break; }
            }
            
            if(k==4) { X_WON; goto end;}
        }

        //see if any col matches with O
        for(j=0; j<4; j++) {
            for(k=0; k<4; k++) {
                if(board[k][j] != 'O' && board[k][j] !='T') { break; }
            }
            
            if(k==4) { O_WON; goto end;}
        }

        //see if any diag matches with X
        for(j=0; j<4; j++) {
            if(board[j][j] != 'X' && board[j][j] !='T') { break; }
        }

        if(j==4) { X_WON; goto end;}

        //see if diag matches with O
        for(j=0; j<4; j++) {
            if(board[j][j] != 'O' && board[j][j] !='T') { break; }
        }

        if(j==4) { O_WON; goto end;}

        //see if cross diag matches with X
        for(j=0; j<4; j++) {
            if(board[j][3-j] != 'X' && board[j][3-j] !='T') { break; }
        }

        if(j==4) { X_WON; goto end;}

        //see if cross diag matches with O
        for(j=0; j<4; j++) {
            if(board[j][3-j] != 'O' && board[j][3-j] !='T') { break; }
        }

        if(j==4) { O_WON; goto end;}

        if(found_dot==true) { GHNC; }
        else          { DRAW; }

end:    cout << endl;

    }



    return 0;
}
