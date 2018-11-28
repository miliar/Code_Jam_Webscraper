#include <iostream>
#include <vector>
using namespace std;

bool winner(vector<vector<bool> >);

int main() {
    int t;
    cin >> t;
    vector<vector<string> > input; 
    input.clear();
    for (int i = 0; i < t; i++) {
        vector<string> in;
        in.clear();
        string str;
        for (int j = 0; j < 4; j++) {
            cin >> str;
            in.push_back(str);
        }
        input.push_back(in);
    }

    for (int k = 0; k < t; k++) {
        cout << "Case #" << k+1 << ": ";
        vector<vector<bool> > model;
        model.resize(4);
        vector<string> in = input[k];
        bool isDotPresent = false;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (in[i][j] == 'X' || in[i][j] == 'T')
                    model[i].push_back(true);
                else
                    model[i].push_back(false);
                if (in[i][j] == '.')
                    isDotPresent = true;
            }
        }
        bool isWinner = winner(model);
        if (isWinner) {
            cout << "X won" << endl;
            continue;
        }
        model.clear();
        model.resize(4);
        for (int i = 0; i < 4; i++) {
           for (int j = 0; j < 4; j++) {
               if (in[i][j] == 'O' || in[i][j] == 'T')
                   model[i].push_back(true);
               else
                   model[i].push_back(false);
            }
        }
        isWinner = winner(model);
        if (isWinner) {
            cout << "O won"<<endl;
            continue;
        }
        if (isDotPresent)
            cout << "Game has not completed" << endl;
        else
            cout << "Draw" << endl;
    }
    
}

bool winner(vector<vector<bool> > model) {
    if ((model[0][0] && model[1][1] && model[2][2] && model[3][3]) || (model[0][3] && model[1][2] && model[2][1] && model[3][0]))
        return true;
    for (int i = 0; i < 4; i++) 
        if (model[i][0] && model[i][1] && model[i][2] && model[i][3])
            return true;
    for (int i = 0; i < 4; i++)
        if (model[0][i] && model[1][i] && model[2][i] &&  model[3][i])
            return true;
    return false;
}

