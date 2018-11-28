#include <iostream>

using namespace std;
typedef unsigned int uint;
int N, M;
string tmap[20];
bool mark[2000][20];
int f[2000][20];
int cnt[2000];
uint _t(uint d, int i){
    return (d >> i) % 2;
}
bool isavail(uint d, int m){
    for(int i = 0; i < N; ++ i)
        if (tmap[m][i] == 'x' && _t(d, i) == 1) return false;
    if (_t(d, 0) == 1 && _t(d, 1) == 1) return false;
    for(int i = 1; i < N; ++ i)
        if (_t(d, i) == 1 && _t(d, i - 1) == 1) return false;
    return true;
}
bool isok(uint dd, uint d, int m){
    if (_t(d, N - 1) == 1 && _t(dd, N - 2) == 1) return false;
    if (_t(d, 0) == 1 && _t(dd, 1) == 1) return false;
    for(int i = 1; i < N - 1; ++ i)
        if (_t(d, i) == 1){
            if (_t(dd, i - 1) == 1) return false;
            if (_t(dd, i + 1) == 1) return false;
        }
    return true;
}
int notepad(uint d, int m){
    if (!mark[d][m]){
        mark[d][m] = true;
        if (!isavail(d, m)) {
            f[d][m] = -1;
            return -1;
        }
        if (m == 0){
            f[d][m] = cnt[d];
            return cnt[d];
        }
        f[d][m] = 0;
        for(uint i = 0; i < (1 << N); ++ i)
            if (isok(i, d, m) && notepad(i, m - 1) != -1) f[d][m] >?= f[i][m - 1] + cnt[d];
    }
    return f[d][m];
}
void init(){
    for(uint i = 0; i < (1 << N); ++ i){
        cnt[i] = 0;
        for(int j = 0; j < N; ++ j)
            if (_t(i, j) == 1) ++ cnt[i];
    }
    //cout << _t(5, 0) << endl;
    //cout << cnt[5] << endl;
}
int calc(){
    cin >> M >> N;
    init();
    for(int i = 0; i < M; ++ i)
        cin >> tmap[i];
    memset(f, -1, sizeof(f));
    memset(mark, false, sizeof(mark));
    int ret = 0;
    for(uint i = 0; i < (1 << N); ++ i){
        ret >?= notepad(i, M - 1);
        //cout << notepad(i, M - 1) << endl;
    }
    return ret;
}
int main(){
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w+", stdout);
    int C;
    cin >> C;
    for(int i = 1; i <= C; ++ i)
        printf("Case #%d: %d\n", i, calc());
    return 0;
}

