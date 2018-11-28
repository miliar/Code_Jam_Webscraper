#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>

using namespace std;

typedef long long ll;

int R, C, D;
int a[1001][1001];
int mi[505][505], ma[505][505];
ll sum[505][505];

void prepare() {
    memset(sum, 0, sizeof sum);
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            sum[i+1][j+1] = sum[i+1][j] + sum[i][j+1] - sum[i][j] + a[i][j];
        }
    }
}

int getSum(int x1, int y1, int x2, int y2) {
    ++x1;
    ++x2;
    ++y1;
    ++y2;
    return sum[x2][y2] - sum[x2][y1-1] - sum[x1-1][y2] + sum[x1-1][y1-1];
}

double xsum[505][505], ysum[505][505];
/*
bool good(int sz) {
    for (int i = 0; i <= R - sz; ++i) {
        int z = sz / 2;
        double first = -z;
        if (sz % 2 == 0) {
            first += 0.5;
        }
        double mfirst = first;
        double lst;
        double csum = 0;
        for (int j = 0; j < sz; ++j) {
            if (j == 0 || j == sz-1) {
                cerr << getSum(i + 1, j, i + sz - 2, j) << endl;
                csum += first * getSum(i + 1, j, i + sz - 2, j);
                lst = first;
                first += 1;
            } else {
                csum += first * getSum(i, j, i + sz - 1, j);
                lst = first;
                first += 1;
            }
        }
        xsum[i][0] = csum;
        for (int f = 0, j = sz; j < C; ++f, ++j) {
            csum -=  mfirst * getSum(i + 1, f, i + sz - 2, f);
            csum += lst * getSum(i + 1, j, i + sz - 2, j);
            csum -= getSum(i, f + 1, i + sz - 1, j-1);
            xsum[i][f+1] = csum;
        }        
    }
    
    for (int j = 0; j <= C - sz; ++j) {
        int z = sz / 2;
        double first = -z;
        if (sz % 2 == 0) {
            first += 0.5;
        }
        double mfirst = first;
        double lst;
        double csum = 0;
        for (int i = 0; i < sz; ++i) {
            if (i == 0 || i == sz-1) {
                csum += first * getSum(i, j+1, i, j + sz - 2);
                lst = first;
                first += 1;
            } else {
                csum += first * getSum(i, j, i, j + sz - 1);
                lst = first;
                first += 1;
            }
        }
        ysum[0][j] = csum;
        for (int f = 0, i = sz; i < R; ++f, ++i) {
            csum -=  mfirst * getSum(f, j + 1, f, j + sz - 2);
            csum += lst * getSum(i, j + 1, i, j + sz - 2);
            csum -= getSum(f + 1, j, i-1, j + sz - 1);
            ysum[f + 1][j] = csum;
        }        
    }
    for (int i = 0; i <= R - sz; ++i) {
        for (int j = 0; j <= C - sz; ++j) {
            if (abs(xsum[i][j] + ysum[i][j]) < 1e-8) {
                return true;
            }
        }
    }
    return false;
}
*/
const double eps = 1e-8;

bool good(int sz) {
    for (int i = 0; i <= R - sz; ++i) {
        
        
        for (int j = 0; j <= R - sz; ++j) {
            double csumx = 0;
            double csumy = 0;
            int z = sz / 2;
        double first = -z;
        if (sz % 2 == 0) {
            first += 0.5;
        }
            for (int k = 0; k < sz; ++k) {
                    if (k == 0 || k == sz-1) {
                        csumx += first * getSum(i + 1, j + k, i + sz - 2, j + k);
                       
                        csumy += first * getSum(i + k, j + 1, i + k, j + sz - 2);
                        first += 1;
                } else {
                       csumx += first * getSum(i, j + k, i + sz - 1, j + k);
                       csumy += first * getSum(i + k, j, i + k, j + sz - 1);
                       
                       first += 1;
                   }
            }
            
            if (fabs(csumx) < eps && fabs(csumy) < eps) {
                return true;
            }
        }
    }
    return false;
}


void solve() {
    scanf("%d%d%d", &R, &C, &D);
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            char c;
            cin >> c;
            a[i][j] = c - '0';
            //a[i][j] += D;
         }
       // cerr << endl;
    }
    prepare();
    for (int K = min(R, C); K >= 3; --K) {
        if (good(K)) {
            printf("%d\n", K);
            return;
        }
    }
    printf("IMPOSSIBLE\n");
}

int T;
    
int main(int argc, char** argv) {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}


