#include <iostream>
#include <cstdio>
using namespace std;
#define ELMATI

using namespace std;

int main()
{
    #ifdef ELMATI
        freopen("B-large.out","w",stdout);
        freopen("B-large.in","r",stdin);
    #endif
    int cantidad;
    cin >> cantidad >> ws;
    int nprueba = 1;
    while (cantidad > 0) {
        int googlers;
        int nota;
        int triplets;
        int val;
        int resultado = 0;
        cin >> googlers;
        cin >> triplets;
        cin >> nota;
        if (nota==0) {
            resultado = googlers;
            for (int p = 0; p < googlers; p++) {
                int n;
                cin >> n;
            }
        } else if (nota==1) {
            for (int p = 0; p < googlers; p++) {
                int n;
                cin >> n;
                if (n != 0) resultado++;
            }
        } else {
            nota = nota*3;
            while(googlers > 0) {
                cin >> val;
                if (val >= (nota-2)) {
                    resultado++;
                } else if (((val == nota-4) or (val == nota-3)) and (triplets > 0)){
                     resultado++;
                    triplets--;
                }
                googlers--;
            }
        }
        cout << "Case #" << nprueba << ": " << resultado << "\n";
        nprueba++;
        cantidad--;
    }
    return 0;
}
