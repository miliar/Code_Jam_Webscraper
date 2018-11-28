/* 
 * File:   main.cpp
 * Author: nickeveritt
 *
 * Created on April 14, 2012, 4:41 PM
 */

#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    string transposition = "yhesocvxduiglbkrztnwjpfmaq";
    int numcases;
    string instr;
    getline(cin, instr);
    stringstream(instr) >> numcases;
    for (int casecount=0; casecount<numcases; casecount++) {
        cout << "Case #" << (casecount+1) << ": ";
        getline(cin, instr);
        for (int i=0; i<instr.length(); i++) {
            if (instr[i] == 32) {
                cout << " ";
            } else {
                cout << transposition[instr[i] - 97];
            }
        }
        cout << endl;
    }
    return 0;
}

