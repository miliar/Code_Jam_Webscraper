#include <iostream>
using namespace std;
const int N = 1001, C = 11;
const int INF = 3214567;
int d[N][N][C];
int a, b, c;

void init(){
    int l, i, j;
    int k, k1, k2, t, t1, t2;

    a = 1; b = 1000; t1 = b-a;
    for (c=2;c<=10;c++) {
        for (l=1;l<=t1;l++){
            t2 = b-l;
            for (i=a;i<=t2;i++){
                j = i+l;
                if (i*c>=j) d[i][j][c] = 0;
                else {
                    k1 = i+1; k2 = j-1; d[i][j][c] = INF;
                    for (k=k1;k<=k2;k++){
                        t = max(d[i][k][c], d[k][j][c]);
                        if (t < d[i][j][c]) d[i][j][c] = t;
                    }
                    d[i][j][c]++;
                }
            }
        }
    }
}

int main(){
    freopen("2.in", "r", stdin);
    freopen("2.out", "w", stdout);
    init();
    int T; cin >> T;
    for (int i=1;i<=T;i++){
        cin >> a >> b >> c;
        printf("Case #%d: %d\n", i, d[a][b][c]);
    }
}
