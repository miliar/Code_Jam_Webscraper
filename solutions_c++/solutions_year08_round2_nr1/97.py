#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int _a;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;


int main() {
    int tests;
    cin >> tests;
    FOT(_t, 1, tests+1) {
        ll n, A, B, C, D, x0, y0, M;
        cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
        int num[3][3];
        FOR(i, 3) FOR(j, 3) num[i][j] = 0;
        ll X, Y;
        X = x0;
        Y = y0;
        FOR(i, n) {
            num[X%3][Y%3]++;
            X = (A * X + B) % M;
            Y = (C * Y + D) % M;
        }
        ll ans = 0;
        for(int a = 0; a < 9; a++) {
            for(int b = a; b < 9; b++) {
                for(int c = b; c < 9; c++) {
                    int xt, yt;
                    xt = yt = 0;
                    int ax = a/3, bx = b/3, cx = c/3;
                    int ay = a%3, by = b%3, cy = c%3;

                    xt = (ax + bx + cx) % 3;
                    yt = (ay + by + cy) % 3;

                    if(xt || yt) continue;
                    if (a == b) {
                        if (b == c) {
                            ans += ll(num[ax][ay]) * ll(num[ax][ay] - 1) * ll(num[ax][ay] - 2) / 6;
                        }
                        else {
                            ans += ll(num[ax][ay]) * ll(num[ax][ay] - 1) / 2 * ll(num[cx][cy]);
                        }
                    }
                    else {
                        if(b == c) {
                            ans += ll(num[ax][ay]) * ll(num[bx][by]) * ll(num[bx][by] - 1) / 2;
                        }
                        else {
                            ans += ll(num[ax][ay]) * ll(num[bx][by]) * ll(num[cx][cy]);
                        }
                    }
                }
            }
        }
        cout << "Case #" << _t << ": " << ans << endl;
    }
    return 0;
}





