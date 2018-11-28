#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
using namespace std;

const int maxn = 5000 + 100;
int n, m, len;
char word[maxn][16], line[1024];
bool flag[16][32];

void convert(char* s) {
    memset(flag, false, sizeof(flag));
    int idx = 0;
    for (int i = 0; s[i] != 0; ++i) {
        if (s[i] == '(') {
            int j;
            for (j = i + 1; s[j] != ')'; ++j) {
                flag[idx][s[j] - 'a'] = true;
            }
            i = j;
        } else {
            flag[idx][s[i] - 'a'] = true;
        }
        idx++;
    }
}

int main() {
    scanf("%d%d%d", &len, &n, &m);
    for (int i = 0; i < n; ++i) {
        scanf("%s", word[i]);
    }
    for (int i = 0; i < m; ++i) {
        scanf("%s", line);
        convert(line);
        int ans = 0;
        for (int j = 0; j < n; ++j) {
            bool ok = true;
            for (int k = 0; k < len && ok; ++k) if (!flag[k][word[j][k] - 'a']) {
                ok = false;
            }
            if (ok) {
                ans++;
            }
        }
        printf("Case #%d: %d\n", i + 1, ans);
    }
    return 0;
}
