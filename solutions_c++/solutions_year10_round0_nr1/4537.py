#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
int snap(bool*, int, int);
int main() {
    ifstream fin("A-small-attempt0.in.txt");
    ofstream fout("A-small-attempt0.out");

    int nCase, nSize, nSnaps;
    fin >> nCase;
    for(int i = 0; i < nCase; i++) {
        fin >> nSize;
        bool* bSnapper = new bool[nSize + 1];
        for(int l = 0; l < nSize; l++)
            bSnapper[l] = false;
        
        fin >> nSnaps;
        fout << "Case #" << i + 1;
        if(nSize == snap(bSnapper, nSize, nSnaps))
            fout << ": ON" << endl;
        else
            fout << ": OFF" << endl;
    }
    return 0;
}

int snap(bool* pSnapper, int nSize, int nSnaps)
{
    int nPower;
    for(int j = 0; j < nSnaps; j++) {
        nPower = 0;
        while(nPower < nSize && pSnapper[nPower])
            nPower++;

        for(int l = 0; l <= nPower; l++)
            pSnapper[l] = !(pSnapper[l]);
    }
    nPower = 0;
    while(nPower < nSize && pSnapper[nPower])
        nPower++;
    return nPower;
}
