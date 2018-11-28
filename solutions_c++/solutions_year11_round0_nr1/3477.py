/*******************************************\
*                                           *
*   Bot Trust                               *
*   CodeJam 2011                            *
*   Rafael Medina (MedinaSoft)              *
*                                           *
\*******************************************/

#include <iostream>
#include <fstream>
using namespace std;

int main () {
    int LINE = 1, TOT, N, K, P;
    char R;

    for (scanf ("%d", &TOT); LINE <= TOT; LINE++)  {
        scanf ("%d ", &N);
        int O[100],B[100],order[100], oi=0, bi=0,o=0;
        for (int t = 1; t <= N; t++) {
            scanf("%c %d ",&R,&P);
            if (R == 'O' || R == 'o') { O[oi++] = P; order[o++] = 1;}
            else { B[bi++] = P; order[o++] = 2; }
        }
        //cout << ":: O ::\n"; for (int x = 0; x < oi; x++) { cout << x << " :: " << O[x] << endl; }
        //cout << ":: B ::\n"; for (int x = 0; x < bi; x++) { cout << x << " :: " << B[x] << endl; }
        int secs=0;
        int x=0, y=0, z=0, poso=1, posb=1;

        do {
            bool skip=false;
            if (x < oi) {
                if (poso < O[x]) { poso++; }
                else if (poso > O[x]) { poso--; }
                else if (poso == O[x] && order[z] == 1) { x++; z++; skip = true; }
            }
            if (y < bi) {
                if (posb < B[y]) { posb++; }
                else if (posb > B[y]) { posb--; }
                else if (posb == B[y] && order[z] == 2) {
                   if (!skip) { y++; z++; }
                }
            }
            secs++;
            //cout << secs << " :: " << poso << " : " << (x < oi ? O[x] : -1) << " :: " << posb << " : " << (y < bi ? B[y] : -1) << " :: " << (order[z] ? "Orange" : "Blue") << endl;
        }while(x < oi || y < bi);
        cout << "Case #" << LINE << ": " << secs << endl;
    }
    return 0;

}
