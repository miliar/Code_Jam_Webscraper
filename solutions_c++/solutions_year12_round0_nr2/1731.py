/* 
 * File:   main.cpp
 * Author: Folker Hoffmann
 *
 * Created on 24 de marzo de 2012, 21:43
 */

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <deque>
#include <queue>
#include <set>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;

/*
 * 
 */

inline void handleProblemNr(int nr, ifstream &in, ofstream &out) {
    int N,S,p,t;
    in >> N >> S >> p;
    int maximumGooglerNumber = 0;
    for(int i=0; i<N; i++) {
        in >> t;
        if (p == 1 && t < 1) continue; 
        if (t >= 3 * p - 2) maximumGooglerNumber++; 
        else if ((t >= 3 * p - 4) && (S > 0)) {
            maximumGooglerNumber++;
            S--;
        }
    }
    
    out << "Case #" << nr << ": " << maximumGooglerNumber << endl;
}

int main(int argc, char** argv) {
    int numTestCases;
    ifstream in("input.in");
    ofstream out("output.out");
    
    in >> numTestCases;
    
    for(int test=0; test < numTestCases; test++) {
        cout << "Handle problem #" << (test+1) << " ..." << endl;
        handleProblemNr(test+1, in, out);
    }
    
    return 0;
}

