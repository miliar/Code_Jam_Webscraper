#include <string>
#include <fstream>
#include <iostream>

using namespace std;

int main(void) {
    ifstream fin("A-large.in");
    ofstream fout("temp.out");

    int* powersof2 = new int[31];
    powersof2[0] = 2; // 2^1 = 2
    int lastfound = 1;

    int t;
    fin >> t;
    for (int i = 0; i < t; i++) {
        int n, k;
        fin >> n >> k;
//        cout << n << " " << k << endl;
//        system("PAUSE");
        k++; // 47 -> 48
        for (int j = lastfound; j < n; j++) {
            powersof2[j] = powersof2[j-1] * 2;
        }
        lastfound = n;
        fout << "Case #" << i + 1 << ": ";
        if (k % (powersof2[n - 1]) == 0) // 48 % 16 = 0 (which means it is on)
            fout << "ON" << endl;
        else
            fout << "OFF" << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
