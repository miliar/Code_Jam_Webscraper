#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int main() {
	// freopen("B_large_in.txt", "r", stdin);
	// freopen("B_large_out.txt", "w", stdout);
    int tc;
    scanf("%d", &tc);
    char s[128];
    for (int tci = 1; tci <= tc; ++tci) {
        scanf("%s", s);
        int len = strlen(s);
        printf("Case #%d: ", tci);
        if (next_permutation(s, s + len)) {
            printf("%s\n", s);
        }
        else {
            // reverse(s, s + len);
            int i, j;
            for (i = 0; s[i] == '0'; ++i);
            putchar(s[i]);
            for (j = 0; j <= i; ++j) putchar('0');
            printf("%s\n", s + i + 1);
        }
    }
    return 0;
}
