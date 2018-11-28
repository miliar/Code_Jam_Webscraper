#include <cstdio>
#include <algorithm>
using namespace std;

int T[20001];
int C[20001];
int V[20001];
int X[20001][2];

static const int IMP=9999999;

int VV, M;

int main() {
    int N;
    scanf("%d", &N);
    for (int cix=0; cix<N; cix++) {
        scanf("%d%d", &M, &VV);
        for (int i=1; i<=M/2; i++) scanf("%d%d", &T[i], &C[i]);
        for (int i=M/2+1; i<=M; i++) scanf("%d", &V[i]), X[i][V[i]]=0, X[i][!V[i]]=IMP;
        
        for (int i=M/2; i>=1; i--) {
            int a=2*i, b=2*i+1;
            int x0=IMP, x1=IMP;
            
            if (T[i]==1) { // and
                x1=min(x1, X[a][1]+X[b][1]);
                if (C[i]) x1=min(x1, min(X[a][1]+1, X[b][1]+1));
                x0=min(x0, min(X[a][0], X[b][0]));
                if (C[i]) x0=min(x0, X[a][0]+X[b][0]+1);
            }
            
            else { // or
                x1=min(x1, min(X[a][1], X[b][1]));
                if (C[i]) x1=min(x1, X[a][1]+X[b][1]+1);
                x0=min(x0, X[a][0]+X[b][0]);
                if (C[i]) x0=min(x0, min(X[a][0]+1, X[b][0]+1));
            }
            X[i][0]=x0, X[i][1]=x1;
        }
        
        //for (int i=1; i<=M; i++) printf("%d %d\n", X[i][0], X[i][1]);
        
        if (X[1][VV]<IMP) printf("Case #%d: %d\n", cix+1, X[1][VV]);
        else printf("Case #%d: IMPOSSIBLE\n", cix+1);
    }
    
    return 0;
}
