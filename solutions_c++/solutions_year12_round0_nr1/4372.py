/***********************************************
* Author - LUONG VAN DO                        *
* Problem aa
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
#define FOR(i,a,b) for (int i=a;i<=b;i++)
#define FORD(i,a,b) for (int i=a;i>=b;i--)
#define REP(i, n) for (int i=0; i<n; i++)
#define pb push_back
#define A first
#define B second
#define PI 3.1415926535897932385
#define uint64 unsigned long long
#define int64 long long
#define INF 500000000
#define M 100000

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
map <char, char> f;
void init() {
//    abcdefghijklmnopqrstuvwxyz
    f['a'] = 'y'; f['p'] = 'r';
    f['b'] = 'h'; f['q'] = 'z';
    f['c'] = 'e'; f['r'] = 't';
    f['d'] = 's'; f['s'] = 'n';
    f['e'] = 'o'; f['t'] = 'w';
    
    f['f'] = 'c'; f['u'] = 'j';
    f['g'] = 'v'; f['v'] = 'p';
    f['h'] = 'x'; f['w'] = 'f';
    f['i'] = 'd'; f['x'] = 'm';
    f['j'] = 'u'; f['y'] = 'a';
    
    f['k'] = 'i'; f['z'] = 'q';
    f['l'] = 'g';
    f['m'] = 'l';
    f['n'] = 'b';
    f['o'] = 'k';
    
}
int main(){
    /*#ifndef ONLINE_JUDGE
    FileIn("exam"); FileOut("exam");
    #endif*/
    init();
    int cases, caseno = 0;
    char s[M];
    scanf(" %d ",&cases);
    while ( cases--) {
        gets(s);
        printf("Case #%d: ",++caseno);
        for (int i=0;i<strlen(s);i++)
            if (s[i]==' ') putchar(s[i]);
            else putchar(f[s[i]]);
        puts("");
    }
}
