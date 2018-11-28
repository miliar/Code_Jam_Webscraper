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

int pre[2], in[2], n;
char s[N][10];
int id[N];

int solve() {
    pre[0] = pre[1] = 0;
    in[0] = in[1] = 1;
    for (int i = 0; i < n; ++i) {
        if (s[i][0] == 'O') {
            int t = id[i] - in[0];
            t = max(t, -t);
            int te = pre[1] - pre[0];
            if (t <= te) {
                pre[0] = pre[1] + 1;
            } else {
                pre[0] = pre[0] + t + 1;
            }
            in[0] = id[i];
        } else {
            int t = id[i] - in[1];
            t = max(t, -t);
            int te = pre[0] - pre[1];
            if (t <= te) {
                pre[1] = pre[0] + 1;
            } else {
                pre[1] = pre[1] + t + 1;
            }
            in[1] = id[i];
        }
     //   cout << pre[0] << " " << pre[1] << endl;
    }
    printf("%d\n", max(pre[0], pre[1]));
}

int main() {
   // freopen("in.txt","r",stdin);
   // freopen("out.txt","w",stdout);
    int cas;
    scanf("%d", &cas);
    for (int i = 1; i <= cas; ++i) {
        scanf("%d", &n);
        for (int j = 0; j < n; ++j) {
            scanf("%s%d", s[j], &id[j]);
        }
        printf("Case #%d: ", i);
        solve();
    }
}