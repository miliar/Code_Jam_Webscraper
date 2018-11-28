#include <cstdio>
#include <cstring>
using namespace std;
const int maxc = 'Z' + 1;

int n, c, d, len;
char map[maxc][maxc];
bool dead[maxc][maxc];
int exist[maxc];
char s[100 + 10], ans[200 + 10];

void append(char c)
{
    if (len) {
        char pc = ans[len - 1];
        if (map[c][pc] < maxc) {
            --exist[ans[--len]];
            append(map[c][pc]);
        } else {
            bool cleaned = false;
            for (int i = 'A'; i <= 'Z'; i++)
                if (dead[c][i] && exist[i]) {
                    memset(exist, 0, sizeof(exist));
                    len = 0;
                    cleaned = true;
                }

            if (!cleaned) {
                ++exist[c];
                ans[len++] = c;
            }
        }
    } else {
        ++exist[c];
        ans[len++] = c;
    }
}

int main(void)
{
    int T;
    scanf("%d", &T);
    for (int loop = 1; loop <= T; loop++) {
        for (int i = 'A'; i <= 'Z'; i++)
            for (int j = 'A'; j <= 'Z'; j++)
                map[i][j] = maxc;

        memset(dead, false, sizeof(dead));
        memset(exist, 0, sizeof(exist));

        scanf("%d", &c);
        for (int i = 0; i < c; i++) {
            char var[5];
            scanf("%s", var);
            map[var[0]][var[1]] = map[var[1]][var[0]] = var[2];
        }

        scanf("%d", &d);
        for (int i = 0; i < d; i++) {
            char var[5];
            scanf("%s", var);
            dead[var[0]][var[1]] = dead[var[1]][var[0]] = true;
        }

        scanf("%d", &n);
        scanf("%s", s);

        len = 0;
        for (int i = 0; i < n; i++)
            append(s[i]);

        printf("Case #%d: [", loop); 
        for (int i = 0; i < len; i++) {
            putchar(ans[i]);
            if (i + 1 < len) {
                putchar(',');
                putchar(' ');
            }
        }
        putchar(']');
        putchar('\n');
    }
    return 0;
}
