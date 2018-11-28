#include <cstdio>
#include <string>
#include <map>
#include <vector>
#include <set>
#define MaxN 510
#define MOD 100003

using namespace std;

int comb[555][555];
int sol[555][555];

void precalc(){
    for (int i=0; i<MaxN; i++){
        comb[i][0] = comb[i][i] = 1;
        for (int j=1; j<i; j++)
            comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD;
    }
    for (int i=2; i<MaxN; i++, fprintf(stderr, "%d\n", i)){
        sol[i][1] = 1;
        for (int k=2; k<i; k++)
            for (int lk=1; lk<k; lk++){
                sol[i][k] += ((long long)sol[k][lk] * comb[i-k-1][k-lk-1]) % MOD;
            }
    }
}

void solve(int tst)
{
    int n, rez = 0;
    scanf("%d", &n);
    for (int i=1; i<n; i++)
        rez = (sol[n][i] + rez) % MOD;
    printf("Case #%d: %d\n", tst, rez);
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    precalc();
    int tst;
    scanf("%d", &tst);
    for (int i=1; i<=tst; i++)
        solve(i);
    fflush(stdout);
    //while (1);
    return 0;
}
