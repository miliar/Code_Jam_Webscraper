
#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
    int tst;
    scanf("%d", &tst);
    for (int cas = 0; cas < tst; ++cas) {
        int N;
        scanf("%d", &N);
        static int last[64];
        for (int i = 0; i < N; ++i) {
            static char str[80];
            scanf("%s", str);
            last[i] = 0;
            for (int j = 0; j < N; ++j)
                if (str[j] == '1')
                    last[i] = j + 1;
        }
        int res = 0;
        for (int i = 0; i < N; ++i) {
            for (int j = i; j < N; ++j)
                if (i + 1 >= last[j]) {
                    int jj = j;
                    while (jj != i) {
                        swap(last[jj], last[jj - 1]);
                        --jj;
                        ++res;
                    }
                    break;
                }
        }
        printf("Case #%d: %d\n", cas + 1, res);
    }
    return 0;
}