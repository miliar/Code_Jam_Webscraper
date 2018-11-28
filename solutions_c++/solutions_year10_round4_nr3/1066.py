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
bool d[110][110];
bool del() {
    /*for(int i = 1; i <= 5; i++) {
            for(int j = 1; j <= 5; j++) printf("%d", d[i][j]);
            printf("\n");
        }*/
    bool flag = false;
    for(int i = 100; i >= 1; i--) {
        for(int j = 100; j >= 1; j--) {
            if(d[i][j]) {
                flag = true;
                if(!d[i - 1][j] && !d[i][j - 1]) {
                    d[i][j] = 0;
                }
            } else {
                if(d[i - 1][j] && d[i][j - 1]) {
                    d[i][j] = 1;
                    flag = true;
                }
            }
        }
    }
    return flag;
}
int main() {
    int t;
    cin >> t;
    for(int Case = 1; Case <= t; Case++) {
        int m;
        cin >> m;
        memset(d, 0, sizeof(d));
        while(m--) {
            int c1, r1, c2, r2;
            cin >> c1 >> r1 >> c2 >> r2;
            for(int i = r1; i <= r2; i++) {
                for(int j = c1; j <= c2; j++) {
                    d[i][j] = 1;
                }
            }
        }
        /*for(int i = 1; i <= 5; i++) {
            for(int j = 1; j <= 5; j++) printf("%d", d[i][j]);
            printf("\n");
        }*/
        int res = 0;
        while(del()) {
            res++;
        }
        printf("Case #%d: %d\n", Case, res);
    }
    return 0;
}

