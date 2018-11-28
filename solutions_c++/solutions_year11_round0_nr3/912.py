#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;

#define Fill(A, n) memset(A, n, sizeof(A))
string FILENAME = "C-large";

const int MAX_N = 1000;

int a[MAX_N];

int main() {
    freopen((FILENAME + ".in").c_str(), "r", stdin);
    freopen((FILENAME + ".out").c_str(), "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int N;
        scanf("%d", &N);
        for (int i = 0; i < N; i++) scanf("%d", &a[i]);

        int result = 0, minValue = a[0], sum = 0;
        for (int i = 0; i < N; i++) {
            result ^= a[i];
            minValue = min(minValue, a[i]);
            sum += a[i];
        }

        if (result) printf("Case #%d: NO\n", t + 1);
        else printf("Case #%d: %d\n", t + 1, sum - minValue);
    }
}
