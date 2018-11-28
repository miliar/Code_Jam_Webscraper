#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <sstream>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <list>
using namespace std;
typedef long long int64;
#define showbit(a, b) (((a) >> (b)) & 1)
#define move(n) ((1) << (n))
#define sz(x) (int)x.size()
#define maxint 0x7fffffff
#define maxint64 0x7fffffffffffffffLL
#define sqr(x) ((x) * (x))
const double pi = acos(-1.0);
const double eps = 1e-8;
int sgn(double x) { return (x > eps) - (x < -eps); }
char str[55][55], rot[55][55];
int n, k;
void rotate() {
    memset(rot, '.', sizeof(rot));
    for(int r = n - 1; r >= 0; r--) {
        int rr = n - 1;
        for(int c = n - 1; c >= 0; c--) if(str[r][c] != '.') {
            rot[rr--][n - r - 1] = str[r][c];
        }
    }
    /*for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) cout << rot[i][j];
        cout << endl;
    }*/
}
bool judge(char c) {
    for(int i = 0; i < n; i++) {
        int tot = 0;
        for(int j = 0; j < n; j++) {
            if(rot[i][j] == c) {
                tot++;
                if(tot == k) return true;
            } else {
                tot = 0;
            }
        }
    }
    for(int j = 0; j < n; j++) {
        int tot = 0;
        for(int i = 0; i < n; i++) {
            if(rot[i][j] == c) {
                tot++;
                if(tot == k) return true;
            } else {
                tot = 0;
            }
        }
    }
    for(int j = 0; j < 2 * n - 1; j++) {
        int row, col;
        if(j < n) {
            row = 0;
            col = j;
        } else {
            row = n - j + 1;
            col = n - 1;
        }
        int tot = 0;
        while(row < n && col >= 0) {
            if(rot[row][col] == c) {
                tot++;
                if(tot == k) return true;
            } else {
                tot = 0;
            } 
            row++;
            col--;
        }
    }
    for(int j = n - 1; j >= -(n - 1); j--) {
        int row, col;
        if(j >= 0) {
            row = 0;
            col = j;
        } else {
            row = -j;
            col = 0;
        }
        int tot = 0;
        while(row < n && col < n) {
            if(rot[row][col] == c) {
                tot++;
                if(tot == k) return true;
            } else {
                tot = 0;
            }
            row++;
            col++;
        }
    }
    return false;
}
int main() {
    int t;
    int Case = 1;
    cin >> t;
    while(t--) {
        cin >> n >> k;
        for(int i = 0; i < n; i++) cin >> str[i];
        rotate();
        bool flagred = judge('R');
        bool flagblue = judge('B');
        if(!flagred && !flagblue) {
            printf("Case #%d: Neither\n", Case++);
        } else if(flagred && flagblue) {
            printf("Case #%d: Both\n", Case++);
        } else if(flagred) {
            printf("Case #%d: Red\n", Case++);
        } else {
            printf("Case #%d: Blue\n", Case++);
        }
    }
    return 0;
}
        
