// mrozik

#include <string>
#include <iostream>
using namespace std;


string board;

bool check(char c, int pos0, int step) {
    for (int i=0; i<4; i++)
        if (board[pos0+i*step]!=c && board[pos0+i*step]!='T')
            return false;
    return true;
}


bool check(char c) {
    return
        check(c, 0, 1) || check(c, 4, 1) || check(c, 8, 1) || check(c, 12, 1) // horiz
        || check(c, 0, 4) || check(c, 1, 4) || check(c, 2, 4) || check(c, 3, 4) // vert
        || check(c, 0, 5) || check(c, 3, 3);
}


bool eog() {
    return board.find('.')==string::npos;
}


int main() {
    int T; cin>>T;
    for (int t=1; t<=T; t++) {
        string b[4];
        cin>>b[0]>>b[1]>>b[2]>>b[3];
        board = b[0]+b[1]+b[2]+b[3];
        
        if (check('X'))
            cout<<"Case #"<<t<<": X won"<<endl;
        else if (check('O'))
            cout<<"Case #"<<t<<": O won"<<endl;
        else if (eog())
            cout<<"Case #"<<t<<": Draw"<<endl;
        else
            cout<<"Case #"<<t<<": Game has not completed"<<endl;
    }
}

