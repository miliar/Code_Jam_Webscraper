// autor: Andrzej Pezarski
// GCJ2010
// Bacteria

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;

int X1[1000];
int Y1[1000];
int X2[1000];
int Y2[1000];
int mark[1000];
int T, R;
int X, Y, W, W2;

bool test(int a, int b) {
    return (X1[a]<=X2[b]+1 && X1[b]<=X2[a]+1) && (Y1[a]<=Y2[b]+1 && Y1[b]<=Y2[a]+1);
}

void DFS(int v, int k) {
    if (mark[v]) return;
    mark[v]=k;
    X=max(X, X2[v]);
    Y=max(Y, Y2[v]);
    W=min(X1[v]+Y1[v], W);
    for (int w=0; w<R; w++) if (test(v, w)) DFS(w, k);
}

int main() {
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        scanf("%d", &R);
        for (int i=0; i<R; i++) {
            scanf("%d%d%d%d", X1+i, Y1+i, X2+i, Y2+i);
            mark[i]=0;
        }
        W2=0;
        for (int i=0; i<R; i++) {
            X=Y=0;
            W=1000000000;
            DFS(i, i+1);
            W2=max(W2, X+Y-W);
        }

        printf("Case #%d: %d\n", t, W2+1);
    }
    return 0;
}
