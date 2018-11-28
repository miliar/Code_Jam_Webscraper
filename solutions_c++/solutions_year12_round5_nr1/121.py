#include <cmath>
#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

typedef struct lvl_t {
    int id;
    int L;
    int P;
};

bool cmp(const lvl_t &a, const lvl_t &b) {
    int cv = a.L * b.P - a.P * b.L;
    if (cv < 0) return true;
    else if (cv > 0) return false;
    return a.id < b.id;
}

int main() {
    FILE *fin, *fout;    
    fin = fopen("D:\\TopCoder\\gcj2012\\R3\\A-large.in", "r");
    fout = fopen("D:\\TopCoder\\gcj2012\\R3\\A.out", "w");
    int T;
    fscanf(fin, "%d\n", &T);
    for (int ca = 1; ca <= T; ca++) {
        int N;
        fscanf(fin, "%d", &N);
        lvl_t lvl[N];
        for (int i = 0; i < N; ++i) {
            lvl[i].id = i;
            fscanf(fin, "%d", &lvl[i].L);
        }
        for (int i = 0; i < N; ++i) {
            fscanf(fin, "%d", &lvl[i].P);
        }
        sort(lvl, lvl+N, cmp);
        
        fprintf(fout, "Case #%d:", ca);
        for (int i = 0; i < N; ++i) {
            fprintf(fout, " %d", lvl[i].id);
        }
        fprintf(fout, "\n");
    }
    
    fclose(fin);
    fclose(fout);
    return 0;
}





