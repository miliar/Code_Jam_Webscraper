#include <iostream>
#include <string>

using namespace std;

int main() {

    int L, D, N;
    char wD[5000][15];
    char input[5000];

    cin >> L >> D >> N;
    
    for (int i = 0; i < D; i++) {
        cin >> wD[i];
    }

    int caseNr = 1;
    bool valid;
    while (N-- > 0) {
        cin >> input;
        int count = 0;
        int iLen = strlen(input), iIndex;
        char pivot;
        for (int i = 0; i < D; i++) { // all words in vocabulary
            valid = false;
            //cout << input << " and " << wD[i] << endl;
            iIndex = 0;
            for (int j = 0; j < L; j++) { // char of each word
                pivot = wD[i][j];
                if (input[iIndex] == '(') {
                    iIndex++;
                    while (input[iIndex] != ')') {
                        if (input[iIndex] == pivot) {
                            valid = true;
                            //cout << "# " << input[iIndex] << " == " << pivot << endl;
                            while(input[iIndex] != ')')
                                iIndex++;
                            iIndex++;
                            break;
                        } else {
                            valid = false;
                        }
                        iIndex++;
                    }
                    if (valid == false)
                        break;
                } else {
                    if (input[iIndex] == pivot) {
                        valid = true;
                        iIndex++;
                        //cout << "# " << input[iIndex] << " == " << pivot << endl;
                    } else {
                        valid = false;
                        break;
                    }
                }
            }
            if (valid == true) {
                //cout << "*** " << wD[i] << " ***" << endl;
                count++;
            }
        }
        cout << "Case #" << caseNr++ << ": " << count << endl;
    }

    return 0;
}

