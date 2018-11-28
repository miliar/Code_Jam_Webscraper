#include <cmath>
#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

typedef struct vine_t {
    int d, l;
    int ad;
};

bool cmp(const vine_t &a, const vine_t &b) {
    return a.d < b.d;
}

int main() {
    FILE *fin, *fout;    
    fin = fopen("D:\\TopCoder\\gcj2012\\R2\\A-large.in", "r");
    fout = fopen("D:\\TopCoder\\gcj2012\\R2\\A.out", "w");
    int T;
    fscanf(fin, "%d\n", &T);
    for (int ca = 1; ca <= T; ca++) {
        int N;
        fscanf(fin, "%d", &N);
        vine_t vine[N];
        for (int i = 0; i < N; ++i) {
            fscanf(fin, "%d %d", &vine[i].d, &vine[i].l);
            vine[i].d *= 2, vine[i].l *= 2;
            vine[i].ad = -1;
        }
        int D; //double?
        fscanf(fin, "%d", &D);
        D *= 2;
        sort(vine+1, vine+N, cmp);
        vine[0].ad = vine[0].d;
        bool flag = false;
        for (int i = 0; i < N; ++i) {
            if (vine[i].ad < 0) continue;
            int mt = vine[i].d + vine[i].ad;
            if (mt >= D) {
                flag = true;
                break;
            }
            for (int j = i+1; j < N; ++j) {
                if (vine[j].d <= mt) {
                    int ad = min(vine[j].d - vine[i].d, vine[j].l);
                    if (ad > vine[j].ad) vine[j].ad = ad;
                } else {
                    break;
                }
            }
        }
        
        if (flag) fprintf(fout, "Case #%d: YES\n", ca);
        else fprintf(fout, "Case #%d: NO\n", ca);
    }
    
    fclose(fin);
    fclose(fout);
    return 0;
}


