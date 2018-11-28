#include <cstdio>
#include <cstring>
#include <cmath>

#include <algorithm>
#include <iostream>

using namespace std;

typedef long long LL;
typedef double db;

const int Max = 1024;
const int MaxS = 1 << 20;

int N,V[Max];
int R[MaxS],C[MaxS];

bool cmp(int i,int j){
    return R[i] < R[j];
}
void out(int s){
    int f = 0;
    for (int i = 0;i < N;i++)
        if (s & (1 << i)){
            if (f++) putchar(' ');
            printf("%d",V[i]);
        }
    puts("");
}

int main(){
    freopen("W:\\C-small-attempt0.in","r",stdin);
    freopen("W:\\C-small-attempt0.out","w",stdout);
    int tCase;
    scanf("%d",&tCase);
    for (int ct = 1;ct <= tCase;ct++){
        scanf("%d",&N);
        memset(R,0,sizeof(R));
        for (int i = 0;i < N;i++){
            scanf("%d",&V[i]);
            R[1 << i] = V[i];
        }
        int g = 1 << N;
        for (int i = 0;i < N;i++)
            for (int j = 1;j < g;j++)
                if (j & (1 << i))
                    R[j] += R[j ^ (1 << i)];
        for (int i = 0;i < g;i++)
            C[i] = i;
        sort(C,C + g,cmp);
        int ri = -1;
        for (int i = 1;i < g;i++)
            if (R[C[i - 1]] == R[C[i]]){
                ri = i;
                break;
            }
        printf("Case #%d:\n",ct);
        if (ri == -1){
            puts("Impossible");
        }else{
            out(C[ri]);
            out(C[ri - 1]);
        }
    }
    return 0;
}
