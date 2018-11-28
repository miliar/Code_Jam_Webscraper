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
int a[10], smin[10];
int main(){
    /*#ifndef ONLINE_JUDGE
    FileIn("exam"); FileOut("exam");
    #endif*/
    int cases, caseno = 0;
    int n, s, p, Ans;
    scanf("%d",&cases);
    while (cases--) {
        scanf("%d %d %d",&n,&s,&p);
        for (int i=0;i<n;i++) scanf("%d",&a[i]);
        sort(a, a + n);
        Ans = 0;
        do{
            int y, z, cnt, d, xmin, xmax;
            cnt = d = 0;
            for (int i=0;i<n;i++)
                smin[i] = a[i] / 3;
            for (int i=0;i<n;i++) {
                int temp = a[i] - smin[i];
                int x = temp / 2;
                if (cnt < s) {
                    y = x - 1;
                    z = x + 1;
                }
                else {
                    y = x;
                    z = a[i] - (smin[i] + y);
                }
                xmin = min(smin[i], min(y, z));
                xmax = max(smin[i], max(y, z));
                if (xmax >= 0 && xmin>=0 && xmax >= p) d++;
                if (xmax>=0 && xmin>=0 && xmax - xmin == 2) cnt++;
            }
            if (cnt == s) Ans = max(Ans, d);
        }while (next_permutation(a, a + n));
        printf("Case #%d: %d\n",++caseno, Ans);
    }
}
