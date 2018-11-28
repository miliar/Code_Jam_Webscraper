#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

using namespace std;

int main () {
    int t, c;
    scanf("%d", &t);
    c = 1;
    while(t--) {
        printf("Case #%d:\n", c);
        c++;
        int n;
        scanf("%d", &n);
        double wp [n], owp[n], oowp[n];
        char tab [n][n];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> tab[i][j];   
            }
        }
        int op [n][n];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                op[i][j] = 0;  
            }   
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if  (tab[i][j] != '.')
                op[i][j] = 1;  
            }   
        }
        for (int k = 0; k < n; ++k) {
            int opk = 0;
            long double cuma = 0;
            for (int i = 0; i < n; ++i) {
            int conty = 0;
            int conty2 = 0;
            if (op[k][i]) {
            opk++;
            for (int j = 0; j < n;++j) {
                if (j != k){
                if (tab[i][j] == '1'){
                ++conty;   
                ++conty2;
                }
                else if (tab[i][j] == '0') {
                    ++conty2;   
                }}
            }
            cuma += (long double)conty/(long double)conty2;   }
        }          
        owp[k] = cuma/(long double)(opk);   
        }
        for (int i = 0; i < n; ++i) {
            long double cuma = 0;
            int opi = 0;
            for (int j = 0; j < n; ++j) {
                if (tab[i][j] != '.') {
                    opi++;
                    cuma += owp[j];   
                }
            }
            oowp[i] = cuma/(long double)opi;  
        }
        for (int i = 0; i < n; ++i) {
            int conty = 0;
            int conty2 = 0;
            for (int j = 0; j < n;++j) {
                if (tab[i][j] == '1'){
                ++conty;   
                ++conty2;
                }
                else if (tab[i][j] == '0') {
                    ++conty2;   
                }

            }
            wp[i] = (long double)conty/(long double)conty2;   
        }
        for (int i = 0; i <n; ++i) {
          long double rr = (long double)0.25 * wp[i] + (long double)0.50 * owp[i] + (long double)0.25 * oowp[i];
          printf("%Lf\n", rr);
          }
    }
    return 0;
}
