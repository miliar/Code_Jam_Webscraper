#include <iostream>
#include <cstdio>
#include <math.h>
#include <set>
using namespace std;
#define ELMATI


int main()
{
    #ifdef ELMATI
        freopen("C-large.out","w",stdout);
        freopen("C-large.in","r",stdin);
    #endif
    int cantidad;
    int nprueba = 1;
    int maximo;
    int minimo;
    int cnumero;
    int prueba;
    cin >> cantidad;
    while(cantidad > 0) {
        cin >> minimo;
        cin >> maximo;
        cnumero = (int) floor(log10(maximo));
        int total = 0;
        while (minimo < maximo) {
            set<int> losqueprobe;
            prueba = minimo;
            for (int i=0; i < cnumero; i++) {
                prueba = (prueba / 10) + (prueba % 10)*pow(10, cnumero);
                if ((minimo < prueba) && (maximo >= prueba)) {
                    if (losqueprobe.find(prueba)==losqueprobe.end()) {
                        total++;
                        losqueprobe.insert(prueba);
                    }
                }
            }
            minimo++;
        }
        cout << "Case #" << nprueba << ": " << total << "\n";
        nprueba++;
        cantidad--;
    }
    return 0;
}
