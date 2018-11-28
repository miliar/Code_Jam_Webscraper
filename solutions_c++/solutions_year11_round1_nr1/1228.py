#include <cstring>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>

int n, pd, pg;

int gcd(int a, int b) {
    if (a == 0) return b;
    return gcd(b % a, a);
}

bool check() {
    if (pg == 0) {
        if (pd > 0) return false;
        return true;
    }
    if (pg == 100) {
        if (pd < 100) return false;
        return true;
    }
    int k = 100 / gcd(pd, 100);
    if (k <= n) return true;
    return false;
}

int main() {
    FILE *fin = fopen("A-small-attempt0.in", "r");
    FILE *fout = fopen("out.txt", "w");
    int t;
    fscanf(fin, "%d", &t);
    for (int i = 1; i <= t; ++i) {
        fprintf(fout, "Case #%d: ", i);
        fscanf(fin, "%d%d%d", &n, &pd, &pg);
        if (check())
            fprintf(fout, "Possible\n");
        else
            fprintf(fout, "Broken\n");
    }
    fclose(fout);
    fclose(fin);
    return 0;
}
