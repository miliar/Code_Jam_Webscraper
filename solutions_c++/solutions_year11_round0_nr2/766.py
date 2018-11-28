#include <cstdio>
#include <cstring>

using namespace std;

int combine[26][26];
bool oppose[26][26];
int len;
char str[1 << 7];
int re_len;
char re[1 << 7];

void go() {
    re_len = 0;

    for (char* p = str; *p != '\0'; ++p) {
        if (re_len > 0 && combine[*p - 'A'][re[re_len - 1] - 'A'] >= 0) {
            re[re_len - 1] = combine[*p - 'A'][re[re_len - 1] - 'A'] + 'A';
        } else {
            bool good = true;

            for (int i = 0; i < re_len; ++i) {
                if (oppose[*p - 'A'][re[i] - 'A']) {
                    good = false;
                    break;
                }
            }

            if (good) {
                re[re_len++] = *p;
            } else {
                re_len = 0;
            }
        }
    }
}

int main() {
    int kases;
    int temp;

    scanf("%d", &kases);
    for (int k = 1; k <= kases; ++k) {
        memset(combine, -1, sizeof combine);
        memset(oppose, 0, sizeof oppose);

        scanf("%d", &temp);
        for (int i = 0; i < temp; ++i) {
            scanf("%s", str);
            combine[str[0] - 'A'][str[1] - 'A'] = combine[str[1] - 'A'][str[0] - 'A'] = str[2] - 'A';
        }

        scanf("%d", &temp);
        for (int i = 0; i < temp; ++i) {
            scanf("%s", str);
            oppose[str[0] - 'A'][str[1] - 'A'] = oppose[str[1] - 'A'][str[0] - 'A'] = true;
        }

        scanf("%d%s", &len, str);

        go();

        printf("Case #%d: [", k);
        for (int i = 0; i < re_len; ++i) {
            printf(i > 0 ? ", %c" : "%c", re[i]);
        }
        printf("]\n");
    }

    return 0;
}
