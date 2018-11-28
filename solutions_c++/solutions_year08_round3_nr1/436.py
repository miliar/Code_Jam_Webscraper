/*
 * =====================================================================================
 *
 *       Filename:  codeletters.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  07/27/08 11:07:47 CEST
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:   (), 
 *        Company:  
 *
 * =====================================================================================
 */

#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <map>

using namespace std;

typedef vector<int> VI;

long long calc(VI& freqs, int K){
    
    long long res = 0;
    sort(freqs.begin(),freqs.end());
    int s = freqs.size();
    for(int i=0;i<s;++i){
        res+=freqs[s-1-i]*(i/K+1);
    }
    return res;
}

void process(ifstream& input, ofstream& output){

    string line;
    getline(input,line);
    int n = atoi(line.c_str());
    int P,K,L;
    int f;
    vector<int> freqs;
    for(int i=1;i<=n;++i){
        freqs.clear();
        getline(input,line);
        sscanf(line.c_str(),"%d %d %d",&P,&K,&L);
        getline(input,line);
        stringstream ss(line);
        freqs.resize(L);
        int pos = 0;
        while(ss >>f){
            freqs[pos++]=f;
        }
        output << "Case #" << i << ": " << calc(freqs,K) << endl;        
    }

}




int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr,"usage: %s arg1 arg2\n", argv[0]);
        return 1;
    }
    ifstream input(argv[1]);
    ofstream output(argv[2]);
    process(input,output);
    return 0;
}

