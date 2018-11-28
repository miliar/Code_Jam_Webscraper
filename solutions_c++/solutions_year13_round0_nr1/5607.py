#include <iostream>

using namespace std;

char check(char a[5][5], int p, int q) {
    int flag = 1, flag1 = 1, flag2 = 1, flag3 = 1;
    if (a[p][q] == 'X' || a[p][q] == 'T') {
        for (int i = 0; i < 4; i++) {
            if (a[p][i] == 'O' || a[p][i] == '.') {
                flag = 0;
             //   cout << "nn\n";
                break;
            }else {
                flag = 1;
            }
        }

        for (int i = 0; i < 4; i++) {
            if (a[i][q] == 'O' || a[i][q] == '.') {
                flag1 = 0;
              //  cout << "vv\n";
                break;
            }else {
                flag1 = 1;
            }
        }
        if ((p == 0 && q == 0) || (p == 0 && q == 3)) {
            if (p == 0 && q == 0) {
                for (int i = 0; i < 4; i++) {
                        if (a[i][i] == 'O' || a[i][i] == '.') {
                                flag2 = 0;
                                flag3 = 0;
                                break;
                        }else {
                            flag2 = 1;
                        }
                }
            }else {
                for (int i = 3; i >= 0; i--) {
                    if (a[q-i][i] == 'O' || a[q-i][i] == '.') {
                        flag3 = 0;
                        flag2 = 0;
                        break;
                    }else {
                        flag3 = 1;
                    }
                }
            }
        }else {
            flag3 = 0;
            flag2 = 0;
        }
            if (flag == 1 || flag1 == 1 || flag2 == 1 || flag3 == 1) {
                return 'X';
            }else {
                return 'Y';
            }
    }else if (a[p][q] == 'O' || a[p][q] == 'T'){
        for (int i = 0; i < 4; i++) {
            if (a[p][i] == 'X' || a[p][i] == '.') {
                flag = 0;
               // cout << "1\n";
                break;
            }else {
                flag = 1;
            }
        }
        for (int i = 0; i < 4; i++) {
            if (a[i][q] == 'X' || a[i][q] == '.') {
                flag1 = 0;
             //   cout << "2\n";
                break;
            }else {
                flag1 = 1;
            }
        }
        if ((p == 0 && q == 0) || (p == 0 && q == 3)) {
            if (p == 0 && q == 0) {
                for (int i = 0; i < 4; i++) {
                        if (a[i][i] == 'X' || a[i][i] == '.') {
                                flag2 = 0;
                                flag3 = 0;
                                break;
                        }else {
                            flag2 = 1;
                        }
                }
            }else {
                for (int i = 3; i >= 0; i--) {
                    if (a[q-i][i] == 'X' || a[q-i][i] == '.') {
                        flag3 = 0;
                        flag2 = 0;
                        break;
                    }else {
                        flag3 = 1;
                    }
                }
            }
        }else {
            flag3 = 0;
            flag2 = 0;
        }
        if (flag == 1 || flag1 == 1 || flag2 == 1 || flag3 == 1) {
                return 'O';
            }else {
                return 'Y';
            }
        }
}
int main() {
    int t;
    cin >> t;
    char a[5][5];
    for (int h = 1; h <= t; h++) {
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> a[i][j];
            }
        }
        int flag = 0, flag1 = 0,  tog = 0, tog1 = 0;
        for (int i = 0 ; i < 4; i++) {
            if (tog != 1 && tog1 != 1) {
            for (int j = 0; j < 4; j++) {
                if (a[i][j] != '.') {
                    char p =check(a, i, j);
                   // cout << " i = " << i << " " << "j = " << j << endl;
                   // cout << "p = " << p << endl;
                    if (p == 'X') {
                        cout << "Case #" << h << ": " << "X won\n";
                        tog = 1;
                        tog1 = 1;
                        break;
                    }else if(p == 'O') {
                        cout << "Case #" << h << ": " << "O won\n";
                        tog1 = 1;
                        tog = 1;
                        break;
                    }else {
                        flag = 1;
                    }
                }else {
                    flag1 = 1;
                }
            }
        }else {
            break;
        }
        }
      //  cout << "tog = " << tog << " " << "tog1 = " << tog1 << endl;
        if (tog == 0 || tog1 == 0) {
            if (flag1 == 1) {
                   cout << "Case #" << h << ": " << "Game has not completed\n";
                 //cout << "Case #" << h << ": " << "Draw\n";
            }else if (flag == 1 && flag1 == 0) {
                 cout << "Case #" << h << ": " << "Draw\n";
            }

    }

    }

    return 0;
}

