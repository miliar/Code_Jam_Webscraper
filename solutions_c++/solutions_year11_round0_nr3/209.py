#include <stdio.h>
using namespace std;
int T, N, ans, c, num, min;
FILE *fin = fopen("input.in", "r");
FILE *fout = fopen("output.out", "w");

int main() {
    fscanf(fin, "%d", &T);
    for(int t = 0; t < T; t++) {
        fscanf(fin, "%d", &N);
        c = 0;
        ans = 0;
        min = 1000000;
        for(int i = 0; i < N; i++) {
            fscanf(fin, "%d", &num);
            c ^= num;
            ans += num;
            if (min > num)
                min = num;
        }
        fprintf(fout, "Case #%d: ", t + 1);
        if (c != 0)
            fprintf(fout, "NO\n");
        else
            fprintf(fout, "%d\n", ans - min);
    }
}
