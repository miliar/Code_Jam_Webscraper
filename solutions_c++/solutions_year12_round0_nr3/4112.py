/***********************************************
* Author - LUONG VAN DO                        *
* Problem bb
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
int64 Ans;
string X, Y;
void check(int n) {
    string x = "", y, temp;
    while ( n ) {
        x = char(n % 10 + 48) + x;
        n/=10;
    }
    y = x;
    while ( true ) {
        temp = x;
        temp = x[x.size()-1] + temp;
        temp.replace(temp.size()-1,1,"");
        if (temp == y) break;
        x = temp;
        if (temp > y && temp>=X && temp<=Y) Ans++;
    }
}
string get(int a) {
    string x = "";
    while ( a ) {
        x = char(a % 10 + 48) + x;
        a/=10;
    }
    return x;
}
int main(){
    /*#ifndef ONLINE_JUDGE
    FileIn("exam"); FileOut("exam");
    #endif*/
    int cases, caseno = 0;
    int A, B;
    scanf("%d",&cases);
    while (cases--) {
        scanf("%d %d",&A,&B);
        X = get(A); Y = get(B);
        Ans = 0;
        for (int n=A;n<=B;n++)
            check(n);
        printf("Case #%d: %lld\n",++caseno, Ans);
    }
}
