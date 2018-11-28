#include <iostream>

using namespace std;

int main( void ) {
    bool unfinished = false;
    int t, w;
    char first, top;
    int firstCount, topCount;
    string ticTac[4];

    cin >> t;

    for(int k = 0; k < t; ++k) {
        unfinished = false;
        for(int i = 0; i < 4; ++i)
            cin >> ticTac[i];
        for(int i = 0; i < 4; ++i) {
            firstCount = 0;
            first = ticTac[i][0];
            if(first == 'T')
                first = ticTac[i][1];
            if(first == '.')
                continue;
            for(int j = 1; j < 4; ++j) {
                if(ticTac[i][j] == first || ticTac[i][j] == 'T') {
                    ++firstCount;
                }
            }
            if(firstCount == 3) {
                break;
            }
        }
        if(firstCount == 3) {
            cout << "Case #" << k+1 << ": " << first << " won\n";
            continue;
        }

        for(int i = 0; i < 4; ++i) {
            firstCount = 0;
            first = ticTac[0][i];
            if(first == 'T')
                first = ticTac[1][i];
            if(first == '.')
                continue;
            for(int j = 1; j < 4; ++j) {
                if(ticTac[j][i] == first || ticTac[j][i] == 'T') {
                    ++firstCount;
                }
            }
            if(firstCount == 3) {
                break;
            }
        }
        if(firstCount == 3) {
            cout << "Case #" << k+1 << ": " << first << " won\n";
            continue;
        }

        for(int i = 0; i < 1; ++i){
            firstCount = 0;
            first = ticTac[0][0];
            if(first == 'T'){
                first = ticTac[1][1];
            }
            if(first == '.')
                continue;
            if((ticTac[1][1] == first || ticTac[1][1] == 'T') && (ticTac[2][2] == first || ticTac[2][2] == 'T')
               &&  (ticTac[3][3] == first || ticTac[3][3] == 'T'))
                firstCount = 3;
        }
        if(firstCount == 3) {
            cout << "Case #" << k+1 << ": " << first << " won\n";
            continue;
        }

        for(int i = 0; i < 1; ++i){
            firstCount = 0;
            first = ticTac[0][3];
            if(first == 'T'){
                first = ticTac[1][2];
            }
            if(first == '.')
                continue;
            if((ticTac[1][2] == first || ticTac[1][2] == 'T') && (ticTac[2][1] == first || ticTac[2][1] == 'T')
               &&  (ticTac[3][0] == first || ticTac[3][0] == 'T'))
                firstCount = 3;
            }
        if(firstCount == 3) {
            cout << "Case #" << k+1 << ": " << first << " won\n";
            continue;
        }

        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                if(ticTac[i][j] == '.') {
                    unfinished = true;
                    break;
                }
            }
            if(unfinished) {
                break;
            }
        }
        if(unfinished) {
            cout << "Case #" << k+1 << ": Game has not completed\n";
        } else {
            cout << "Case #" << k+1 << ": Draw\n";
        }
    }
    return 0;
}
