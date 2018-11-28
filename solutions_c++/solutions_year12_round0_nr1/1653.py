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
#include <cstring>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;

/*
 * 
 */

char translationTable[] = "yhesocvxduiglbkrztnwjpfmaq";

inline void handleProblemNr(int nr, ifstream &in, ofstream &out) {

    char buffer[200];
    in.getline(buffer,200);
    for (int i=0; i<strlen(buffer); i++) {
        if(buffer[i] >= 'a' && buffer[i] <= 'z')
            buffer[i] = translationTable[buffer[i]-'a'];
    }
    
    out << "Case #" << nr << ": " << buffer << endl;
}

int main(int argc, char** argv) {
    int numTestCases;
    ifstream in("input.in");
    ofstream out("output.out");
    
    in >> numTestCases;
    in.get(); // Read \n
    for(int test=0; test < numTestCases; test++) {
        cout << "Handle problem #" << (test+1) << " ..." << endl;
        handleProblemNr(test+1, in, out);
    }
    
    return 0;
}

