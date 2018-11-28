#include <iostream>
#include <vector>
#include <string>

using namespace std;
int i, j;

int main() {
    
    freopen("tomek.in","r",stdin);
    freopen("tomek.out","w",stdout);

    int t;
    cin >> t;

    for(int t_case = 1; t_case <= t; ++t_case) {
        
        vector<string> table(4);
        bool winnerO = false, winnerX = false, has_void = false;

        for(i = 0; i < 4; ++i)
            cin >> table[i];
        
        for(i = 0; i < 4; ++i) {
            int Os = 0, Xs = 0;

            for(j = 0; j < 4; ++j) {
                Os += (table[i][j] == 'O' || table[i][j] == 'T');
                Xs += (table[i][j] == 'X' || table[i][j] == 'T');
                if(table[i][j] == '.')
                    has_void = true;
            }

            if(Os == 4)
                winnerO = true;
            if(Xs == 4)
                winnerX = true;
        }

        for(j = 0; j < 4; ++j) {
            int Os = 0, Xs = 0;
            
            for(i = 0; i < 4; ++i) {
                Os += (table[i][j] == 'O' || table[i][j] == 'T');
                Xs += (table[i][j] == 'X' || table[i][j] == 'T');
            }

            if(Os == 4)
                winnerO = true;
            if(Xs == 4)
                winnerX = true;
        }
        
        int Os = 0, Xs = 0;

        for(i = 0; i < 4; ++i)
            Os += (table[i][i] == 'O' || table[i][i] == 'T'),
            Xs += (table[i][i] == 'O' || table[i][i] == 'T');

        if(Os == 4)
            winnerO = true;
        if(Xs == 4)
            winnerX = true;

        Os = 0, Xs = 0;

        for(i = 0; i < 4; ++i)
            Os += (table[i][3 - i] == 'O' || table[i][3 - i] == 'T'),
            Xs += (table[i][3 - i] == 'T' || table[i][3 - i] == 'T');

        if(Os == 4)
            winnerO = true;
        if(Xs == 4)
            winnerX = true;
        
        cout << "Case #" << t_case <<": ";

        if(winnerO)
            cout << "O won\n";
        else if(winnerX)
            cout << "X won\n";
        else if(has_void)
            cout << "Game has not completed\n";
        else
            cout << "Draw\n";
    }

    return 0;
}
