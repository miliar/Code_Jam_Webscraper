#include<iostream>
#include<fstream>
#include<string>
using namespace std;

void stat(char c, int &x, int &o, int &t, int &state) {
    switch (c) {
        case 'X': ++x; break;
        case 'O': ++o; break;
        case 'T': ++t; break;
        default: state = 3;//not completed
    }
}

bool test_complete(int x, int o, int t, int &state) {
    if(x + t == 4) state = 1;//x won
    else if(o + t == 4) state = 2;//o won
    else return false;

    return true;
}

int game_state(char board[4][4]) {
    int state = 0;//draw
    
    for(int i = 0; i < 4; ++i) {
        int x = 0, o = 0, t = 0;
        for(int j = 0; j < 4; ++j)
            stat(board[i][j], x, o, t, state);
        if(test_complete(x, o, t, state)) return state;
        
        x = o = t = 0;
        for(int j = 0; j < 4; ++j)
            stat(board[j][i], x, o, t, state);
        if(test_complete(x, o, t, state)) return state;
    }

    int x = 0, o = 0, t = 0;
    for(int i = 0; i < 4; ++i)
        stat(board[i][i], x, o, t, state);
    if(test_complete(x, o, t, state)) return state;

    x = o = t = 0;
    for(int i = 0; i < 4; ++i)
        stat(board[3-i][i], x, o, t, state);
    if(test_complete(x, o, t, state)) return state;

    return state;
}


int main(int argc, char **argv) {
    ifstream input(argv[1], ios::in);
    ofstream output("output.txt", ios::out);

    int T;
    input>>T;
    
    char board[4][4];
    for(int t = 0; t < T; ++t) {
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                input>>board[i][j];
            }
        }

        output<<"Case #"<<t+1<<": ";
        int s = game_state(board);
        switch (s) {
            case 0: output<<"Draw"<<endl; break;
            case 1: output<<"X won"<<endl; break;
            case 2: output<<"O won"<<endl; break;
            default: output<<"Game has not completed"<<endl;
        }
    }
 
    return 0;
}
