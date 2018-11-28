#include <iostream>

using namespace std;
int board[4][4];

int check(){
        int state[4][4];

        for(int i = 0; i < 4; i++)
                for(int j = 0; j < 4; j++)
                        state[i][j] = board[i][j];
        for(int i = 0; i < 4; i++){
                int x = 0;
                int o = 0;
                int t = 0;
                for(int j = 0; j < 4; j++){
                        x += ((state[i][j] == 'X') ? 1 : 0);
                        o += ((state[i][j] == 'O') ? 1 : 0);
                        t += ((state[i][j] == 'T') ? 1 : 0);
                        if (x + t == 4) return 1;
                        if (o + t == 4) return 2;
                }
        }
        for(int j = 0; j < 4; j++){
                int x = 0;
                int o = 0;
                int t = 0;
                for(int i = 0; i < 4; i++){
                        x += ((state[i][j] == 'X') ? 1 : 0);
                        o += ((state[i][j] == 'O') ? 1 : 0);
                        t += ((state[i][j] == 'T') ? 1 : 0);
                        if (x + t == 4) return 1;
                        if (o + t == 4) return 2;
                }
        }

        int x = 0, o = 0, t = 0;
        for(int i = 0; i < 4; i++){
                int j = i;
                x += ((state[i][j] == 'X') ? 1 : 0);
                o += ((state[i][j] == 'O') ? 1 : 0);
                t += ((state[i][j] == 'T') ? 1 : 0);
                if (x + t == 4) return 1;
                if (o + t == 4) return 2;
        }
        x = 0; o = 0; t = 0;
        for(int i = 0; i < 4; i++){
                int j = 3-i;
                x += ((state[i][j] == 'X') ? 1 : 0);
                o += ((state[i][j] == 'O') ? 1 : 0);
                t += ((state[i][j] == 'T') ? 1 : 0);
                if (x + t == 4) return 1;
                if (o + t == 4) return 2;
        }

        for(int i = 0; i < 4; i++)
                for(int j = 0; j < 4; j++){
                        if (state[i][j] == '.')
                                return 3;
                }
        return 4;
}
                        
                       

                        
                        

                        
        
        
int main(){
        int t;
        cin >> t;
        for(int c = 1; c <= t; c++){

                for(int i = 0; i < 4; i++){
                        string s;
                        cin >> s;
                        for(int j = 0; j < 4; j++)
                                board[i][j] = s[j];
                }
                int x = check();
                if (x == 1){
                        cout << "Case #" << c << ": X won" << endl;
                }
                else if (x == 2){
                        cout << "Case #" << c << ": O won" << endl;
                }
                else if (x == 3){
                        cout << "Case #" << c << ": Game has not completed" << endl;
                }
                else if (x == 4){
                        cout << "Case #" << c << ": Draw" << endl;
                }
                // string s;
                // cin >> s;

        }
        return 0;
        
}
                        
