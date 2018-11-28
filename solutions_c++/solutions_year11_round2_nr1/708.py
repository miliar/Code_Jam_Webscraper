/* 
 * File:   main.cpp
 * Author: xhSong
 *
 * Created on 2011年5月21日, 下午9:16
 */

#include <cstdlib>
#include <cstdio>

using namespace std;

char mp[101][101];
int w[101], l[101];
double wp[101], owp[101], oowp[101];

int main(int argc, char** argv) {
    int T;
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        printf("Case #%d:\n", t);
        int n;
        scanf("%d", &n);
        for(int i = 0; i < n; ++i) {
            scanf("%s", mp[i]);
        }
        for(int i = 0; i < n; ++i) {
            w[i] = 0, l[i] = 0;
            for(int j = 0; j < n; ++j) {
                if(mp[i][j] == '1') {
                    ++w[i];
                } else if(mp[i][j] == '0') {
                    ++l[i];
                }
            }
            if(l[i] + w[i] == 0) {
                wp[i] = 0;
            } else {
                wp[i] = w[i] * 1.0 / (w[i] + l[i]);
            }
        }
        
        for(int i = 0; i < n; ++i) {
            int cnto = 0;
            owp[i] = 0;
            for(int j = 0; j < n; ++j) {
                if(mp[i][j] == '1') {
                    owp[i] += w[j] * 1.0 / (w[j] + l[j] - 1);
                    ++cnto;
                } else if(mp[i][j] == '0') {
                    owp[i] += (w[j] - 1) * 1.0 / (w[j] + l[j] - 1);
                    ++cnto;
                }
            }
            if(cnto) {
                owp[i] /= cnto;
            }
        }
        for(int i = 0; i < n; ++i) {
            int cnto = 0;
            oowp[i] = 0;
            for(int j = 0; j < n; ++j) {
                if(mp[i][j] != '.') {
                    ++cnto;
                    oowp[i] += owp[j];
                }
            }
            if(cnto) {
                oowp[i] /= cnto;
            }
        }
        for(int i = 0; i < n; ++i) {
            printf("%.8lf\n", wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25);
        }
    }
    return 0;
}


