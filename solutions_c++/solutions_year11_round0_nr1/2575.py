#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;



int main() {

    ofstream out;
    out.open ("A-large.out");
    ifstream in;
    in.open("A-large.in");


    int t;
    in >> t;
    for(int i=0; i<t; ++i) {

        int n;
        in >> n;

        int brSekO = 0, brSekB = 0;
        int oPos = 1, bPos = 1;

        for(int i=0; i<n; ++i) {
            char r;
            int pos;
            in >> r >> pos;

            if(r == 'O') {
                int trajanje = abs(pos - oPos) + 1;
                if(brSekO + trajanje <= brSekB)
                    brSekO = brSekB + 1;
                else
                    brSekO += trajanje;
                oPos = pos;
            }

            else if(r == 'B') {
                int trajanje = abs(pos - bPos) + 1;
                if(brSekB + trajanje <= brSekO)
                    brSekB = brSekO + 1;
                else
                    brSekB += trajanje;
                bPos = pos;
            }
        }

        out << "Case #" << (i+1) << ": " << max(brSekO, brSekB) << endl;
    }


    return 0;

}
