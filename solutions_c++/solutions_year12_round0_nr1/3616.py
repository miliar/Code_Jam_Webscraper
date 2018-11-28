#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 205;
const char map[30] = "yhesocvxduiglbkrztnwjpfmaq";
char s[maxn];

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int test, testi, n, i;
    scanf("%d", &test);
    for (testi = 1; testi <= test; ++testi) {
        scanf(" "); gets(s); n = strlen(s);
        printf("Case #%d: ", testi);
        for (i = 0; i < n; ++i)
            if (s[i] != ' ')
                printf("%c", map[s[i] - 'a']);
            else printf("%c", s[i]);
        printf("\n");
    }
    fclose(stdout);
    return 0;
}
