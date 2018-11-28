//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;

int N, d;
int D[10047], L[10047], niz[10047];

int extra(){
    scanf("%d",&N);
    For(i,N) scanf("%d%d",D+i,L+i);
    For(i,N+1) niz[i] = 0; 
    scanf("%d",&d);
    niz[0] = D[0];
    D[N] = d;
    L[N] = 1;
    For(i,N){
        for(int j = i+1; j<=N && D[i]+niz[i]>=D[j]; ++j){
            niz[j] = max(niz[j], min(L[j], D[j]-D[i]));
        }
    }
    if (niz[N]) printf("YES\n");
    else printf("NO\n");
    
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
