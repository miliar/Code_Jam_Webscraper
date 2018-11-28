/* 
 * File:   main.cpp
 * Author: Folker Hoffmann
 *
 * Created on 24 de marzo de 2012, 21:43
 */

#include <cmath>
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
    int A,B;
    int count = 0;
    set<int> s; // To solve the #4 problem
    
    in >> A >> B;
    for(int n = A; n < B; n++) {
        s.clear();
        int maxRotate = log10(n);
        int cutOff = 10;
        int multFirst = 1;
        for(int i=0; i<maxRotate; i++) multFirst *= 10;
        
        // Split the number and merge it again:
        for(int i=0; i<maxRotate; i++) {
            int last = n % cutOff;
            int first = n / cutOff;
            
            if( last >= (cutOff/10)) { // No leading 0
                int m = multFirst * last + first;
                if (m > n && m <= B && s.count(m) == 0) {
                    count++;
                    s.insert(m);
                }
            }
            cutOff *= 10;
            multFirst /= 10;
        }
    }
    
    out << "Case #" << nr << ": " << count << endl;
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

