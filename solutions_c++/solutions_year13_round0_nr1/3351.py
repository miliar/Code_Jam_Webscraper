#include <iostream>
#include <string>
#include <fstream>

using namespace std;

const int Xwin = 'X'+'X'+'X'+'X';
const int XT = 'X'+'X'+'X'+'T';
const int Owin = 'O'+'O'+'O'+'O';
const int OT = 'O'+'O'+'O'+'T';

struct Test{
    char board[4][4];
    int sums[10] = {0};

    void read(ifstream& in, bool& notFull){
        for(int i = 0; i < 4; ++i){
            for(int j = 0; j < 4; ++j){
                in >> board[i][j];
                if(board[i][j] == '.'){
                    notFull = true;
                }
            }
        }
    }

};

int main(){
    ifstream in;
    string inputString = "A-large.in";
    in.open(inputString.c_str());
    int numCases;
    in >> numCases;
    bool notFull, winner;
    for(int i = 0; i < numCases; ++i){
        {
        notFull = false;
        winner = false;
        Test test;
        test.read(in, notFull);
        
        for(int x = 0; x < 4; ++x){
            //check diags
            test.sums[0] += test.board[x][x];
            test.sums[1] += test.board[x][3-x];
            //check rows/columns
            for(int y = 0; y < 4; ++y){
                test.sums[x+2] += test.board[x][y];
                test.sums[x+6] += test.board[y][x];
            }
        }
        for(int z = 0; z < 10; ++z)
        {
            if(test.sums[z] == Owin || test.sums[z] == OT){
                cout << "Case #" << i+1 << ": " << "O won\n";
                winner = true;
                break;
            }
            else if(test.sums[z] == Xwin || test.sums[z] == XT){
                cout << "Case #" << i+1 << ": " << "X won\n";
                winner = true;
                break;
            }
        }
        if(!winner){

            if(notFull){
                cout << "Case #" << i+1 << ": " << "Game has not completed\n";
            }

            else cout << "Case #" << i+1 << ": " << "Draw\n";
        
        }
    }
    }
    in.clear();
    in.close();
    return 0;
}

