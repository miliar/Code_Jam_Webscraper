#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int T, N, bTab[100], oTab[100], bNow, oNow;
    char ch, obOrder[201];
    int oIsNow, bIsNow, obIsNow;
    int oToPush, bToPush;
    int movesNeeded;
    fstream plikIn ("large.in", fstream::in | fstream::out);
    fstream plikOut ("large.out", fstream::in | fstream::out);

    plikIn >> T;


    for(int i=0; i<T; i++) {
        movesNeeded = 0;
        oToPush = bToPush = 0;
        plikIn >> N;
        { //
        bNow = oNow = 0;
        for(int j=0; j<N;j++) {
            plikIn >> ch;
            obOrder[j] = ch;
            switch(ch) {
                case 'O':
                    plikIn >> oTab[oNow];
                    oNow++;
                    break;
                case 'B':
                    plikIn >> bTab[bNow];
                    bNow++;
                    break;
            }
        }
        }//
    /// READING S DONE
    //...
    /// CMPT START

    oIsNow = bIsNow = 1;
    obIsNow = 0;
    while(1) {
        if(obOrder[obIsNow] == 'O') {
            if(oTab[oToPush] != oIsNow) {
                if(oTab[oToPush] > oIsNow) oIsNow++;
                if(oTab[oToPush] < oIsNow) oIsNow--;
            } else {
                //cout << "*";
                oToPush++;
                obIsNow++;
            }


            if(bTab[bToPush] != bIsNow) {
                if(bTab[bToPush] > bIsNow) bIsNow++;
                if(bTab[bToPush] < bIsNow) bIsNow--;
            }
        }
        else if(obOrder[obIsNow] == 'B') {
            if(bTab[bToPush] != bIsNow) {
                if(bTab[bToPush] > bIsNow) bIsNow++;
                if(bTab[bToPush] < bIsNow) bIsNow--;
            } else {
                //cout << "*";
                bToPush++;
                obIsNow++;
            }


            if(oTab[oToPush] != oIsNow) {
                if(oTab[oToPush] > oIsNow) oIsNow++;
                if(oTab[oToPush] < oIsNow) oIsNow--;
            }
        }
        //cout << "#" << T << " O:" << oIsNow << " | " << oTab[oToPush] << " B:" << bIsNow << " | " << bTab[bToPush]<< endl;
        movesNeeded++;
        if(obIsNow == N) {
             plikOut << "Case #" << i+1  << ": " << movesNeeded << endl;
             break;

        }

    }


    }





    plikIn.close();
    plikOut.close();
    return 0;
}
