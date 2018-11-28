#include <cstdio>
#include <cstring>
#include <map>
using namespace std;
#define maxn 102
map<char, int>p[maxn];
char word[maxn][64];
int q[16];
#define MOD 10009
int f[256];
char str[128];
int K, n;
void dfs(int x) {
    if (1 <= x && x <= K) {
        int cur = 1;
        int ans = 0;
        for (int i = 0; str[i]; ++i) {
            if (str[i] == '+') {
                ans = (ans + cur) % MOD;
                cur = 1;
            } else {
                cur = (cur * f[str[i]]) % MOD;
            } 
        }
        ans = (ans + cur) % MOD;
        q[x] = (q[x] + ans) % MOD;
    }
    if (x == K) {
        return;
    }
    for (int i = 0; i < n; ++i) {
        for (map<char, int>::iterator iter = p[i].begin();
                iter != p[i].end(); ++iter) {
            f[iter->first] += iter->second;
        }
        dfs(x + 1);
        for (map<char, int>::iterator iter = p[i].begin();
                iter != p[i].end(); ++iter) {
            f[iter->first] -= iter->second;
        }
    }
}
int main() {
//	freopen("a.txt", "r", stdin);
    int t;
    scanf("%d", &t);
    for (int kase = 1; kase <= t; ++kase) {
		memset(q, 0, sizeof(q));
        int i;
        scanf("%s%d", str, &K);
        scanf("%d", &n);
        for ( i = 0; i < n; ++i) {
            p[i].clear();
            scanf("%s", word[i]);
            for (int j = 0; word[i][j]; ++j) {
                if (p[i].find(word[i][j]) == p[i].end()) {
                    p[i][word[i][j]] = 1;
                } else {
                    ++p[i][word[i][j]];
                }
            }
        }
        memset(f, 0, sizeof(f));
        dfs(0);
        printf("Case #%d:", kase);
        for(i = 1; i <= K; ++i) {
            printf(" %d", q[i]);
        }
        puts("");
    }
    return 0;
}
