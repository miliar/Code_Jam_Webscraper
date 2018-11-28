#include <iostream>

using namespace std;

int main(void)
{
    int t;
    cin >>t;
    for (int i = 1; i <= t; i++) {
        char chess[4][4];
        
        cin >>chess[0];
        cin >>chess[1];
        cin >>chess[2];
        cin >>chess[3];
        
        int count = 0;
        for (int j = 0; j < 4; j++) {
            for (int k = 1; k < 4; k++) {
                if (chess[j][k] == '.') {
                    count++;
                }
            }
        }

        bool flag = false;
        char now = ' ';
        for (int j = 0; j < 4; j++) {
            for (int k = 1; k < 4; k++) {
                now = chess[j][0];
                if (now == '.') {
                    break;
                }
                if (now == 'T') {
                    now = chess[j][1];
                    k++;
                }
                if (chess[j][k] != now && chess[j][k] != 'T') {
                    break;
                }
                if (k == 3) {
                    flag = true;
                    
                }
            }
            if (flag) {
                break;
            }
            
            for (int k = 1; k < 4; k++) {
                now = chess[0][j];
                if (now == '.') {
                    break;
                }
                if (now == 'T') {
                    now = chess[1][j];
                    k++;
                }
                if (chess[k][j] != now && chess[k][j] != 'T') {
                    break;
                }
                if (k == 3) {
                    flag = true;
                    
                }
            }
            if (flag) {
                break;
            }
        }
        
        if (!flag) {
            now = chess[0][0];
            if (now != '.') {
                if (now == 'T') {
                    now = chess[1][1];
                }
                if ((chess[2][2] == now || chess[2][2] == 'T') && (chess[3][3] == now || chess[3][3] == 'T')) {
                    flag = true;
                }
            }
            
            if (!flag) {
                now = chess[0][3];
                if (now != '.') {
                    if (now == 'T') {
                        now = chess[1][2];
                    }
                    if ((chess[2][1] == now || chess[2][1] == 'T') && (chess[3][0] == now || chess[3][0] == 'T')) {
                        flag = true;
                    }
                }
            }
        }
        
        if (flag) {
            cout <<"Case #" <<i <<": " <<now <<" won" <<endl;
        }
        else {
            if (count == 0) {
                cout <<"Case #" <<i <<": " <<"Draw" <<endl;
            }
            else {
                cout <<"Case #" <<i <<": " <<"Game has not completed" <<endl;
            }
        }
    }
    
    return 0;
}

