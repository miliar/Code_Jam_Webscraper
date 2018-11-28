#include <cstdio>

#define For(i,n) for (int i = 0; i < n; ++i)

int l, n, T, b[16], ans;
char s[5000][16], t[256];

int r() {
        char c;
        while ((c = getchar()) != '(' && !('a' <= c && c <= 'z'));
        if ('a' <= c && c <= 'z') return 1 << c - 'a';
        int t = 0;
        while ((c = getchar()) != ')') t |= 1 << c - 'a';
        return t;
}

bool ok(int x) {
        For(i,l) if (!(b[i] & (1 << s[x][i] - 'a'))) return 0;
        return 1;
}

int main() {
        scanf("%d%d%d", &l, &n, &T);
        For(i,n) scanf("%s", s + i);
        For(i,T) {
                For(j,l) b[j] = r();
                ans = 0;
                For(j,n) if (ok(j)) ++ans;
                printf("Case #%d: %d\n", i + 1, ans);
        }
        return 0;
}
