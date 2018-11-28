/* 
 * File:   main.cpp
 * Author: jyd
 *
 * Created on 2011年5月22日, 上午12:00
 */

#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

const int N = 201;
char g[N][N];
double wp[N], owp[N], oowp[N];
int total[N], win[N];
int main(int argc, char** argv) {
freopen("in", "r", stdin);
freopen("out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas ++){
        int n;
        memset(total, 0, sizeof(total));
        memset(win, 0, sizeof(win));
        for(int i = 0; i < N; i ++){
            wp[i] = owp[i] = oowp[i] = 0.0;
        } 
        scanf("%d", &n);
        for(int i = 0; i < n; i ++){
            scanf("%s", g + i);
            for(int j = 0; j < n; j ++){
                if(g[i][j] != '.'){
                    total[i] ++;
                    if(g[i][j] == '1') win[i]++;
                }
            }
            wp[i] = win[i] * 1.0 / total[i];
        }
        for(int i = 0; i < n; i ++){
            for(int j = 0; j < n; j ++){
                if(g[i][j] != '.'){
                    if(g[i][j] == '0'){
                        owp[i] += (win[j] - 1)*1.0/(total[j] - 1);
                    }
                    else{
                        owp[i] += win[j]*1.0 / (total[j] - 1);
                    }
                }
            }
            owp[i] /= total[i];
        }
        for(int i = 0; i < n; i ++){
            for(int j = 0; j < n; j ++){
                if(g[i][j] != '.'){
                    oowp[i] += owp[j];
                }
            }
            oowp[i] /= total[i];
        }
        printf("Case #%d:\n", cas);
        for(int i = 0; i  < n; i ++){
            double ans = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
            printf("%.8lf\n", ans);
        }
    }
    return 0;
}

