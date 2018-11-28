#include <iostream>
#include <sstream>

#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <string>

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>

#include <algorithm>
#include <numeric>

#define foreach(i, x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)
#define sqr(x) ((x) * (x))
#define len(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define pbk pop_back
#define mp make_pair
#define fs first
#define sc second
#define endl '\n'
#ifdef CUTEBMAING
#include "cutedebug.h"
#else
#define debug(x) ({})
#endif

using namespace std;

typedef long long int64;
typedef unsigned long long lint;
typedef long double ld;

const int inf = ((1 << 30) - 1);
const int64 linf = ((1ll << 62) - 1);

const char* fin = "input.txt";
const char* fout = "output.txt";

string s[4];

void run(){
    for (int i = 0; i < 4; i++)
        cin >> s[i];
    for (int i = 0; i < 4; i++){
        bool aWin = true, bWin = true;
        for (int j = 0; j < 4; j++){
            if (s[i][j] == '.')
                aWin = bWin = false;
            if (s[i][j] == 'X')
                bWin = false;
            if (s[i][j] == 'O')
                aWin = false;
        }
        if (aWin)
            return void (puts("X won"));
        if (bWin)
            return void (puts("O won"));
    }
    for (int j = 0; j < 4; j++){
        bool aWin = true, bWin = true;
        for (int i = 0; i < 4; i++){
            if (s[i][j] == '.')
                aWin = bWin = false;
            if (s[i][j] == 'X')
                bWin = false;
            if (s[i][j] == 'O')
                aWin = false;
        }
        if (aWin)
            return void (puts("X won"));
        if (bWin)
            return void (puts("O won"));
    }
    {
        bool aWin = true, bWin = true;
        for (int j = 0; j < 4; j++){
            if (s[j][j] == '.')
                aWin = bWin = false;
            if (s[j][j] == 'X')
                bWin = false;
            if (s[j][j] == 'O')
                aWin = false;
        }
        if (aWin)
            return void (puts("X won"));
        if (bWin)
            return void (puts("O won"));
    }
    {
        bool aWin = true, bWin = true;
        for (int j = 0; j < 4; j++){
            if (s[j][4 - j - 1] == '.')
                aWin = bWin = false;
            if (s[j][4 - j - 1] == 'X')
                bWin = false;
            if (s[j][4 - j - 1] == 'O')
                aWin = false;
        }
        if (aWin)
            return void (puts("X won"));
        if (bWin)
            return void (puts("O won"));
    }
    bool empty = false;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (s[i][j] == '.')
                empty = true;
    puts(empty ? "Game has not completed" : "Draw");
}

int main(){
    #if !defined STRESS && defined CUTEBMAING
    assert(freopen(fin, "r", stdin));
    assert(freopen(fout, "w", stdout));
    #endif
    int t; cin >> t;
    for (int i = 0; i < t; i++){
        double begin = clock();
        printf("Case #%d: ", i + 1);
        cerr << "Solving case " << i << endl;
        run();
        cerr << "Case " << i << " OK" << endl;
        cerr << "Time elapsed: " << fixed << (clock() - begin) / CLOCKS_PER_SEC << endl;
    }
    return 0;
}
