#include <iostream>
#include <string>
#include <cstdio>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#include <stack>
#include <cctype>
#include <cstdlib>
#include <bitset>
#include <utility>
#include <cstring>

using namespace std;

const long double EPS = 1e-8;
const long double PI = 3.1415926535897932384626433832795;
const long double E = 2.7182818284;
const int INF = 1000000000;

typedef long long ll;
typedef long double ld;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define pb push_back
#define all(a) a.begin(), a.end()
#define mp make_pair;
#define X first
#define Y second

int main(void)
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        char tab[5][5];
        for(int j = 0; j < 4; j++) {
            for(int h = 0; h < 4; h++) {
                cin >> tab[j][h];
            }
        }
        int res = -1;
        for (int j = 0; j < 4; j++) {
            if ((tab[0][j] == 'X' || tab[0][j] == 'T') && (tab[1][j] == 'X' || tab[1][j] == 'T') && (tab[2][j] == 'X' || tab[2][j] == 'T') && (tab[3][j] == 'X' || tab[3][j] == 'T')) {res = 1; break;}
            if ((tab[0][j] == 'O' || tab[0][j] == 'T') && (tab[1][j] == 'O' || tab[1][j] == 'T') && (tab[2][j] == 'O' || tab[2][j] == 'T') && (tab[3][j] == 'O' || tab[3][j] == 'T')) {res = 2; break;}
        }
        if (res == -1) {
            for (int j = 0; j < 4; j++) {
                if ((tab[j][0] == 'X' || tab[j][0] == 'T') && (tab[j][1] == 'X' || tab[j][1] == 'T') && (tab[j][2] == 'X' || tab[j][2] == 'T') && (tab[j][3] == 'X' || tab[j][3] == 'T')) {res = 1; break;}
                if ((tab[j][0] == 'O' || tab[j][0] == 'T') && (tab[j][1] == 'O' || tab[j][1] == 'T') && (tab[j][2] == 'O' || tab[j][2] == 'T') && (tab[j][3] == 'O' || tab[j][3] == 'T')) {res = 2; break;}
            }
        }
        if (res == -1) {
            if ((tab[0][0] == 'X' || tab[0][0] == 'T') && (tab[1][1] == 'X' || tab[1][1] == 'T') && (tab[2][2] == 'X' || tab[2][2] == 'T') && (tab[3][3] == 'X' || tab[3][3] == 'T')) {res = 1;}
            if ((tab[0][0] == 'O' || tab[0][0] == 'T') && (tab[1][1] == 'O' || tab[1][1] == 'T') && (tab[2][2] == 'O' || tab[2][2] == 'T') && (tab[3][3] == 'O' || tab[3][3] == 'T')) {res = 2;}
            if ((tab[3][0] == 'X' || tab[3][0] == 'T') && (tab[2][1] == 'X' || tab[2][1] == 'T') && (tab[1][2] == 'X' || tab[1][2] == 'T') && (tab[0][3] == 'X' || tab[0][3] == 'T')) {res = 1;}
            if ((tab[3][0] == 'O' || tab[3][0] == 'T') && (tab[2][1] == 'O' || tab[2][1] == 'T') && (tab[1][2] == 'O' || tab[1][2] == 'T') && (tab[0][3] == 'O' || tab[0][3] == 'T')) {res = 2;}
        }
        if (res == -1) {
            for(int j = 0; j < 4; j++) {
                for(int h = 0; h < 4; h++) {
                    if (tab[j][h] == '.') {
                        res = 3;
                        break;
                    }
                }
            }
        }
        if (res == -1) res = 0;
        cout << "Case #" << i + 1 << ": ";
        if (res == 1) {
            cout << "X won" << endl;
        } else if (res == 2) {
            cout << "O won" << endl;
        } else if (res == 0) {
            cout << "Draw" << endl;
        } else {
            cout << "Game has not completed" << endl;
        }
    }
    return 0;
}
