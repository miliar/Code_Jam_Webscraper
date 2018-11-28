/* 
 * File:   main.cpp
 * Author: hayoungpark
 *
 * Created on May 7, 2010, 4:08 PM
 */

#include <stdlib.h>
#include <iostream>
#include <fstream>

using namespace std;
/*
 * 
 */
int main(int argc, char** argv) {
    ifstream fin("A-small-attempt0(2).in");
    ofstream fout("A-small.out");

    int T, N, K, l, nPower;
    fin >> T;
    for(int nCase = 0; nCase < T; nCase++) {
        fin >> N;
        bool* bSnapper = new bool[N + 1];
        for(l = 0; l < N; l++)
            bSnapper[l] = false;
        
        fin >> K;
        for(int nSnap = 0; nSnap < K; nSnap++) {
            nPower = 0;
            while(nPower < N && bSnapper[nPower])
                nPower++;

            for(l = 0; l <= nPower; l++)
                bSnapper[l] = !(bSnapper[l]);
        }
        fout << "Case #" << nCase + 1;
        nPower = 0;
        while(nPower < N && bSnapper[nPower])
            nPower++;
        if(nPower == N)
            fout << ": ON" << endl;
        else
            fout << ": OFF" << endl;
    }
    return (EXIT_SUCCESS);
}

