/*
 hasihfiasjioasjfoisjfoisajisjdfioasjfo

 */
#include <iostream>
using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("out4.txt","w",stdout);

    int t, pos;
    cin >> t;
    for (pos = 1; pos <= t; pos++) {
        int position, lmm, ihihihi[100] = {0}, ihjiaiia[100] = {0};
        /*
 hasihfiasjiloklkjokjokojojofioasjfo
         */
        char a[100];
        int O = 1, notbad = 0, bug = 1, ltj = 0, bbb, mo, temp, step = 0;
        cin >> lmm;
        for (position = 0; position < lmm; position++) {
            cin >> a[position] >> temp;
            if (a[position] == 'B')
                ihihihi[ltj++] = temp;
            else
                ihjiaiia[notbad++] = temp;
        }
        /*
 hjiojewofjosjfosjfosjdjfijdsifjsijfsfioasjfo

         */
        ltj = notbad = 0;
        for (position = 0; position < lmm; position++) {
            if (a[position] == 'B') {
                if (bug < ihihihi[ltj])
                    bbb = 1;
                else//ijijiji
                    bbb = -1;
                if (O < ihjiaiia[notbad])
                    mo = 1;
                else {
                    mo = -1; //ijijiji
                }
                for (; bug != ihihihi[ltj]; bug += bbb) {
                    step++;
                    if (O != ihjiaiia[notbad])
                        //hihihi
                        O += mo;
                    //huihi
                }
                step++;
                if (O != ihjiaiia[notbad])
                    O += mo;
                ltj++;
            } else
                if (a[position] == 'O') {
                if (bug < ihihihi[ltj])
                    bbb = 1;
                else
                    bbb = -1;
                if (O < ihjiaiia[notbad])
                    mo = 1;
                else
                    mo = -1;
                for (; O != ihjiaiia[notbad]; O += mo) {
                    step++;
                    if (bug != ihihihi[ltj])
                        bug += bbb;
                }
                step++;
                if (bug != ihihihi[ltj])
                    bug += bbb;
                notbad++;
            }
        }
        cout << "Case #" << pos << ": " << step << endl;
    }
}