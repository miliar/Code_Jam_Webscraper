#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <numeric>
#include <algorithm>
using namespace std;
#ifdef DEBUGRUN
#define LOG(a) (cerr<<__LINE__<<": "#a" = "<<(a)<<endl)
#define DBG(...) (__VA_ARGS__)
#else
#define LOG(...) ((void)0)
#define DBG(...) ((void)0)
#endif
#define rep(i, n) for(int i=0; i<(int)(n); i++)
#define mp make_pair
#define foreach(it, c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
typedef long long Int;
#define INF (1<<30)

int main() {
    int T;
    scanf("%d", &T);
    rep(q, T) {
        int n;
        scanf("%d", &n);
        int x=0, s=0, m=INF;
        rep(i, n) {
            int a;
            scanf("%d", &a);
            x = x ^ a;
            s = s + a;
            m = min(m, a);
        }
        printf("Case #%d: ", q+1);
        if(x!=0) printf("NO\n");
        else printf("%d\n", s-m);
    }
    return 0;
}


