#include "string"
#include "iostream"
using namespace std;

int main() {
    int T;
    cin >> T;
    char c;
    int result; // 0: O won, 1: X won, 2: draw, 3: not complete
    int board[4][4];
    string s;
    bool full;
    int r1, r2, r3, r4, c1, c2, c3, c4, d1, d2;

    for (int k=0; k<T; k++) {
        result = 0;
        full = true;
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                cin >> c;
                if (result != 3) {
                    if (c == '.') {
                        full = false;
                        board[i][j] = 0;
                    }
                    else if (c == 'O') {
                        board[i][j] = 2;
                    }
                    else if (c == 'X') {
                        board[i][j] = 1;
                    }
                    else if (c == 'T') {
                        board[i][j] = -1;
                    }
                }
                
            }
        }
        r1 = board[0][0] * board[0][1] * board[0][2] * board[0][3]; 
        r2 = board[1][0] * board[1][1] * board[1][2] * board[1][3]; 
        r3 = board[2][0] * board[2][1] * board[2][2] * board[2][3]; 
        r4 = board[3][0] * board[3][1] * board[3][2] * board[3][3]; 
    
        c1 = board[0][0] * board[1][0] * board[2][0] * board[3][0]; 
        c2 = board[0][1] * board[1][1] * board[2][1] * board[3][1]; 
        c3 = board[0][2] * board[1][2] * board[2][2] * board[3][2]; 
        c4 = board[0][3] * board[1][3] * board[2][3] * board[3][3]; 
        
        d1 = board[0][0] * board[1][1] * board[2][2] * board[3][3]; 
        d2 = board[0][3] * board[1][2] * board[2][1] * board[3][0]; 
    
        if (r1*r1==1 ||r2*r2==1 ||r3*r3==1 || r4*r4==1 || c1*c1==1 || c2*c2==1 || c3*c3==1 || c4*c4==1 || d1*d1==1 || d2*d2==1) {
            result = 0;
        }
        else if ((r1-4)*(r1-4)==144 ||(r2-4)*(r2-4)==144 ||(r3-4)*(r3-4)==144 || (r4-4)*(r4-4)==144 || (c1-4)*(c1-4)==144 || (c2-4)*(c2-4)==144 || (c3-4)*(c3-4)==144 || (c4-4)*(c4-4)==144 || (d1-4)*(d1-4)==144 || (d2-4)*(d2-4)==144) {
            result = 1;
        }
        else if (full){
            result = 2;
        }
        else {
            result = 3;
        }


        /*
         Case #1: X won
         Case #2: Draw
         Case #3: Game has not completed
         */
        switch (result) {
            case 0: s = "X won"; break;
            case 1: s = "O won"; break;
            case 2: s = "Draw"; break;
            case 3: s = "Game has not completed"; break;
        }

        cout << "Case #" << k+1 << ": " << s << endl;

    
    }
    
    return 0;
}
