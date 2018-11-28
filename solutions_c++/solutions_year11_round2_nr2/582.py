#include <cstring>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <limits>
using namespace std;

int n, d, pos[200], v[200];

bool check(double m) {
    double min = -1e100;
    for (int i = 0; i < n; ++i) {
        if (min < pos[i] - m) min = pos[i] - m;
        min += (v[i] - 1) * d;
        if (min > pos[i] + m) return false;
        min += d;
    }
    return true;
}

int main() {
    FILE *fin = fopen("B-small-attempt0.in", "r");
    FILE *fout = fopen("out.txt", "w");
    int test;
    fscanf(fin, "%d", &test);
    for (int i = 1; i <= test; ++i) {
        fprintf(fout, "Case #%d: ", i);
        fscanf(fin, "%d%d", &n, &d);
        for (int j = 0; j < n; ++j)
            fscanf(fin, "%d%d", &pos[j], &v[j]);
        double min, max = 1;
        while (!check(max)) max *= 2;
        if (max == 1) min = 0;
        else min = max / 2;
        while (max - min > 1e-7) {
            double m = (min + max) / 2;
            if (check(m)) max = m;
            else min = m;
        }
        fprintf(fout, "%lf\n", min);
    }
    fclose(fout);
    fclose(fin);
    return 0;
}
