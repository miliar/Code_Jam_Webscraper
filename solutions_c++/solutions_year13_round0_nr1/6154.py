#include <iostream>
#include <string>

#define forn(i,x,y) for(int i=x;i<y;i++)

using namespace std;

char board[4][4];

string answer(void) {
    int qty_o = 0, qty_x = 0, points = 0;
    forn(i,0,4) {
        qty_o += (board[i][i] == 'O' || board[i][i] == 'T');
        qty_x += (board[i][i] == 'X' || board[i][i] == 'T');
        points += (board[i][i] == '.');
    }
    if(qty_o == 4) return "O won"; if(qty_x == 4) return "X won";
    qty_o = qty_x = 0;
    forn(i,0,4) {
        qty_o += (board[i][3-i] == 'O' || board[i][3-i] == 'T');
        qty_x += (board[i][3-i] == 'X' || board[i][3-i] == 'T');
        points += (board[i][3-i] == '.');
    }
    if(qty_o == 4) return "O won"; if(qty_x == 4) return "X won";
    qty_o = qty_x = 0;
    forn(i,0,4) {
        forn(j,0,4){
            qty_o += (board[i][j] == 'O' || board[i][j] == 'T');
            qty_x += (board[i][j] == 'X' || board[i][j] == 'T');
            points += (board[i][j] == '.');
        }
        if(qty_o == 4) return "O won"; if(qty_x == 4) return "X won";
        qty_o = qty_x = 0;
        forn(j,0,4){
            qty_o += (board[j][i] == 'O' || board[j][i] == 'T');
            qty_x += (board[j][i] == 'X' || board[j][i] == 'T');
            points += (board[j][i] == '.');
        }
        if(qty_o == 4) return "O won"; if(qty_x == 4) return "X won";
        qty_o = qty_x = 0;
    }
    if(points > 0) return "Game has not completed";
    else return "Draw";
}

int main(void) {
    int test; cin >> test;
    forn(t,1,test+1) {
        forn(i,0,4) forn(j,0,4)
            cin >> board[i][j];
        cout << "Case #" << t << ": " << answer() << endl;
    }
}
