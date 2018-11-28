/*******************************************\
*                                           *
*   Candy Splitting                         *
*   CodeJam 2011                            *
*   Rafael Medina (MedinaSoft)              *
*                                           *
\*******************************************/

#include <iostream>
#include <fstream>
using namespace std;

int main () {
    int LINE = 1, TOT, N;
    for (scanf ("%d", &TOT); LINE <= TOT; LINE++)  {
        scanf ("%d", &N);
        int C[1000];
        for (int i = 0; i < N; i++) { scanf ("%d", &C[i]); }
        for (int i = 0; i < N-1; i++) {
            for (int j = i+1; j < N; j++) {
                if (C[j] < C[i]) {
                    int tmp = C[i];
                    C[i] = C[j];
                    C[j] = tmp;
                }
            }
        }
        int res,res2,pos = -1, sum[2] = {0,0};
        for (int i = 0; i < N-1; i++) {
            res=-1;
            for(int j = 0; j <= i; j++) {
                if (res == -1) { res = C[i]; }
                else { res = res ^ C[i]; }
                sum[0] += C[i];
            }
            res2=-1;
            for (int j = i+1; j < N; j++) {
                if (res2 == -1) { res2 = C[j]; }
                else { res2 = res2 ^ C[j]; }
                sum[1] += C[j];
            }
            if (res == res2) {  pos = i; break; }
        }
        cout << "Case #" << LINE << ": ";
        if (pos != -1) {
            cout << (sum[1] > sum[0] ? sum[1] : sum[0]);
        }
        else { cout << "NO"; }
        cout << endl;

    }
    return 0;

}
