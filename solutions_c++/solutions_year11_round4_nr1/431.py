/*
ID: hosyvieta1
PROG: 
LANG: C++
*/

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstring>
//#include <conio.h>

using namespace std;

#define oo 1000000000
#define fi first
#define se second
#define sqr(a) ((a)*(a))
#define FR(i,n) for (int i = 0; i < (n); i++)
#define DN(i,a) for(int i = (a)-1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define esl 0.00000001

typedef pair<int, int> PII;
typedef vector<int> VI;

bool cmp(PII A, PII B) {
    return A.fi < B.fi;    
}

int X, S, R, T, n,
    dodai[500];
    
double t;    
    
PII b[1000005];    

int main () {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> T;
    FR(test, T) {
        memset(dodai, 0, sizeof(dodai));
        cin >> X >> S >> R >> t >> n;
        dodai[S] = X;        
        int maxs = S;
        FR(i, n) {
            int x, y, z;
            cin >> x >> y >> z;
            FOR(j, x, y - 1);
            dodai[S + z] += y - x;
            maxs = max(maxs, S + z);
            dodai[S] -= y - x;
        }
        
        int A = R - S;
        double res = 0;
        
        FOR(i, 1, maxs ) {
            if (dodai[i]) {
                if (t > 0) {
                    if (t * (i + A) >= dodai[i]) {
                        res = res + dodai[i] * 1.0 / (i + A);
                        t = t - dodai[i] * 1.0 / (i + A);
                    } else {
                        res = res + t + (dodai[i] - t * (i + A)) / i; 
                        t = 0;   
                    }
                } else res = res + dodai[i] * 1.0 / i;
            }   
        }
        printf("Case #%d: %.9lf\n", test + 1, res);                
    }
    return 0;   
}
