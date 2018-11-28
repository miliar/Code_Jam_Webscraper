#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>

using namespace std;

typedef pair<int, int> pi;
typedef unsigned long long ull;

#define x first
#define y second
#define mp make_pair


void solution(int tstNum) {
    int n;
    scanf("%d\n", &n);
    
    vector<double> wp(n), owp(n), oowp(n);
    vector<int> cnts(n);

    char tabl[101][101] = {0};
    for (int i = 0; i < n; i++) {
        gets(tabl[i]);
        for (int j = 0; j < n; ++j) {
            if (j > i) {
                if (tabl[i][j] == '0') {
                    wp[j] += 1;
                }
                if (tabl[i][j] == '1') {
                    wp[i] += 1;
                }
            }
        }
    }
    for (int i = 0; i < n; ++i) {
        int cnt = 0;
        for (int j = 0; j < n; ++j) {
            if (tabl[i][j] != '.') {
                ++cnt;
            }
        }        
        wp[i] /= cnt;
        cnts[i] = cnt;
    }
    for (int i = 0; i < n; ++i) {
        double tot = 0;
        int cnt = 0;
        for (int j = 0; j < n; ++j) {
            if (tabl[i][j] != '.') {                
                ++cnt;
                if (tabl[i][j] == '0') {
                    tot += (wp[j] * cnts[j] - 1) / (cnts[j] - 1);
                } else {
                    tot += (wp[j] * cnts[j]) / (cnts[j] - 1);
                }
            }
        }
        tot /= cnt;
        owp[i] = tot;
    }
    for (int i = 0; i < n; ++i) {
        double tot = 0;
        int cnt = 0;
        for (int j = 0; j < n; ++j) {
            if (tabl[i][j] != '.') {
                tot += owp[j];
                ++cnt;
            }
        }
        tot /= cnt;
        oowp[i] = tot;
    }
    for (int i = 0; i < n; ++i) {
        double res;
        res = wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25;
        printf("%.8lf\n", res);
    }
}

int main() {

//    freopen("in.in", "rt", stdin);
    //freopen("out.out", "wt", stdout);

    //freopen("A-small.in", "rt", stdin);
    //freopen("A-small.out", "wt", stdout);

    freopen("A-large.in", "rt", stdin);
    freopen("A-large.out", "wt", stdout);

    int t = 0;
    scanf("%d\n", &t);
    for (int tt = 0; tt < t; tt++) {
        printf("Case #%d:\n", tt + 1);
        solution(tt);
    }

    return 0;
}