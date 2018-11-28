#include<iostream>
#include<vector>
#include<string>
using namespace std;

bool checkhorizontal(const vector<string> &board, char &winner){
    bool check = false;
    for(int i=0;i < 4;i++){
        if((board[i][0] == 'T' || board[i][0] == 'X') &&
            (board[i][1] == 'T' || board[i][1] == 'X') &&
            (board[i][2] == 'T' || board[i][2] == 'X') &&
            (board[i][3] == 'T' || board[i][3] == 'X')){
            check = true;
            winner = 'X';
            break;
            }
        if((board[i][0] == 'T' || board[i][0] == 'O') &&
            (board[i][1] == 'T' || board[i][1] == 'O') &&
            (board[i][2] == 'T' || board[i][2] == 'O') &&
            (board[i][3] == 'T' || board[i][3] == 'O')){
            check = true;
            winner = 'O';
            break;
            }
    }
    return check;

}

bool checkvertical(const vector<string> &board, char &winner){
    bool check = false;
    for(int i=0;i < 4;i++){
        if((board[0][i] == 'T' || board[0][i] == 'X') &&
            (board[1][i] == 'T' || board[1][i] == 'X') &&
            (board[2][i] == 'T' || board[2][i] == 'X') &&
            (board[3][i] == 'T' || board[3][i] == 'X')){
            check = true;
            winner = 'X';
            break;
            }
        if((board[0][i] == 'T' || board[0][i] == 'O') &&
            (board[1][i] == 'T' || board[1][i] == 'O') &&
            (board[2][i] == 'T' || board[2][i] == 'O') &&
            (board[3][i] == 'T' || board[3][i] == 'O')){
            check = true;
            winner = 'O';
            break;
            }
    }
    return check;

}

bool checkdiagonal1(const vector<string> &board, char &winner){
    bool check = false;
    if((board[0][0] == 'T' || board[0][0] == 'X') &&
            (board[1][1] == 'T' || board[1][1] == 'X') &&
            (board[2][2] == 'T' || board[2][2] == 'X') &&
            (board[3][3] == 'T' || board[3][3] == 'X')){
        check = true;
        winner = 'X';
    }
    if((board[0][0] == 'T' || board[0][0] == 'O') &&
            (board[1][1] == 'T' || board[1][1] == 'O') &&
            (board[2][2] == 'T' || board[2][2] == 'O') &&
            (board[3][3] == 'T' || board[3][3] == 'O')){
        check = true;
        winner = 'O';
    }
    return check;

}

bool checkdiagonal2(const vector<string> &board, char &winner){
    bool check = false;
    if((board[0][3] == 'T' || board[0][3] == 'X') &&
            (board[1][2] == 'T' || board[1][2] == 'X') &&
            (board[2][1] == 'T' || board[2][1] == 'X') &&
            (board[3][0] == 'T' || board[3][0] == 'X')){
        check = true;
        winner = 'X';
    }

    if((board[0][3] == 'T' || board[0][3] == 'O') &&
            (board[1][2] == 'T' || board[1][2] == 'O') &&
            (board[2][1] == 'T' || board[2][1] == 'O') &&
            (board[3][0] == 'T' || board[3][0] == 'O')){
        check = true;
        winner = 'O';
    }
    return check;

}
bool checkgame(const vector<string> &board){
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(board[i][j] == '.')
                return true;
        }
    }
    return false;
}

int main(){
    int t;
    cin>>t;
    for(int j=0;j < t;j++){
        vector<string> board;
        string temp;
        for(int i=0;i< 4;i++){
            cin>>temp;
            board.push_back(temp);
        }
        char winner = '.';

        if(checkhorizontal(board, winner))
            cout<<"Case #"<<j + 1<<": "<<winner<<" won"<<endl;

        else if(checkvertical(board, winner))
            cout<<"Case #"<<j + 1<<": "<<winner<<" won"<<endl;

        else if(checkdiagonal1(board, winner))
            cout<<"Case #"<<j + 1<<": "<<winner<<" won"<<endl;

        else if(checkdiagonal2(board, winner))
            cout<<"Case #"<<j + 1<<": "<<winner<<" won"<<endl;
        else if(checkgame(board))
            cout<<"Case #"<<j + 1<<": "<<"Game has not completed"<<endl;
        else
            cout<<"Case #"<<j + 1<<": "<<"Draw"<<endl;
    }
}
