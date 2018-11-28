#include <cstdio>
#include <cstring>

const int maxl = 100000;
const int inf = 0x7fffffff;

char str[maxl], _str[maxl];
int K, len, ans;
int stack[1000];
bool used[1000];

void Check() {
    int i, j, cnt = 0;
    for (i = 0; i < len; i += K)
        for (j = 0; j < K; j++)
            _str[i + j] = str[i + stack[j]];
    for (i = 0; i < len; i++)
        if (!i || _str[i] != _str[i - 1]) cnt++;
    if (ans > cnt) ans = cnt;
}

void DFS(int dig) {
    if (dig == K) {
        Check();
        return;
    }
    int i;
    for (i = 0; i < K; i++)
        if (!used[i]) {
            used[i] = 1;
            stack[dig] = i;
            DFS(dig + 1);
            used[i] = 0;
        }
}

int main() {
    int t, i;
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        printf("Case #%d: ", i + 1);
        scanf("%d %s", &K, str);
        len = strlen(str);
        ans = inf;
        memset(used, 0, sizeof used);
        DFS(0);
        printf("%d\n", ans);
    }
    return 0;
}
