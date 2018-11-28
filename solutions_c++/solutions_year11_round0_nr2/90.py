#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 128;
char st[N], mpc[N][N], mpo[N][N], s[N];
int p[N], cnt[N], top;

void push(char ch) {
    cnt[st[++top] = ch] ++;
}
void pop() {
    cnt[st[top --]] --;
}
int main() {
    int cas, tt;
    scanf("%d", &tt);
    for (cas = 1; cas <= tt; cas ++) {
        int comb, oppo, len;
        memset(mpc, 0, sizeof(mpc));
        memset(cnt, 0, sizeof(cnt));
        memset(p, 0, sizeof(p));
        scanf("%d", &comb);
        while (comb--) {
            scanf("%s", s);
            mpc[s[0]][s[1]] = s[2];
            mpc[s[1]][s[0]] = s[2];
        }
        scanf("%d", &oppo);
        while (oppo--) {
            scanf("%s", s);
            mpo[s[0]][p[s[0]] ++] = s[1];
            mpo[s[1]][p[s[1]] ++] = s[0];
        }
        scanf("%d%s", &len, s);
        top = 0;
        for (int i = 0; i < len; i ++) {
            push(s[i]);
            if (top >= 2 && mpc[st[top]][st[top - 1]]) {
                char res = mpc[st[top]][st[top - 1]];
                pop(); pop(); push(res);
            } else
            for (int j = 0; j < p[s[i]]; j ++)
                if (cnt[mpo[s[i]][j]])
                    while (top > 0) pop();
        }
        printf("Case #%d: [", cas);
        for (int i = 1; i <= top; i ++) {
            putchar(st[i]);
            if (i < top) printf(", ");
        }
        printf("]\n");
    }
    return 0;
}

