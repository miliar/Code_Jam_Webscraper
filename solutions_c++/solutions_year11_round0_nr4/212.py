#include <stdio.h>
using namespace std;
int T, N, ans, num;
FILE *fin = fopen("input.in", "r");
FILE *fout = fopen("output.out", "w");

int main() {
    fscanf(fin, "%d", &T);
    for(int t = 0; t < T; t++) {
        fscanf(fin, "%d", &N);
        ans = 0;
        for(int i = 0; i < N; i++) {
            fscanf(fin, "%d", &num);
            if (num != i + 1)
                ans++;
        }
        fprintf(fout, "Case #%d: ", t + 1);
        fprintf(fout, "%d", ans);
        fprintf(fout, ".000000\n");
    }
}
