//============================================================================
// Name        : SearchAndSort.cpp
// Author      : Akshay Dua
// Version     :
// Copyright   : Open to all
// Description : Hello World in C++, Ansi-style
//============================================================================

// Comment/Uncomment as necessary
#include <iostream>
#include <fstream>
//#include <stack>
#include <vector>
#include <algorithm>
#include <math.h>
#include <assert.h>
using namespace std;

ifstream infile;
ofstream outfile;

// print any vector. Remember: change the vector element type.
void printVector(vector<int>& v)
{
    for(int i = 0; i < (int) v.size(); ++i) {
        cout << v[i] << " ";
    }
    cout << endl;
}

void processEntry(int entryIdx, int N, int K)
{
    string bulbState = "OFF";

    int firstGlow = pow(2, N);

    if((K + 1) % firstGlow == 0) {
        bulbState = "ON";
        goto do_output;
    }

    do_output:
    // no change needed here
    outfile << "Case #" << entryIdx + 1 << ": ";
    outfile << bulbState << endl;
}

int main()
{
    // change file names
    infile.open("/home/akshay/OpenSource/GoogleCodeJam/iofiles/A-large.in");
    assert(infile.is_open());

    outfile.open(
            "/home/akshay/OpenSource/GoogleCodeJam/iofiles/A-large.out");
    assert(outfile.is_open());

    // read number of cases; no change needed here
    int T;
    infile >> T;
    cout << "Entries: " << T << endl;

    // change input parameters
    int N, K;

    for (int i = 0; i < T; ++i) {
        // read input parameters: change as needed
        infile >> N >> K;

        // output input parameters on screen
        cout << "processing..." << endl;
        cout << N << " " << K << endl;

        // process the input
        processEntry(i, N, K);
    }

    return 0;
}
