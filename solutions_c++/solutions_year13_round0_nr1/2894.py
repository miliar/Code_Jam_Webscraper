// INCLUDE LIST
#include <cstdio>
#include <bitset>
#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <vector>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

// DEFINE LIST
#define REP(_I, _J, _K) for(_I = (_J) ; _I < (_K) ; _I++)
#define input(_A)       freopen(_A, "r", stdin);
#define output(_A)      freopen(_A, "w", stdout);
#define INPUT           input("in.txt");
#define OUTPUT          output("out.txt");
#define hold            {fflush(stdin); getchar();}
#define reset(_A, _B)   memset((_A), (_B), sizeof (_A));
#define debug           printf("<<TEST>>\n");
#define eps             1e-11
#define f_cmp(_A, _B)   (fabs((_A) - (_B)) < eps)
#define phi             acos(-1)
#define pb              push_back
#define value(_A)       cout << "Variabel -> " << #_A << " -> " << _A << endl;
#define st              first
#define nd              second

// TYPEDEF LIST
typedef pair<int, int>  ii;
typedef vector<int>     vi;
typedef vector<ii>      vii;
typedef long long       LL;

// VAR LIST
int MAX =               1000000;
int MIN =               -1000000;
int INF =               1000000000;
int x4[4] =             {0, 1, 0, -1};
int y4[4] =             {1, 0, -1, 0};
int x8[8] =             {0, 1, 1,  1,  0, -1, -1, -1};
int y8[8] =             {1, 1, 0, -1, -1, -1,  0,  1};
int i, j, k;

// MAIN CODE
int main () {
    input("A-large.in");
    OUTPUT;
    int t, x, o, T, kasus = 0;
    string str[10];
    cin >> t;
    while (t--) {
        bool x_win = false, o_win = false, belum = false;
        REP(i, 0, 4) cin >> str[i];
        // CEK MENANG DULU
        REP(i, 0, 4) {
            x = o = T = 0;
            REP(j, 0, 4) {
                if (str[i][j] == 'X') x++;
                if (str[i][j] == 'O') o++;
                if (str[i][j] == 'T') T++;
            }
            if (x == 4 || (x == 3 && T == 1)) x_win = true;
            if (o == 4 || (o == 3 && T == 1)) o_win = true;
        }
        
        REP(i, 0, 4) {
            x = o = T = 0;
            REP(j, 0, 4) {
                if (str[j][i] == 'X') x++;
                if (str[j][i] == 'O') o++;
                if (str[j][i] == 'T') T++;
            }
            if (x == 4 || (x == 3 && T == 1)) x_win = true;
            if (o == 4 || (o == 3 && T == 1)) o_win = true;
        }
        
        //REP(i, 0, 4) {
            x = o = T = 0;
            REP(j, 0, 4) {
                if (str[j][j] == 'X') x++;
                if (str[j][j] == 'O') o++;
                if (str[j][j] == 'T') T++;
            }
            if (x == 4 || (x == 3 && T == 1)) x_win = true;
            if (o == 4 || (o == 3 && T == 1)) o_win = true;
        //}
        
            x = o = T = 0;
            REP(j, 0, 4) {
                if (str[3 - j][j] == 'X') x++;
                if (str[3 - j][j] == 'O') o++;
                if (str[3 - j][j] == 'T') T++;
            }
            if (x == 4 || (x == 3 && T == 1)) x_win = true;
            if (o == 4 || (o == 3 && T == 1)) o_win = true;
            
        // CEK UDAH LENGKAP BELUM
        REP(i, 0, 4) {
            REP(j, 0, 4) {
                if (str[i][j] == '.') belum = true;
            }
        }
        cout << "Case #" << ++kasus << ": ";
        if (x_win) cout << "X won" << endl;
        else if (o_win) cout << "O won" << endl;
        else if (belum) cout << "Game has not completed" << endl;
        else cout << "Draw" << endl;
    }
    return 0;
}

// VINCENTIUS MADYA
// DARKSTALKER
// LANGUAGE : C++
