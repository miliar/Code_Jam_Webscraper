#include <cstdio>
#include <map>
#include <algorithm>
#include <cassert>
#include <vector>
#include <stack>
#include <cmath>
#include <queue>
#include <iostream>
#include <cstring>
#define REP(i,n) for(int i = 0;i<n;i++)
#define FOREACH(it,u) for(__typeof(u.begin()) it = u.begin();it!=u.end();it++)
#define PB push_back
#define st first
#define nd second
#define PI pair<int,int>
#define debug if(0)
typedef long long LL;

const int MAXN = 1000;
const int BRAK = -2000000000;
const int INF = 2000000002;

using namespace std;

int t[MAXN+10][MAXN+10];
int C, L, P;

int f(int p, int k) {
    if(p>k) return 0;
    if(t[p][k]!=-1) {
        return t[p][k];
    }
    if(!(C*p<=k)) {
        t[p][k]=0;
        return 0;
    }
    int val=1000000000;
    for(int i = C*p;i<=k;i++) {
        val=min(val,max(f(p,i-1),f(i,k)));
        if(!(C*i<=k)) break;
    }
    t[p][k]=val+1;
    return t[p][k];
}

void solve() {
    scanf("%d %d %d", &L, &P, &C);
    for(int i = L;i<=P;i++) for(int j = L;j<=P;j++) t[i][j]=-1;
    printf("%d\n", f(L,P-1));
}

int main() {
    int z;
    scanf("%d", &z);
    for(int i = 1;i<=z;i++) {
        printf("Case #%d: ", i);
        solve();
    }
}
