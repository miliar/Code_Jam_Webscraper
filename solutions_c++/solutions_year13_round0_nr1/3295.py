#include<iostream>
#include<vector>

using namespace std;

int main () {
    vector< vector<char> > board(4, vector<char>(4));
    int T; cin >> T;   
    for (int i=0; i<T; i++) {
        string line;
        for (int j=0; j<4; j++) {
            cin >> line; 
            for (int k=0; k<4; k++)
                board[j][k] = line[k];    
        }
        int X_v, O_v, X_h, O_h;
        bool draw = true;
        bool finished = false;
        cout << "Case #" << i+1 << ": ";
        for (int a=0; a<4; a++) {
            X_v = 0, O_v = 0, X_h = 0, O_h = 0;
            for (int b=0; b<4; b++) {
                if (board[a][b] == '.') {
                    draw = false;            
                }
                else if (board[a][b] == 'X')
                     X_v++;
                else if (board[a][b] == 'O')
                     O_v++;
                else X_v++, O_v++;           
                
                if (board[b][a] == '.') {
                    draw = false;         
                }
                else if (board[b][a] == 'X')
                     X_h++;
                else if (board[b][a] == 'O')
                     O_h++;
                else X_h++, O_h++;           
            }
            if (X_v == 4 || X_h == 4) { 
                cout << "X won" << endl;      
                finished = true;
                break;
            }
            if (O_v == 4 || O_h == 4) {
                cout << "O won" << endl; 
                finished = true;
                break;
            }
        }
        X_v = 0, O_v = 0, X_h = 0, O_h = 0;
        for (int a=0; a<4 && !finished; a++) {
            
                if (board[a][a] == '.')    
                   draw = false;
                else if (board[a][a] == 'X')
                   X_v++;
                else if (board[a][a] == 'O')
                   O_v++;
                else 
                   X_v++, O_v++;     
                if (board[3-a][a] == '.')    
                   draw = false;
                else if (board[3-a][a] == 'X')
                   X_h++;
                else if (board[3-a][a] == 'O')
                   O_h++;
                else 
                   X_h++, O_h++;     
            
        }
        if (X_v == 4 || X_h == 4) { 
                cout << "X won" << endl;      
                finished = true;
                
            }
            if (O_v == 4 || O_h == 4) {
                cout << "O won" << endl;
                finished = true;
                            }
        if (draw && !finished) 
            cout << "Draw" << endl;
        else if (!finished) 
            cout << "Game has not completed" << endl;
    }
    return 1;
}
