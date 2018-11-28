#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>

using namespace std;

#define MP make_pair
typedef pair<int, int> PII;
typedef long long LL;

const int INF = 0x3f3f3f3f;
const int MAXN = 10086;
PII ar[MAXN];
int br[MAXN];

void solved(int nCase) {
    int N, D; scanf("%d", &N);
    ar[0].first = 0, ar[0].second = 0x3f3f3f3f;
    for (int i = 1; i <= N; ++i) {
        scanf("%d %d", &ar[i].first, &ar[i].second);
    }
    scanf("%d", &D);
    ar[N+1].first = D, ar[N+1].second = INF;
    memset(br, -1, sizeof(br));
    br[1] = ar[1].first;
    for (int i = 1; i <= N; ++i) {
        if (br[i] == -1) continue;
        int length = br[i];
        for (int j = i + 1; j <= N + 1; ++j) {
            if (ar[j].first - ar[i].first <= length) {
                int c = min(ar[j].second, ar[j].first - ar[i].first);
                if (br[j] == -1 || c > br[j]) 
                    br[j] = c;
            }
        }
    }
    printf("Case #%d: ", nCase);
    if (br[N+1] == -1) printf("NO\n");
    else printf("YES\n");
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int nCase; scanf("%d", &nCase);
    for (int tCase = 1; tCase <= nCase; ++tCase) {
        //printf("Case #%d:", tCase);
        solved(tCase);
    }
    return 0;
}