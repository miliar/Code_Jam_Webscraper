#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <iostream>
#include <ctime>
using namespace std;
#define rep(i,n) for(int i=0;i<n;++i)
#define REP(i,a,b) for(int i=a;i<b;++i)
#define sz size()
#define pb(x) push_back(x)
typedef long long LL;
const int N = 1001;

int n;
int a[N];

int solve() {
    int s = 0, sum=0;
    for (int i = 0; i < n; ++i) {
        s ^= a[i];
        sum += a[i];
    }
    if (s) puts("NO");
    else {
        sort(a, a + n);
        printf("%d\n", sum - a[0]);
    }
}

int main() {
      freopen("in.txt", "r", stdin);
      freopen("outC.txt", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int i = 1; i <= cas; ++i) {
        scanf("%d", &n);
        for (int j = 0; j < n; ++j) {
            scanf("%d", a + j);
        }
        printf("Case #%d: ", i);
        solve();
    }
}