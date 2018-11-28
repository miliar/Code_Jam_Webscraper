#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cstdio>
#include <cmath>

using namespace std;
typedef long long LL;
const int MaxN = 1005;

double X[MaxN], Y[MaxN];
int R[MaxN];
LL N, W, L;
double eps = 1e-9;

int cmp(int a, int b){
    return a > b;
}

double sqr(double a){
    return a * a;
}

int check(){
    for(int i = 0; i < N; ++i){
        for(int j = i + 1; j < N; ++j){
            if(sqrt(sqr(X[i] - X[j]) + sqr(Y[i] - Y[j])) < R[i] + R[j] - eps) return 0;
        }
    }
    return 1;
}

int main(){
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B.txt", "w", stdout);
    int T;scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas){
        scanf("%lld%lld%lld", &N, &W, &L);
        for(int i = 0; i < N; ++i){
            scanf("%d", R + i);
        }
        W *= 100, L *= 100;
        W ++, L ++;
       // sort(R, R + N, cmp);
        while(1){
            for(int i = 0; i < N; ++i){
                X[i] = (LL)rand() * rand() % W * rand() % W / 100.0;
                Y[i] = (LL)rand() * rand() % L * rand() % L / 100.0;
            }
            if(check()){
                printf("Case #%d:", cas);
                for(int i = 0; i < N; ++i){
                    printf(" %.2f %.2f", X[i], Y[i]);
                }
                puts("");
                break;
            }
        }
    }
}
