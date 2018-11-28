
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

unsigned int chickloc[50];
unsigned int speeds[50];

int pickUpChicks(int nchicks, int narrivals, unsigned int barnloc, int timelimit) {
    unsigned int loc, speed;
    int nswaps = 0, j = narrivals;
    for (int i = nchicks-1; i >= 0 && j > 0; --i) {
        loc = chickloc[i];
        speed = speeds[i];
        if ((barnloc-loc)*1.0/speed > timelimit*1.0) 
            nswaps += j;
        else {
            --j;
        }
    }
    if (j != 0) return -1;
    else return nswaps;
}

int main() {
    char inputfilename[] = "B-large.in";
    ifstream ifs(inputfilename);
    int ntestcases, nchicks, narrivals, timelimit, result;
    unsigned int barnloc; 
    ifs>>ntestcases;
    for (int i = 0; i < ntestcases; ++i) {
        ifs>>nchicks>>narrivals>>barnloc>>timelimit;
        for (int j = 0; j < nchicks; ++j) {
            ifs>>chickloc[j];
        }
        for (int j = 0; j < nchicks; ++j) {
            ifs>>speeds[j];
        }

        result = pickUpChicks(nchicks, narrivals, barnloc, timelimit);
        if (result == -1)
            cout<<"Case #"<<(i+1)<<": IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<(i+1)<<": "<<result<<endl;
    }
}

