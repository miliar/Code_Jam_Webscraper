#include <stdio.h>
#include <math.h>
#include <stdlib.h>
using namespace std;

int max(int a, int b) {
    if (a > b) return a;
    return b;
}

int main() {
    FILE *ff = fopen("A-large.in", "r");
    FILE *gg = fopen("izlaz.txt", "w");
    char c;
    int sta, prvi = 1, drugi = 1, res = 0, prviKad = 0, drugiKad = 0;
    int n, t;
    fscanf(ff, "%d", &t);
    for (int i = 1; i <= t; i++) {
        prvi = drugi = 1;
        prviKad = drugiKad = 0;
        fscanf(ff, "%d", &n);
        for (int j = 1; j <= n; j++) {
            fscanf(ff, " %c %d", &c, &sta);
            //printf("%c %d\n", c, sta);
            if (c == 'O') {
                prviKad = max(drugiKad+1, prviKad + max(1, (abs(prvi - sta) + 1)));
                prvi = sta;
            }
            else {
                drugiKad = max(prviKad+1, drugiKad + max(1, (abs(drugi - sta) + 1)));
                drugi = sta;
            }
        }
        fprintf(gg, "Case #%d: %d\n", i, max(prviKad, drugiKad));
    }
}
