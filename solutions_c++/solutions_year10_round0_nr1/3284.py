#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

string sRep(int n, char c) {
    string s("");

    for (int i = 0; i < n; i++) {
        s += c;
    }

    return s;
}

int main() {
    int K, T, N, iMax;
    ifstream fin("a.in");
    ofstream fout("a.out");
    string s, sList;

    fin >> T;

    for (int i = 0; i < T; i++) {
        fin >> N >> K;
        sList = sRep(N, '0');
        s = sRep(N, '1');
        for (int k = 0; k < K; k++) {
            for (int J = 0; J < N; J++) {
                if (sList[J] == '0') {
                    sList[J] = '1';
                    break;
                }
                else {
                    sList[J] = '0';
                }
            }
        }

        if (sList == s) {
            fout << "Case #" << (i + 1) << ": " << "ON" << endl;
        }
        else {
            fout << "Case #" << (i + 1) << ": " << "OFF" << endl;
        }
    }

    return 0;
}
