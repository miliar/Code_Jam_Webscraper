#include <iostream>

using namespace std;

int main(){
    string s[4];
    int table[256];
    int t;

    cin >> t;

    for(int w = 0; w < t; w++){
        for(int x = 0; x < 4; x++)
            cin >> s[x];

        char winner = 0;
        table['.'] = 0;

        for(int j = 0; j < 4; j++){
            table['X'] = 0;
            table['O'] = 0;
            table['T'] = 0;

            for(int i = 0; i < 4; i++){
                table[s[j][i]]++;
            }

            if(table['X'] + table['T'] == 4)
                winner = 'X';
            else if(table['O'] + table['T'] == 4)
                winner = 'O';
        }

        for(int j = 0; j < 4; j++){
            table['X'] = 0;
            table['O'] = 0;
            table['T'] = 0;

            for(int i = 0; i < 4; i++){
                table[s[i][j]]++;
            }

            if(table['X'] + table['T'] == 4)
                winner = 'X';
            else if(table['O'] + table['T'] == 4)
                winner = 'O';
        }

        table['X'] = 0;
        table['O'] = 0;
        table['T'] = 0;

        for(int i = 0; i < 4; i++){
            table[s[i][i]]++;
        }

        if(table['X'] + table['T'] == 4)
            winner = 'X';
        else if(table['O'] + table['T'] == 4)
            winner = 'O';

        table['X'] = 0;
        table['O'] = 0;
        table['T'] = 0;

        for(int i = 0; i < 4; i++){
            table[s[i][3-i]]++;
        }

        if(table['X'] + table['T'] == 4)
            winner = 'X';
        else if(table['O'] + table['T'] == 4)
            winner = 'O';

        if(winner != 0)
            cout << "Case #" << (w+1) << ": " << winner << " won" << endl;
        else if(table['.'] == 0)
            cout << "Case #" << (w+1) << ": Draw" << endl;
        else
            cout << "Case #" << (w+1) << ": Game has not completed" << endl;
    }

    return 0;
}
