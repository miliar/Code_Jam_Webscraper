#include <cstdio>
#include <cstring>
#include <cmath>

#include <algorithm>
#include <iostream>

using namespace std;

typedef long long LL;
typedef double db;

const int Max = 1024;

int V[Max];

int main(){
    freopen("W:\\A-small-attempt0.in","r",stdin);
    freopen("W:\\A-small-attempt0.out","w",stdout);
    int tCase;
    scanf("%d",&tCase);
    for (int ct = 1;ct <= tCase;ct++){
        int N,X = 0;
        scanf("%d",&N);
        for (int i = 0;i < N;i++){
            scanf("%d",&V[i]);
            X += V[i];
        }
        printf("Case #%d:",ct);
        for (int i = 0;i < N;i++){
            db s = 0.0,t = 1.0;
            for (int j = 0;j < 100;j++){
                db d = (s + t) * 0.5;
                db vd = V[i] + X * d;
                db rm = X * (1.0 - d);
                db sm = 0.0;
                for (int k = 0;k < N;k++) if (k != i)
                    if (V[k] < vd)
                        sm += vd - V[k];
                if (sm < rm) s = d;
                else t = d;
            }
            printf(" %.10f",s * 100.0);
        }
        puts("");
    }
    return 0;
}
