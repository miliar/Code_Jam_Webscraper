#include <cstdio>
#include <cstring>

using namespace std;

const char *s = "welcome to code jam";
const int l = 19;
int count[50];

void solve() {
    char c;

    memset(count, 0, sizeof(count));
    count[0] = 1;
    scanf("%c", &c);
    while(c == '\n' || c == '\r') scanf("%c", &c);

    while(c != '\n' && c != '\r') {
        for (int i = 0; i < l; i++) {
            if (s[i] == c) {
                count[i+1] += count[i];
                count[i+1] %= 10000;
            }
        }
        scanf("%c", &c);
    }
    printf("%04d\n", count[l]);
}

int main() {
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        printf("Case #%d: ", i+1);
        solve();
    }
    return 0;
}
