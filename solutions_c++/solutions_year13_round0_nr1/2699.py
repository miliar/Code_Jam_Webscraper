#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool check(string, int, int, ofstream&);

int main(int argc, const char * argv[])
{
    ifstream fin;
    ofstream fout;
    fin.open("A-large.in");
    fout.open("A-large.out");
    
    int T;
    fin >> T;
    
    for(int i = 1; i <= T; i++){
        string board, temp;
        for(int j = 0; j < 4; j++){
            fin >> temp;

            board += temp;
            
        }
        fout << "Case #" << i << ": ";
        if(check(board, 0, 5, fout)){
            
        }
        else if(check(board, 3, 3, fout)){
            
        }
        else{
            bool flag = false;
            for(int k = 0; k < 4; k++){
                if(check(board, k, 4, fout)){
                    flag = true;
                    break;
                }
                if(check(board, k * 4, 1, fout)){
                    flag = true;
                    break;
                }
            }
            if(!flag){
                if(board.find('.') == string::npos)
                    fout << "Draw";
                else
                    fout << "Game has not completed";
            }
        }
        fout << endl;
    }
    
    fout.close();
    fin.close();
    return 0;
}

bool check(string b, int pos, int inc, ofstream& fout){
    char player = b[pos];
    if(player == '.')
        return false;
    
    if(player == 'T' && b[pos + inc] != '.')
        player = b[pos + inc];
    
    for(int k = 1; k < 4; k++){
        pos += inc;
        if(player != b[pos]){
            if(b[pos] != 'T')
                return false;
        }
    }
    fout << player << " won";
    return true;
}