#include <cstdio>


int main(void) {
 int test; scanf("%d", &test);

 for (int cs = 0; cs < test; ++cs) {
    int n; scanf("%d", &n);
    int seq[1000]; for (int i = 0; i < n; ++i) scanf("%d", seq+i);

    int noswaps = 0;
    for (int i = 0; i < n; ++i)
        if (seq[i] != i+1) ++noswaps;

    double sol = noswaps;

    printf("Case #%d: %0.6lf\n", cs+1, sol);
 }

 return 0;
}
