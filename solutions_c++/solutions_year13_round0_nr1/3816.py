#include <cstdlib>
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

bool winner(int win) {
    if (win==1)
        cout << "X won" << endl;
    else if (win==2)
        cout << "O won" << endl;
}

void solve() {
    int grid [4][4];  //0=., 1=X, 2=O, 3=T
    int x, y, win;
    bool blank=false;
    string buf;
    for (x=0; x<4; x++) {
        getline(cin, buf);
        for (y=0; y<4; y++) {
            switch (buf[y]) {
                case 'X':
                    grid[x][y]=1;
                    break;
                case 'O':
                    grid[x][y]=2;
                    break;
                case 'T':
                    grid[x][y]=3;
                    break;
                default:
                    grid[x][y]=0;
                    blank = true;
            }
        }
    }
    getline(cin, buf);
    

    for (x=0; x<4; x++) {
        win = 3;
        for (y=0; y<4; y++)
            win = win & grid[x][y];
        if (winner(win)) return;
    }
    
    for (y=0; y<4; y++) {
        win = 3;
        for (x=0; x<4; x++)
            win = win & grid[x][y];
        if (winner(win)) return;
    }
    
    win = 3;
    for (x=0; x<4; x++)
        win = win & grid[x][x];
    if(winner(win)) return;
    
    win = 3;
    for (x=0; x<4; x++)
        win = win & grid[x][3-x];
    if(winner(win)) return;
    
    if (blank)
        cout << "Game has not completed" << endl;
    else
        cout << "Draw" << endl;
}


int main(int argc, char** argv) {
    int tmax;
    cin >> tmax;
    cin.ignore();
    
    for (int t=1; t<=tmax; t++) {
        
        cout << "Case #" << t << ": ";
        solve();
        //cout << endl;
    }
}
