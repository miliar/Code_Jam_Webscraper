#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int a[100000], n, val, change[12000];
int best[12000][2];

bool hasSons(int k){
     return 2*k+1 <= n; 
}

void improve(int &k, int val){
     if (val < k) k = val;
}

void calc(int k){
    int mult = (1-change[k])*99999+1; 
    int costOr = (a[k]==1)*mult;
    int costAnd = (a[k]==0)*mult;
    for (unsigned i=0; i<2; i++)
        for (unsigned j=0; j<2; j++){
            improve(best[k][i | j], best[2*k][i]+best[2*k+1][j]+costOr);
            improve(best[k][i & j], best[2*k][i]+best[2*k+1][j]+costAnd);            
        }
}

int nr;

void solve(){
     scanf("%d %d", &n, &val);
     memset(best, 0x3f, sizeof(best));
     for (int i=1; i<=n; i++){
         scanf("%d", a+i);
         if (i<=(n-1)/2) scanf("%d", &change[i]);
     }
     for (int i=n; i>0; i--)
         if (!hasSons(i)){
            best[i][a[i]] = 0;
         }  else calc(i);
     nr++;
     if (best[1][val] <= n){
        printf("Case #%d: %d\n", nr, best[1][val]);
     }  else         {
        printf("Case #%d: IMPOSSIBLE\n", nr);
     }
}

int main(){
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int tst;
    scanf("%d", &tst);
    while (tst--)
          solve();
    return 0;
}
