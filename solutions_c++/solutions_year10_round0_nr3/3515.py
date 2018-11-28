/* 
 * File:   themepark.cpp
 * Author: hayoungpark
 *
 * Created on May 7, 2010, 11:43 PM
 */

#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <queue>

using namespace std;
/*
 * 
 */

int main(int argc, char** argv) {
    ifstream fin("C-small-attempt1.in");
    ofstream fout("C-small1.out");

    int T, R, K, N, nTemp, nCap, nPpl, nAtt;
    fin >> T;
    
    for(int i = 0; i < T; i++){
        queue<int> qLine;
        nPpl = nAtt = 0;
        
        fin >> R;
        fin >> K;
        fin >> N;
        fin.ignore();
        for(int j = 0; j < N; j++){
            fin >> nTemp;
            qLine.push(nTemp);
            nPpl += nTemp;
            fin.ignore();
        }
        for(int l = 0; l < R; l++){
            if(nPpl > K) {
                nCap = K;
                while(nCap >= qLine.front()) {
                    nTemp = qLine.front();
                    qLine.pop();
                    nCap -= nTemp;
                    nAtt += nTemp;
                    qLine.push(nTemp);
                }
            }
            else
                nAtt += nPpl;
        }
        fout << "Case #" << i + 1 << ": " << nAtt << endl;
    }
    return (EXIT_SUCCESS);
}

