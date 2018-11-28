#include <iostream>
#include <string>
using namespace std;

int main(){
    int T, i, j, k;
    string dump;
    char B[4][4];
    bool won = false;
    bool fdot = false;
    cin >> T;
    for (i=0;i<T;i++){
        fdot = false;
        for (j=0;j<4;j++){
            for (k=0;k<4;k++){
                cin >> B[j][k];
                if (B[j][k] == '.') fdot = true;
            }
        }
        //getline(ifile, dump);
        for (j=0;j<4;j++){
            if (B[j][0] == '.') continue;
            won = true;
            for (k=1;k<4;k++){
                if (B[j][0] != B[j][k] && B[j][k] != 'T'){
                   won = false;
                   break;
                }
            }
            if (won) break;
        }
        if (won){
           cout << "Case #" << i+1 << ": " << B[j][0] << " won" << endl;
           continue;
        }
        
        for (j=0;j<4;j++){
            if (B[0][j] == '.') continue;
            won = true;
            for (k=1;k<4;k++){
                if (B[0][j] != B[k][j] && B[k][j] != 'T'){
                   won = false;
                   break;
                }
            }
            if (won) break;
        }
        if (won){
           cout << "Case #" << i+1 << ": " << B[0][j] << " won" << endl;
           continue;
        }
        
        if ((B[0][0] == 'O' || B[0][0] == 'T') && (B[1][1] == 'O' || B[1][1] == 'T') && (B[2][2] == 'O' || B[2][2] == 'T') && (B[3][3] == 'O' || B[3][3] == 'T')){
           cout << "Case #" << i+1 << ": O won" << endl;
           continue;
        }
        if ((B[0][0] == 'X' || B[0][0] == 'T') && (B[1][1] == 'X' || B[1][1] == 'T') && (B[2][2] == 'X' || B[2][2] == 'T') && (B[3][3] == 'X' || B[3][3] == 'T')){
           cout << "Case #" << i+1 << ": X won" << endl;
           continue;
        }
        if ((B[0][3] == 'O' || B[0][3] == 'T') && (B[1][2] == 'O' || B[1][2] == 'T') && (B[2][1] == 'O' || B[2][1] == 'T') && (B[3][0] == 'O' || B[3][0] == 'T')){
           cout << "Case #" << i+1 << ": O won" << endl;
           continue;
        }
        if ((B[0][3] == 'X' || B[0][3] == 'T') && (B[1][2] == 'X' || B[1][2] == 'T') && (B[2][1] == 'X' || B[2][1] == 'T') && (B[3][0] == 'X' || B[3][0] == 'T')){
           cout << "Case #" << i+1 << ": X won" << endl;
           continue;
        }
        if (fdot){
           cout << "Case #" << i+1 << ": Game has not completed" << endl;
           continue;
        }        
        cout << "Case #" << i+1 << ": Draw" << endl;
    }
}
