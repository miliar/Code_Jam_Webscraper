//
//  Qualification Round 2011 - C
//
//  Diogo Tridapall
//

#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;



int main (int argc, const char * argv[]){

    string inFileName;
    string outFileName;
    
    switch (argc) {
        case 2:
            inFileName = argv[1];
            outFileName.assign(inFileName, 0, inFileName.find_last_of(".in")-2);
            outFileName+=".out";
            break;
        default:
            cout << "Usage: " << argv[0] << " inputFile" << endl;
            exit(0);
            break;
    }
    
    fstream inFile(inFileName.c_str(),fstream::in);
    if (!inFile.is_open()) {
        cout << "File " << inFileName << " is not open!" << endl;
        exit(1);
    }
    fstream outFile(outFileName.c_str(),fstream::out);
    if (!outFile.is_open()) {
        cout << "File " << outFileName << " is not open!" << endl;
        exit(1);
    }
    
    
    int T;    
    
    if(!(inFile >> T)){
        cout << "Error, can't read T!" << endl;
        exit(1);
    }
    
    for (int iT = 0; iT < T; ++iT) {
        int N;
        inFile >> N;
        vector<int> C;
        C.reserve(N);
        for (int iN=0; iN<N; ++iN) {
            int tmp;
            inFile >> tmp;
            C.push_back(tmp);
        }
        int poss = (1<<N)-2;
        bool possible = false;
        int max = 0;
        for (int i=1; i<poss; ++i) {
            int sum1=0;
            int sum2=0;
            int xor1=0;
            int xor2=0;
            for (int iN=0; iN<N; ++iN)
                if (i & (1<<iN)) {
                    sum1+=C[iN];
                    xor1^=C[iN];
                } else {
                    sum2+=C[iN];
                    xor2^=C[iN];
                }
            if ((xor1 == xor2)){
                possible = true;
                double maxL = (sum1 > sum2)? sum1 : sum2;
                if (maxL > max) {
                    max = maxL;
                }
            }
        }
        
        outFile << "Case #" << iT+1 << ": ";
        if (possible) 
            outFile << max << endl;
        else
            outFile << "NO" << endl;
    }
    
    
    inFile.close();
    outFile.close();
    return 0;
}


















