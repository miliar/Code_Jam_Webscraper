#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;


int main() {

    ifstream in;
    ofstream out;
    out.open("A-small-attempt1.out");
    in.open("A-small-attempt1.in");

    int t;
    in >> t;

    for(int i=0; i<t; ++i) {

        int n, k;
        in >> n >> k;

        int rez = (1 << n) | k;
        string ispis;

        if((rez+1) % (1 << (n+1)) == 0)
            ispis = "ON";
        else ispis = "OFF";

        out << "Case #" << i+1 << ": " << ispis << endl;

    }

    return 0;
}
