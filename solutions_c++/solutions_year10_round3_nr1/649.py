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

const int MAXN = 100000;
const int BRAK = -2000000000;
const int INF = 2000000002;

using namespace std;

int A[MAXN], B[MAXN];
void solve() {
    int n;
    scanf("%d", &n);
    REP(i,n) scanf("%d %d", &A[i], &B[i]);
    int il=0;
    REP(i,n) REP(j,i) {
        int x=B[i], y=B[j];
        if(A[i]>A[j]) swap(x,y);
        if(x>y) il++;
    }
    printf("%d\n", il);
}

int main() {
    int z;
    scanf("%d", &z);
    for(int i = 1;i<=z;i++) {
        printf("Case #%d: ", i);
        solve();
    }
}
