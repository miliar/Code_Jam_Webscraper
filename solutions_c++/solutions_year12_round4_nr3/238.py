#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cstdio>
#include <cmath>
#include <time.h>

using namespace std;
typedef long long LL;
const int MaxN = 1005;
const int inf = 1000;

int X[MaxN];
int R[MaxN];
LL N, W, L;

int cmp(int a, int b){
    return a > b;
}

double sqr(double a){
    return a * a;
}

int cha(int X1, int Y1, int X2, int Y2){
    return X1 * Y2 - Y1 * X2;
}

int check(){
    for(int i = 1; i < N; ++i){
        for(int j = i + 1; j <= N; ++j){
            if(j == R[i]) continue;
            if(cha(R[i] - i, X[R[i]] - X[i], j - i, X[j] - X[i]) >= 0) return 0;
        }
    }
    return 1;
}

int main(){
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C.txt", "w", stdout);
    int T;scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas){
        scanf("%d", &N);
        for(int i = 1; i < N; ++i){
            scanf("%d", R + i);
        }
        int IOp = clock();
        printf("Case #%d:", cas);
        int F = 0;
        while(1){
            int P = clock();
            if(P - IOp >= 10000) break;
            for(int i = 1; i <= N; ++i){
                X[i] = (LL)rand() % inf;
            }
            if(check()){
                F = 1;
                for(int i = 1; i <= N; ++i){
                    printf(" %d", X[i]);
                }
                puts("");
                break;
            }
        }
        if(!F) {
            puts(" Impossible");
        }
    }
}
