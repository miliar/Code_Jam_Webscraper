#include <iostream>
#include <fstream>

using namespace std;

int main() {
    fstream fin ("A-small-attempt2.in", fstream::in);
    int cases; fin >> cases;
    string answers[cases];
    for (int t = 0; t < cases; t++) {
        int n, pD, pG;
        fin >> n >> pD >> pG;
        int numer = pD;
        int denom = 100;
        for (int i = 2; i <= numer ; i++) {
            while (numer % i == 0 && denom % i == 0) {
                numer /= i;
                denom /= i;
            }
        }
        if (pG == 0 && pD == 0) answers[t] = "Possible";
        else if (denom > n) answers[t] = "Broken";
        else if (pG == 100 && pD < 100 || pG == 0 && pD > 0) answers[t] = "Broken";
        else answers[t] = "Possible";
    }
    fstream fout ("output.txt", fstream::out);
    for (int t = 0; t < cases; t++)
        fout << "Case #" << t+1 << ": " << answers[t] << endl;
    //system("PAUSE");
    return 0;
}
