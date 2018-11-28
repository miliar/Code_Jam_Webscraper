#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

const int maxn = 110;

int n;
int d[maxn][maxn];
char tmp[maxn];
int win[maxn], sum[maxn];

double wp[maxn], owp[maxn], oowp[maxn];

void work() {
    scanf("%d", &n);
    memset(win, 0, sizeof(win));
    memset(sum, 0, sizeof(sum));
    memset(d, 0, sizeof(d));
    for(int i=0; i<n; ++i) {
        scanf("%s", tmp);
        for(int j=0; j<n; ++j) {
            if(tmp[j] == '1') {
                d[i][j] = 2;
                ++ win[i];
                ++ sum[i];
            } else if(tmp[j] == '0') {
                d[i][j] = 1;
                ++ sum[i];
            }
        }
    }
    for(int i=0; i<n; ++i) {
        wp[i] = (double)win[i] / (double)sum[i];
    }
    for(int i=0; i<n; ++i) {
        double s = 0;
        int cnt = 0;
        for(int j=0; j<n; ++j) {
            if(j == i) continue;
            if(d[i][j] == 0) continue;
            int u = win[j];
            if(d[i][j] == 1) --u;
            int v = sum[j] - 1;
            s += (double)u / (double)v;
            ++ cnt;
        }
        owp[i] = s / cnt;
    }
    for(int i=0; i<n; ++i) {
        double s = 0;
        int cnt = 0;
        for(int j=0; j<n; ++j) {
            if(j == i) continue;
            if(d[i][j] == 0) continue;
            s += owp[j];
            ++ cnt;
        }
        oowp[i] = s / cnt;
    }
    for(int i=0; i<n; ++i) {
        printf("%.10f\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for(int i=0; i<T; ++i) {
        printf("Case #%d:\n", i+1);
        work();
    }
}
