#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <sstream>
#include <ctime>
#include <set>
#define  N   362
#define  M   1200
#define  inf 0XFFFFFFFFFFFFFFll
#define  mod 1000000007
#define  LL  long long
#define  eps 1e-12
#define  pi  acos(-1.0)

using namespace std;

ofstream fo("A-large.out");
ifstream fi("A-large.in");
#define cout fo
#define cin fi

char s[10][10];

int main()
{
    int cases; cin >> cases;
    for (int c=1; c<=cases; c++) {
        cout << "Case #" << c << ": ";
        bool flag = true;
        for (int i=1; i<=4; i++)
            cin >> s[i]+1;
        int cntx = 0, cnty = 0;
        for (int i=1; i<=4; i++) {
            cntx = cnty = 0;
            for (int j=1; j<=4; j++) {
                if (s[i][j] == '.')
                    flag = false;
                if (s[i][j] == 'X' || s[i][j] == 'T')
                    cntx++;
                if (s[i][j] == 'O' || s[i][j] == 'T')
                    cnty++;
            }
            if (cntx == 4)
                break;
            if (cnty == 4)
                break;
        }

        if (cntx == 4) {
            cout << "X won" << endl;
            continue;
        }
        if (cnty == 4) {
            cout << "O won" << endl;
            continue;
        }


        for (int j=1; j<=4; j++) {
            cntx = cnty = 0;
            for (int i=1; i<=4; i++) {
                if (s[i][j] == 'X' || s[i][j] == 'T')
                    cntx++;
                if (s[i][j] == 'O' || s[i][j] == 'T')
                    cnty++;
            }
            if (cntx == 4)
                break;
            if (cnty == 4)
                break;
        }

        if (cntx == 4) {
            cout << "X won" << endl;
            continue;
        }
        if (cnty == 4) {
            cout << "O won" << endl;
            continue;
        }

        cntx = cnty = 0;
        for (int i=1; i<=4; i++) {
            if (s[i][i] == 'X'||s[i][i] == 'T')
                cntx++;
            if (s[i][i] == 'O'||s[i][i] == 'T')
                cnty++;
        }
        if (cntx == 4) {
            cout << "X won" << endl;
            continue;
        }
        if (cnty == 4) {
            cout << "O won" << endl;
            continue;
        }

        cntx = cnty = 0;
        for (int i=1; i<=4; i++) {
            if (s[i][5-i] == 'X'||s[i][5-i] == 'T')
                cntx++;
            if (s[i][5-i] == 'O'||s[i][5-i] == 'T')
                cnty++;
        }
        if (cntx == 4) {
            cout << "X won" << endl;
            continue;
        }
        if (cnty == 4) {
            cout << "O won" << endl;
            continue;
        }
        if (!flag)
            cout << "Game has not completed" << endl;
        else
            cout << "Draw" << endl;
    }
    return 0;
}

/*
6
 XXXT
 ....
 OO..
 ....

XOXT
 XXOO
 OXOX
 XXOO

XOX.
 OX..
 ....
 ....

OOXX
 OXXX
 OX.T
 O..O

XXXO
 ..O.
 .O..
 T...

OXXX
 XO..
 ..O.
 ...O



Case #1: X won
 Case #2: Draw
 Case #3: Game has not completed
 Case #4: O won
 Case #5: O won
 Case #6: O won
*/
