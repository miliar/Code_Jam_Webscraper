#include <cstdio>
#include <algorithm>

using namespace std;

const int MOD = 10007;

int nrT, N, M, n;
bool calc[200][200], bad[200][200];
int sol[200][200], xp[20], yp[20];

int ans(int x, int y){
    if (x<1 || y<1 || bad[x][y]) return 0;
    if (x==1 && y==1) return 1;
    if (calc[x][y])
       return sol[x][y];   
    calc[x][y] = true;
    sol[x][y] = ans(x-2, y-1) + ans(x-1, y-2);
    sol[x][y] %= MOD;
    return sol[x][y];
}

void solve(){
     nrT++;
     printf("Case #%d: ", nrT);     
     memset(calc, 0, sizeof(calc));
     memset(bad, 0, sizeof(bad));
     scanf("%d %d %d\n", &N, &M, &n);
     for (int i=0; i<n; i++){
         scanf("%d %d", xp+i, yp+i);
         bad[xp[i]][yp[i]] = true;
     }
     printf("%d\n", ans(N, M));
}

int main(){
    freopen("data.in", "r", stdin);
    freopen("data.out", "w",stdout);
    int tst;
    scanf("%d", &tst);
    while (tst--)
          solve();
    return 0;
}
