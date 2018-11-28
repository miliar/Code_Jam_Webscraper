#include <stdio.h>
#include <iostream>

using namespace std;

int n, a[105][105], ntest, k, nnw[105], nnc[105];
double wp[105], owp[105], oowp[105];

int exchange(char ch) {
    if (ch == '.') return 0;
    if (ch == '0') return -1;
    if (ch == '1') return 1;    
}

void process1(int k) {
    for (int i = 1; i <= n; i++) {
        int nw = 0, nc = 0;
        for (int j = 1; j <= n; j++) {
            if (a[i][j] != 0) nc++;
            if (a[i][j] == 1) nw++;
        }
        nnw[i] = nw;
        nnc[i] = nc;
        wp[i] = nw* 1.0 / nc;
    }    
    
    for (int i = 1; i <= n; i++) {
        double res = 0;
        int nc = 0, k = 0;
        for (int j = 1; j <= n; j++) {
            if (a[i][j] != 0) {
                nc++;
                if (a[j][i] == 1) k = 1; else k = 0;
                if (a[j][i] != 0) {
                    res += (nnw[j] - k) * 1.0 / (nnc[j] - 1);
                }
            }
        }
        owp[i] = res / nc;
    }      
      
    for (int i = 1; i <= n; i++) {
        double res = 0;
        int nc = 0;
        for (int j = 1; j <= n; j++) {
            if (a[i][j] != 0) {
                nc ++;
                res += owp[j];
            }
        }
        oowp[i] = res / nc;
    }          
    for (int i = 1; i <= n; i++) printf("%.9lf\n",0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
}

int main () {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> ntest;
    for (k = 1; k <= ntest; k++) {
        cin >> n;
        string s;        
        cout << "Case #" << k << ":" << endl;                    
        for (int i = 1; i <= n; i++) {
            cin >> s;
            for (int j = 1; j <= n; j++) {
                a[i][j] = exchange(s[j - 1]);   
            }
        }   
        process1(k);            
    }
    return 0;   
}
