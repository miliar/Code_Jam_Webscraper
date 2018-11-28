#define maxn 150
#include <iostream>
#include <stdio.h>
using namespace std;

char str[maxn][maxn];
double wp[maxn], owp[maxn], oowp[maxn];
int cnt[maxn], win[maxn], n;

void init(){
    scanf("%d", &n);
    for (int i=0; i<n; i++) scanf("%s", str[i]);
}

void getwp(){
    for (int i=0; i<n; i++){
        cnt[i]=n, win[i]=0;
        for (int j=0; j<n; j++) {
            if (str[i][j]=='.') cnt[i]--;
            if (str[i][j]=='1') win[i]++;
        }
        wp[i] = (double)win[i] / cnt[i];
    }
}

void getowp(){
    for (int i=0; i<n; i++){
        owp[i]=0;
        for (int j=0; j<n; j++){
            if (str[i][j]!='.'){
                if (str[i][j] == '1') owp[i]+=(double)(win[j])/(cnt[j]-1);
                else owp[i]+=(double)(win[j]-1)/(cnt[j]-1);
            }
        }
        owp[i]/=(double)(cnt[i]);
    }
}

void getoowp(){
    for (int i=0; i<n; i++){
        oowp[i]=0;
        for (int j=0; j<n; j++)
            if (str[i][j]!='.') oowp[i]+=owp[j];
        oowp[i]/=(double)(cnt[i]);
    }
}

void getpri(){
    for (int i=0; i<n; i++) {
        double pri=0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
        printf("%.12lf\n", pri);
    }
}

void solve(){
    getwp();
    getowp();
    getoowp();
    getpri();
}

int main(){
    int test; scanf("%d", &test);
    for (int cas=1; cas<=test; cas++){
        init();
        printf("Case #%d:\n", cas);
        solve();
    }
    return 0;
}
