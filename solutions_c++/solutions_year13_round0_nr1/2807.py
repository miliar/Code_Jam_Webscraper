#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define SIZE(A) ((int)(A).size())
#define ALL(A) (A).begin(),(A).end()
#define fi first
#define se second
#define pb push_back
#define mp make_pair

using namespace std ;

#define INFILE "date.in"
#define	OUTFILE "date.out"
//#define cin F
//#define cout G

ifstream F (INFILE) ;
ofstream G (OUTFILE) ;

int T, nrO, nrX, nrT, nrP = 0 ;
vector < string > V(4, "") ;

void Read() ;
void Solve() ;
void test(int i, int j) ;

int main() {
    int i ;
    cin >> T ;
    for (i = 1; i <= T; ++i) {
        Read() ;
        nrP = 0 ;
        //cin.get() ;
        cout << "Case #" << i << ": " ;
        Solve() ;
    }
	F.close() ;
	G.close() ;
	return 0;
}

void Read() {
    int i ;
    for (i = 0; i < 4; ++i) {
        cin >>V[i] ;
        //cout << V[i] ;
    }
}

void Solve() {
    int i, j;
    for (i = 0; i < 4; ++i) {
        nrX = nrT = nrO = 0 ;
        for (j = 0; j < 4; ++j) {
             test(i, j) ;
             if (V[i][j] == '.') {
                nrP ++ ;
            }
        }
        if ((nrX == 3 && nrT) || nrX == 4) {
            cout << "X won\n" ;
            return ;
        }
        if ((nrO == 3 && nrT) || nrO == 4) {
            cout << "O won\n" ;
            return ;
        }
    }

    for (j = 0; j < 4; ++j) {
        nrX = nrT = nrO = 0 ;
        for (i = 0; i < 4; ++i) {
                test(i, j) ;
            if ((nrX == 3 && nrT) || nrX == 4) {
                cout << "X won\n" ;
                return ;
            }
            if ((nrO == 3 && nrT) || nrO == 4) {
                cout << "O won\n" ;
                return ;
            }
        }
    }

    nrX = nrT = nrO = 0 ;
    for (i = 0; i < 4; ++i) {
        test(i, i) ;
    }
    if ((nrX == 3 && nrT) || nrX == 4) {
        cout << "X won\n" ;
        return ;
    }
    if ((nrO == 3 && nrT) || nrO == 4) {
        cout << "O won\n" ;
        return ;
    }

    nrX = nrT = nrO = 0 ;
    for (i = 0; i < 4; ++i) {
        test(i, 3 - i) ;
    }
    if ((nrX == 3 && nrT) || nrX == 4) {
        cout << "X won\n" ;
        return ;
    }
    if ((nrO == 3 && nrT) || nrO == 4) {
        cout << "O won\n" ;
        return ;
    }

    if (nrP == 0) {
        cout << "Draw\n" ;
        return ;
    }
    cout << "Game has not completed\n" ;
}

void test(int i, int j) {
    if (V[i][j] == 'X') {
        nrX ++ ;
    }
    if (V[i][j] == 'O') {
        nrO ++ ;
    }
    if (V[i][j] == 'T') {
        nrT ++ ;
    }
}
