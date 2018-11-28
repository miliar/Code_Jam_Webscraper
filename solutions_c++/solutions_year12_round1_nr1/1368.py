#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 100000;

int main() {
    int T;
    int A, B, dBA, word;
    double p[MAXN];
    double prob[MAXN], tmp;
    double s;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &A, &B);
        dBA = B - A + 1;
        word = B + 1;
        p[A] = 0;
        for (int i = 0; i < A; i++) {
            scanf("%lf", &p[i]);
        }
        tmp = 1;
        for (int i = A; i >= 0; i--) {
            prob[i] = tmp * (1 - p[A-i]);
            tmp *= p[A-i];
        }
        // init with 'enter'
        s = word + 1;
        // compare to 'keep'
        s = min(s, dBA*prob[0] + (dBA + word)*(1-prob[0]));
        // compare to 'k backspaces'
        tmp = prob[0];
        for (int i = 1; i <= A; i++) {
            tmp += prob[i];
            s = min(s, (2*i + dBA)*tmp + (2*i + dBA + word)*(1-tmp));
        }
        // print solution
        printf("Case #%d: %.6lf\n", t, s);
    }
}
