/*
 * Author: NomadThanatos
 * Created Time:  2011/5/22 0:07:15
 * File Name: A.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())

const int MAXINT = -1u>>1;
const int MAXN = 100 + 10;
const double EPS = 1e-9;

template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

char gra[MAXN][MAXN];
double WP[MAXN],OWP[MAXN],OOWP[MAXN],RPI[MAXN];
double win[MAXN],total[MAXN];

int sgn(const double &x) {return (int)((x > EPS) - (x < -EPS));}

int main() {
    freopen("A.out","w",stdout);
    
    int T;
    scanf("%d",&T);
    for(int t = 0 ; t < T ; t++) {
        int N;
        scanf("%d",&N);
        for(int i = 0 ; i < N ; i++) {
            scanf("%s",gra[i]);
        }
        memset(WP,0,sizeof(WP));
        memset(OWP,0,sizeof(OWP));
        memset(OOWP,0,sizeof(OOWP));
        memset(win,0,sizeof(win));
        memset(total,0,sizeof(total));
        for(int i = 0 ; i < N ; i++) {
            for(int j = 0 ; j < N ; j++) {
                if (gra[i][j] == '1') {
                    win[i] += 1.0;
                    total[i] += 1.0;
                }
                if (gra[i][j] == '0') {
                    total[i] += 1.0;
                }
            }
            if (sgn(total[i]) == 0) continue;
            WP[i] = win[i] / total[i];
        }
        for(int i = 0 ; i < N ; i++) {
            double cnt = 0.0;
            for(int j = 0 ; j < N ; j++) {
                if (gra[i][j] == '0') {
                    if ((total[j] - 1.0) == 0) continue;
                    OWP[i] += (win[j] - 1.0) / (total[j] - 1.0);
                    cnt += 1.0;
                }
                if (gra[i][j] == '1') {
                    if ((total[j] - 1.0) == 0) continue;
                    OWP[i] += (win[j]) / (total[j] - 1.0);
                    cnt += 1.0;
                }
            }
            if (sgn(cnt) == 0) continue;
            OWP[i] /= cnt;
        }
        for(int i = 0 ; i < N ; i++) {
            double res = 0.0,cnt = 0.0;
            for(int j = 0 ; j < N ; j++) {
                if (gra[i][j] != '.') {
                    res += OWP[j];
                    cnt += 1.0;
                }
            }
            if (sgn(cnt) == 0) continue;
            OOWP[i] = res / cnt;
        }
        for(int i = 0 ; i < N ; i++) {
            RPI[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
        }
        //printf("%lf\n%lf\n%lf\n",WP[0],OWP[0],OOWP[0]);
        printf("Case #%d:\n",t + 1);
        for(int i = 0 ; i < N ; i++) {
            printf("%0.12lf\n",RPI[i]);
        }
    }
    return 0;
}

