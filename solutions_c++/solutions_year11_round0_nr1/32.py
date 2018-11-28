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
#define INF MY_INFINITY

int n;

int main() {
    int T;
    scanf("%d", &T);
    rep(q, T) {
        int n;
        scanf("%d", &n);
        int p1=1, t1=0, p2=1, t2=0;
        int cur = 0;
        rep(i, n) {
            char ch;
            int at;
            scanf(" %c%d", &ch, &at);
            if(ch=='O') {
                int diff = abs(p1-at);
                cur += 1 + max(0, diff-(cur-t1));
                p1 = at;
                t1 = cur;
            }
            else {
                int diff = abs(p2-at);
                cur += 1 + max(0, diff-(cur-t2));
                p2 = at;
                t2 = cur;
            }
        }
        printf("Case #%d: %d\n", q+1, cur);
    }
    return 0;
}


