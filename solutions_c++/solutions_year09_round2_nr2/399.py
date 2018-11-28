#include <climits>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

#define foreach(iter, cont) \
    for (typeof((cont).begin()) iter = (cont).begin(); iter != (cont).end(); iter++)
typedef long long LL;

void solve(char* s)
{
    int n = strlen(s);
    int cnt[10];
    memset(cnt, 0, sizeof(cnt));
    for (int i = n-1; i >= 0; i--) {
        for (int j = s[i]-'0'+1; j < 10; j++) if (cnt[j] > 0) {
            for (int q = 0; q < i; q++)
                printf("%c", s[q]);
            cnt[s[i]-'0']++;

            printf("%d", j);
            cnt[j]--;
            for (int q = 0; q < 10; q++)
                while (cnt[q]--) printf("%d", q);
            return;
        }
        cnt[s[i]-'0']++;
    }

    int begin = 1;
    while (cnt[begin] == 0) begin++;
    cnt[begin]--;
    printf("%d0", begin);
    while (cnt[0]--) printf("0");
    while (begin < 10) {
        while (cnt[begin]--) printf("%d", begin);
        begin++;
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        char str[50];
        scanf("%s", str);
        printf("Case #%d: ", i);
        solve(str);
        printf("\n");
    }
    return 0;
}
