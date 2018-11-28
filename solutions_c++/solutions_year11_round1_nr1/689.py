#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define sz size()
#define pb push_back
#define len length()
#define clr clear()

#define eps 0.0000001
#define PI  3.14159265359
#define inf 1999888777

int max(int q, int w) {
    if (q > w) return q;
    return w;
}

int main() {
    FILE *ff = fopen("ulazz.in", "r");
    FILE *gg = fopen("izlaz.txt", "w");
    long long t, n, Pd, Pg, x, y, danas, ikad, m, m1, m2;
    fscanf(ff, "%I64d", &t);
    for (int zzz = 1; zzz <= t; zzz++) {
        fscanf(ff, "%I64d%I64d%I64d", &n, &Pd, &Pg);
        fprintf(gg, "Case #%d: ", zzz);
        if ((Pg > 0) && (Pg < 100)) {
            danas = 100;
            for (int i = 2; i <= 100; i++) {
                while ((Pd % i == 0) && (danas % i == 0)) {
                    Pd /= i;
                    danas /= i;
                    //printf("1     %d %d %d\n", i, Pd, danas);
                }
            }
            x = (danas*Pd)/100;
            y = danas-x;
            if (danas <= n) fprintf(gg, "Possible\n");
            else fprintf(gg, "Broken\n");
        }
        else {
            if (((Pg == 0) && (Pd == 0)) || ((Pg == 100) && (Pd == 100))) fprintf(gg, "Possible\n");
            else fprintf(gg, "Broken\n");
        }



    }
}



