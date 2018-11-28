#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <map>
using namespace std;

int T, N;
char op[100][101];
double wp[100], owp[100], oowp[100], rpi[100];

double get_owp(int k)
{
    double p[100];
    memset(p, 0, sizeof(p));
    for(int i = 0; i < N; i++){
        int c = 0;
        for(int j = 0; j < N; j++){
            if(j != k && op[i][j] != '.'){
                p[i] += (op[i][j] == '1');
                c++;
            }
        }
        if(c>0) p[i] /= c;
        else p[i] = 0;
    }
    double pp = 0;
    int c = 0;
    for(int i = 0; i < N; i++)
        if(i != k && op[k][i] != '.')
            pp += p[i], c++;
    return c>0 ? pp/c : 0;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++){
        scanf("%d", &N);
        for(int i = 0; i < N; i++){
            scanf("%s", op[i]);
        }
        memset(wp, 0, sizeof(wp));
        memset(owp, 0, sizeof(owp));
        memset(oowp, 0, sizeof(oowp));
        memset(rpi, 0, sizeof(rpi));
        
        for(int i = 0; i < N; i++){
            int c = 0;
            for(int j = 0; j < N; j++){
                if(op[i][j] != '.'){
                    wp[i] += (op[i][j]=='1');
                    c++;
                }
            }
            wp[i] = c>0? wp[i]/c : 0;
        }
        for(int i = 0; i < N; i++){
            owp[i] = get_owp(i);
        }
        for(int i = 0; i < N; i++){
            int c = 0;
            for(int j = 0; j < N; j++){
                if(i != j && op[i][j] != '.'){
                    oowp[i] += owp[j];
                    c++;
                }
            }
            oowp[i] = c>0 ? oowp[i]/c : 0;
        }
        for(int i = 0; i < N; i++)
            rpi[i] = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
        printf("Case #%d:\n", cas);
        for(int i = 0; i < N; i++)
            printf("%.8lf\n", rpi[i]);
    }
    
    return 0;
}
