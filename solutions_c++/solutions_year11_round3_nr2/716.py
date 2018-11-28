#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int tab[1000001];

int main(int argc, char** argv) {
    int t;
    scanf("%d", &t);
    for (int z = 0; z < t; z++) {
        int dopalacze, czas, gwiazdy, modulo, calkowitykoszt = 0, zysk = 0;
        scanf("%d%d%d%d", &dopalacze, &czas, &gwiazdy, &modulo);
        for (int i = 0; i < modulo; i++) {
            scanf("%d", &tab[i]);
            calkowitykoszt += (tab[i]*2);
        }
        for (int i = modulo; i < gwiazdy; i++) {
            tab[i] = tab[i % modulo];
            calkowitykoszt += (tab[i]*2);
        }
        if (czas == 0) {
            /* Specjalny przypadek */
            sort(tab, tab + gwiazdy);
            for (int j = 0; j < dopalacze && j < gwiazdy; j++) {
                zysk += tab[gwiazdy - j - 1];
            }
        } else {
            int i = 0;
            int suma = 0;
            while (suma - czas < 0 && i < gwiazdy) {
                suma += (tab[i++]*2);
            }
            if (i == gwiazdy) {
                zysk = 0;
            } else {
                --i;
                suma -= (tab[i]*2);
                int zyskprzylocie = 0;
                /* Wyliczyc zysk przy locie */
                int czastemp = czas - suma;
                zyskprzylocie = tab[i] - czastemp / 2;
                sort(tab + i + 1, tab + gwiazdy);
                zysk = 0;
                bool dostepny = true;
                for (int j = 0; j < dopalacze && j < (gwiazdy - i - 1); j++) {
                    if (dostepny && zyskprzylocie > tab[gwiazdy - j - 1]) {
                        dostepny = false;
                        zysk += zyskprzylocie;
                    } else {
                        zysk += tab[gwiazdy - j - 1];
                    }
                }
            }
        }
        printf("Case #%d: %d\n", z + 1, calkowitykoszt - zysk);
    }
    return 0;
}

