#include <iostream>
using namespace std;

#define CheckRow(arr, c, val) (arr[c][0]==val && arr[c][1]==val && arr[c][2]==val && arr[c][3] == val)
#define CheckCol(arr, c, val) (arr[0][c]==val && arr[1][c]==val && arr[2][c]==val && arr[3][c] == val)
#define CheckDia(arr, val) ((arr[0][0]==val && arr[1][1]==val && arr[2][2]==val && arr[3][3] == val) ||(arr[3][0]==val && arr[2][1]==val && arr[1][2]==val && arr[0][3] == val)) 

int main() {
    
    int T, flag;
    bool dotCheck;
    char temp, arr1[4][4], arr2[4][4];
    
    cin >> T;

    for (int i = 0; i < T; i++) {
        
        flag = 0;
        dotCheck = false;
        
        cout << "Case #" << i+1 << ": ";
        
        for (int j = 0; j < 4; j++) {
            for (int k = 0; k < 4; k++) {
                cin >> temp;
                if (temp == '.')
                    dotCheck = true;
                if (temp == 'T') {
                    arr1[j][k] = 'X';
                    arr2[j][k] = 'O';
                }
                else
                    arr1[j][k] = arr2[j][k] = temp;
            }
        }
        
        for (int j = 0; j < 4; j++) {
            if (CheckRow(arr1, j, 'X') || CheckCol(arr1, j, 'X') || CheckDia(arr1, 'X')) {
                flag = 1;
                break;
            }
            if (CheckRow(arr2, j, 'O') || CheckCol(arr2, j, 'O') || CheckDia(arr2, 'O')) {
                flag = 2;
                break;
            }
        }
        if (!flag && dotCheck)
            cout << "Game has not completed" << endl;
        else {
            if (flag == 1)
                cout << "X won" << endl;
            else if (flag == 2)
                cout << "O won" << endl;
            else
                cout << "Draw" << endl;
        }
    }
    
    return 0;
}
