#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char s[64];

int main() {
    freopen("B.in", "rt", stdin);

    int N;
    scanf("%d ", &N);
    for (int i = 0; i < N; i++) {
        scanf(" %s", s);
        if (!next_permutation(s, s + strlen(s))) {
            char t[64];
            memset(t, 0, sizeof(t));
            t[0] = '0';
            for (int i = 0; s[i]; i++) {
                t[i + 1] = s[i];
            }
            for (int i = 0; t[i]; i++) {
                if (t[i] != '0') {
                    swap(t[0], t[i]);
                    break;
                }
            }
            memcpy(s, t, sizeof(s));
        }
        printf("Case #%d: %s\n", i + 1, s);
    }

    return 0;
}


