#include <iostream>

using namespace std;
typedef char board[4][4];

char win(board b);
void print(board b);

int main()
{

    board b;
    int number;
    char winner = '.';

    cin >> number;
    for(int i = 0; i < number; ++i){
        for(int y = 0; y < 4; ++y){
            for(int x = 0; x < 4; ++x){
                cin >> b[x][y];
            }
        }
        cout << "Case #" << i+1 << ": ";
        winner = win(b);
        if(winner == '.'){
            cout << "Game has not completed" << endl;
        }else if(winner == 'D'){
            cout << "Draw" << endl;
        }else{
            cout << winner << " won" << endl;
        }

        //print(b);
    }
    return 0;
}

void print(board b){
    for(int y = 0; y < 4; ++y){
        for(int x = 0; x < 4; ++x){
            cout << b[x][y];
        }
        cout << endl;
    }
}

char win(board b){
    char last = '.';
    int number = 1;

    //CHECK X
    for(int y = 0; y < 4; ++y){
        last = b[0][y];
        number = 1;
        for(int x = 1; x < 4; ++x){
            if(last == 'T'){
                number++;
                last = b[x][y];
            }else if((b[x][y] == 'X' || b[x][y] == 'O' || b[x][y] == 'T') && (b[x][y] == 'T' || b[x][y] == last)){
                number++;
            }
        }
        if(number >= 4){
            return last;
        }
    }

    //CHECK Y
    for(int x = 0; x < 4; ++x){
        last = b[x][0];
        number = 1;
        for(int y = 1; y < 4; ++y){
            if(last == 'T'){
                number++;
                last = b[x][y];
            }else if((b[x][y] == 'X' || b[x][y] == 'O' || b[x][y] == 'T') && (b[x][y] == 'T' || b[x][y] == last)){
                number++;
            }
        }
        if(number >= 4){
            return last;
        }
    }

    number = 1;
    last = b[0][3];
    if(last == 'O' || last == 'X' || last == 'T'){
        for(int xy = 1; xy < 4; ++xy){
            if(last == 'T'){
                number++;
                last = b[xy][3-xy];
            }else if(b[xy][3-xy] == last || b[xy][3-xy] == 'T'){
                number++;
            }else{
                break;
            }
        }
        if(number >= 4){
            return last;
        }
    }


    number = 1;
    last = b[0][0];
    if(last == 'O' || last == 'X' || last == 'T'){
        for(int xy = 1; xy < 4; ++xy){
            if(last == 'T'){
                number++;
                last = b[xy][xy];
            }else if(b[xy][xy] == last || b[xy][xy] == 'T'){
                number++;
            }else{
                break;
            }
        }
        if(number >= 4){
            return last;
        }
    }

    for(int y = 0; y < 4; ++y){
        for(int x = 0; x < 4; ++x){
            if(b[x][y] == '.'){
                return '.';
            }
        }
    }


    return 'D';
}

