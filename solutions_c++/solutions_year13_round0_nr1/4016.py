// Tic-Tac-Toe-Tomek

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

int Board[4][4];

int test_four(int a, int b, int c, int d)
{
    if (a == 0 || b == 0 || c == 0 || d == 0) return 0;
    else if (a == 3) {if (b == c && c == d && b != 0)  return b;}
        else if ((b == a || b == 3) && (c == a || c == 3) && (d == a || d == 3)) return a;
    return 3;
}

int decide(int Board[4][4])
{
    bool finished = true;
    int i = 0, res;
    while (i < 4) {
        res = test_four(Board[i][0],Board[i][1],Board[i][2],Board[i][3]);
        if (res == 1 || res == 2) return res; if (res == 0) finished = false;
        res = test_four(Board[0][i],Board[1][i],Board[2][i],Board[3][i]);
        if (res == 1 || res == 2) return res; if (res == 0) finished = false;
        ++i;
    }
    res = test_four(Board[0][0], Board[1][1], Board[2][2], Board[3][3]);
    if (res == 1 || res == 2) return res;
    res = test_four(Board[0][3], Board[1][2], Board[2][1], Board[3][0]);
    if (res == 1 || res == 2) return res;
    if (!finished) return 0; else return 3;
}
void print_board(int Board[4][4])
{
    for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
        cout << Board[i][j] << ' ';
    }   cout << endl;
    }
}


int main()
{
    ifstream fin("A-large.in");
    freopen("A-large.out", "w", stdout);
/*
    int res;
    cout << test
    cout << test_four(1,1,1,3) << endl;
    cout << test_four(1,1,1,2) << endl;
    cout << test_four(2,1,1,1) << endl;
    cout << test_four(2,2,2,3) << endl;
*/

    int T;
    fin >> T;
    char c;
    int a;
    int test_res;
    string line;
    getline(fin, line);
    for (int t = 1; t <= T; ++t) {
        for (int k = 0; k < 4; ++k){
            getline(fin, line);
            for(int i = 0; i < 4; ++i)
            {c = line[i];
            if      (c == '.') a = 0;
            else if (c == 'X') a = 1;
            else if (c == 'O') a = 2;
            else if (c == 'T') a = 3;
            Board[k][i] = a;}
        }
        getline(fin, line);
        //print_board(Board);
        test_res = decide(Board);
        if (test_res == 0) printf("Case #%d: Game has not completed\n", t);
        else if (test_res == 1) printf("Case #%d: X won\n", t);
        else if (test_res == 2) printf("Case #%d: O won\n", t);
        else printf("Case #%d: Draw\n", t);
    }

    return 0;
}
