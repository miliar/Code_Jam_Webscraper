/***********************************************
* Author - LUONG VAN DO                        *
* Problem 
* Algorithm
* Time Limit
* *********************************************/
#include <iostream>
#include <stdio.h>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <math.h>
#include <cstring>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

#define FileIn(file) freopen(file".inp", "r", stdin)
#define FileOut(file) freopen(file".out", "w", stdout)
#define fr(i,a,b) for (int i=a;i<=b;i++)
#define FORD(i,a,b) for (int i=a;i>=b;i--)
#define rep(i, n) for (int i=0; i<n; i++)
#define repr(i, n) for (int i = n - 1;i >= 0;i--)
#define fill(ar, val) memset(ar, val, sizeof(ar))
#define pb push_back
#define ff first
#define ss second
#define PI 3.1415926535897932385
#define uint64 unsigned long long
#define int64 long long
#define INF 500000000
#define N 100111

using namespace std;

inline int max(int a, int b) { return a > b ? a : b; }
inline int min(int a, int b) { return a < b ? a : b; }
inline int gcd(int a, int b) { if (a % b) return gcd(b, a % b); else return b; }
inline int lcm(int a, int b) { return (a * (b / gcd(a, b) )); }

inline int And(int mask, int bit) { return mask & (1 << bit); }
inline int Or(int mask, int bit) { return mask | (1 << bit); }
inline int Xor(int mask, int bit) { return mask & (~(1 << bit)); }

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
char s[5][5], ss[N];
bool X, O;
bool checkRow(int pos, char c) {
    int t = 0, x = 0;
    for (int i = 0;i < 4;i++)
        if (s[pos][i] == c) x++;
        else 
        if (s[pos][i] == 'T') t++;
    if (x == 3 && t == 1) return true;
    if (x == 4) return true;
    return false;
}
bool checkCol(int pos, char c) {
    int t = 0, x = 0;
    for (int i = 0;i < 4;i++)
        if (s[i][pos] == c) x++;
        else
        if (s[i][pos] == 'T') t++;
    if (x == 3 && t == 1) return true;
    if (x == 4) return true;
    return false;
}
bool checkDig(char c) {
    int t = 0, x = 0;
    for (int i = 0;i < 4;i++)
        if (s[i][i] == c) x++;
        else 
        if (s[i][i] == 'T') t++;
    if (x == 3 && t == 1) return true;
    if (x == 4) return true;
    t = 0; x = 0;
    for (int i = 0;i < 4;i++)
        if (s[i][4 - i - 1] == c) x++;
        else 
        if (s[i][4 - i - 1] == 'T') t++;
    if (x == 3 && t == 1) return true;
    if (x == 4) return true;
    return false;
}
int main() {
	freopen("exam.inp","r", stdin); freopen("exam.out","w", stdout);
	int cases, caseno = 0;
	scanf(" %d ", &cases);
	while (cases--) {
	    rep(i, 4) gets(s[i]);
	    gets(ss);
	    printf("Case #%d: ", ++caseno);
	    X = O = false;
	    rep(i, 4)
            if ( checkRow(i, 'X') ) X = true;
	    rep(i, 4)
            if ( checkCol(i, 'X') ) X = true;
        if (checkDig('X')) X = true;
        if (X) {
            puts("X won");
            continue;
        }
        rep(i, 4)
            if ( checkRow(i, 'O') ) O = true;
	    rep(i, 4)
            if ( checkCol(i, 'O') ) O = true;
        if (checkDig('O')) O = true;
        if (O) {
            puts("O won");
            continue;
        }
        int cnt = 0;
        rep(i, 4)
            rep(j, 4)
                if (s[i][j] != '.') cnt++;
        if (cnt != 16) puts("Game has not completed");
        else puts("Draw");
        
	}
	return 0;
}
