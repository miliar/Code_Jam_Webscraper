/* 
 * File:   Ans 1
 * Author: kunal
 *
 * Created on 26 July, 2008, 9:10 PM
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char** argv) {
    
    std::ifstream inFile("/home/kunal/Desktop/input"); std::ofstream outFile("/home/kunal/Desktop/output");
    
    int N, P, K, L, i = 0;
    
    inFile>>N;
    
    while (i<N) {
        inFile>>P;
        inFile>>K;
        inFile>>L;
        
        unsigned long keyPress = 0;
        vector <unsigned long> freq(L, 0);
        
        for (int j=0; j<L; j++) inFile>>freq[j];
        
        sort(freq.begin(), freq.end());
        
        for (int j = 0; j<L; j++) {
            keyPress += freq[L-j-1] * (1 + j/K);
        }
        
        freq.clear();
        i++;
        
        outFile<<"Case #"<<i<<": "<<keyPress<<"\n";
    }
    
    
    inFile.close(); outFile.close();
    return (EXIT_SUCCESS);
}

