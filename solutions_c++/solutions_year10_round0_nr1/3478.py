#include <iostream>
#include <fstream>
#include <cstring>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

int main (int argc, char * const argv[]) {
    int cases;
    ifstream fin("C:\\A-large.in");
    ofstream fout("C:\\output.txt");

    if (!fin || !fout) {
        cerr << "Unable to open file datafile.txt";
    }

    fin >> cases;
    
for (int c = 0; c < cases; ++c) {
        
//-------------Data Input Start---------------    
    unsigned int clicks, switches;
    bool on = false;

    fin >> switches >> clicks;

    if (clicks % 2 != 0) {
        ++clicks;
        unsigned long max = pow(2.0, switches);

        if (clicks % max == 0) {
            on = true;
        }
    }

//-------------Data Input End---------------
        
    if (on) {
        fout << "Case #" << c+1 << ": " << "ON\n";
    }
    else {
        fout << "Case #" << c+1 << ": " << "OFF\n";
    }
}
    fout << flush;
    fout.close(); 
    return 0;
}
