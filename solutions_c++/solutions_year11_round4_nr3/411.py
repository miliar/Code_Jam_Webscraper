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

typedef pair<int, int> PII;
typedef vector<int> VI;

bool nt[1000006];
long long n;
int ntest, res;

void init() {
    FOR(i, 2, 1000000) {
        nt[i] = true;
        FOR(j, 2, int(sqrt(i))) {
            if (i % j == 0) {
                nt[i] = false;
                break;
            }   
        }   
    }    
}

int xd(int x) {
    long long y = x;
    int num = 0;
    while (y <= n) {
        num ++;
        y = y * x;    
    }  
    return num - 1;
}

int main () {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    cin >> ntest;
    init();
    FR(test, ntest) {
        cin >> n;
        res = 1;
        FOR(i, 2, int(sqrt(n))) {
            if (nt[i]) {
                res += xd(i);   
            }    
        }   
        if (n == 1) res = 0;
        printf("Case #%d: %d\n", test + 1, res);        
    }
    
    return 0;   
}
