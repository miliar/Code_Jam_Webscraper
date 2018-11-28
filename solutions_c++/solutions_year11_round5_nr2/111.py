#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

const int INF = 100000000;
int cnt[10010];
int maxa;
int best;

int tryit() {
    int i, j, best = INF;
    vector<int> v;
    for (i = 1 ; i <= maxa + 1 ; i++) {
        vector<int> tv;
        for (j = 0 ; j < cnt[i] && j < v.size() ; j++) {
            ++v[j];
            tv.push_back(v[j]);
        }
        if (j < cnt[i]) {
            for ( ; j < cnt[i] ; j++)
                tv.push_back(1);
        } else {
            for ( ; j < v.size() ; j++) {
                if (v[j] < best) best = v[j];
            }
        }
        v = tv;
        sort(v.begin(), v.end());
    }
    return best;
}

int main() {
    freopen("b-large.in","r",stdin);
    freopen("b-large.out","w",stdout);
    int T, ca, n;
    scanf("%d",&T);
    for (ca = 1 ; ca <= T ; ++ca) {
        scanf("%d",&n);
        printf("Case #%d: ",ca);
        if (n == 0) {
            printf("0\n");
            continue;
        }
        memset(cnt, 0, sizeof(cnt));
        maxa = 0;
        while (n--) {
            int tmp;
            scanf("%d",&tmp);
            if (tmp > maxa) maxa = tmp;
            ++cnt[tmp];
        }

        printf("%d\n", tryit());
    }
    return 0;
}
/*
4
10 1 2 3 4 5 10 9 8 7 6
8 101 102 103 104 105 106 103 104
0
5 1 2 3 4 9
*/
