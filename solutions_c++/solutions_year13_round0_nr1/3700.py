#include <iostream>
#include <cstdio>
using namespace std;
int main()
{

    int i, j, k, m, n, t;
    int flag1, flag2;
    char a[5][5];
    char e;
    cin >> t;
    getchar();
    for (i = 0; i < t; i++) {
        int flag3 = 0;
        int p = 0;
        for (j = 0; j < 4; j++) {
            for (k = 0; k < 4; k++) {
		    cin >> a[j][k];
               
                if (a[j][k] == '.') {
                    p = 1;
                }
            }
	    getchar();
        }
        cout << "Case #"<< i+1<< ": ";
        for (j = 0; j < 4; j++) {
            flag1 = 0;
            for (k = 0; k < 3; k++) {
                if (a[j][k] != a[j][k+1] || a[j][k] == '.') {
                    if ((a[j][k] == 'T' && (k == 0 || a[j][k-1] == a[j][k+1])) || (flag1 != 1 && a[j][k+1] == 'T') ){
                        flag1 = 1;
                    }
                    else {
                        flag2 = 0;
                        break;
                    }
                }
                else {
                    e = a[j][k];
                    flag2 = 1;
                }
            }
            if (flag2 == 1) {

                cout  <<  e << " won " << endl;
                flag3 = 1;
                break;
            }
        }
        for (j = 0; j < 4; j++) {
            flag1 = 0;
            for (k = 0; k < 3; k++) {
                if (a[k][j] != a[k+1][j] || a[k][j] == '.') {
                    if ( (a[k][j] == 'T' && (k == 0 || a[k-1][j] == a[k+1][j])) || ( (flag1 != 1) && (a[k+1][j] == 'T'))) {
                        flag1 = 1;
                    }
                    else {
                        flag2 = 0;
                        break;
                    }
                }
                else {
                    e = a[k][j];
                    flag2 = 1;
                }
            }
            if (flag2 == 1 && flag3 == 0) {
                    cout <<  e << " won " << endl;
                	flag3 = 1;
                	break;
            }
        }
        flag1 = 0;
        for (j = 0; j < 3; j++) {
            if (a[j][j] != a[j+1][j+1] || a[j][j] == '.') {
                if ((a[j][j] == 'T' && (j == 0 || a[j-1][j-1] == a[j+1][j+1])) || (flag1 != 1 && a[j+1][j+1] == 'T')) {
                    flag1 = 1;

                }
                else {
                    flag2 = 0;
                    break;
                }
            }
            else {
                e = a[j][j];
                flag2 = 1;
            }

        }
        if (flag2 == 1 && flag3 == 0) {
            cout << e << " won " << endl;

            flag3 = 1;
        }
        flag1 = 0;
        for (j = 0; j < 3; j++) {
            if (a[j][3-j] != a[j+1][2-j] ||a[j][3-j] == '.') {
                if ((a[j][3-j] == 'T' && (j == 0 || a[j-1][4-j] == a[j+1][2-j])) || (flag1 != 1 && a[j+1][2-j] == 'T')) {
                    flag1 = 1;

                }
                else {
                    flag2 = 0;
                    break;
                }
            }
            else {
                    e = a[j][3-j];
                flag2 = 1;
            }
        }
        if (flag2 == 1 && flag3 == 0) {
                cout << e<< " won " << endl;
            	flag3 = 1;
        }
        if (flag3 == 0) {
            if (p == 1) {
                cout << "Game has not completed" << endl;
            }
            else {
                cout << "Draw" << endl;
            }
	}
    }
    return 0;
}
