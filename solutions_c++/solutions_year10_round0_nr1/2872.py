#include <cstdio>

int n_tests;
int n, k;

int main() {

    FILE* fin = fopen("input.txt", "r");
    FILE* fout = fopen("output.txt", "w");
    fscanf(fin, "%d", &n_tests);

    for (int test=1 ; test<=n_tests ; test++) {
        fscanf(fin, "%d %d", &n, &k);
        if (k == 0) {
            fprintf(fout, "Case #%d: OFF\n", test);
        } else {
            fprintf(fout, "Case #%d: ", test);
            if (k % (1<<n) == (1<<n)-1) {
                fprintf(fout, "ON\n");
            } else {
                fprintf(fout, "OFF\n");
            }
        }
    }
    return 0;
}
