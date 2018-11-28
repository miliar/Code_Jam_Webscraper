#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <cctype>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)

const int maxn = 1111;

int res, n, id[maxn], ok[maxn];
char mp[maxn][maxn], str[maxn];

int check() {
    int mx = -1;
    for (int i = 0; i < n; i++) if (str[i] == '1') mx = i;
    return mx;
}

int main(){
    int cas;
    scanf("%d", &cas);
    for (int tt = 0; tt < cas; tt++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf(" %s", mp[i]);

        for (int i = 0; i < n; i++) {
            strcpy(str, mp[i]);
            ok[i] = check();
        }
        for (int i = 0; i < n; i++) id[i] = i;
        res = 0;
        for (int i = 0; i < n; i++) {
            int k = -1;
            for (int j = i; j < n; j++) if (ok[id[j]] <= i) {k = j; break;}
            if (i == k) continue;
            for (int j = k; j > i; j--) swap(id[j], id[j - 1]), res++;
        }
        cout << "Case #" << tt + 1 << ": " << res << endl;
    }
}
