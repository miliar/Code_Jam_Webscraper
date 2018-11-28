/* 
 * File:   A-TheSnapper.cpp
 * Author: vdyy
 *
 * Created on May 8, 2010, 9:17 AM
 */

#include <stdlib.h>
#include <vector>
#include <fstream>
#include <iostream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {

    ifstream in("A-small-attempt4.in");
    if (!in) {
        cout << "Cannot open input file for reading" << endl;
        getchar();
        return -1;
    }

    ofstream out("A-small-attempt4.out");
    if (!out) {
        cout << "Cannot open output file for writing" << endl;
        getchar();
        return -1;
    }
    
    unsigned int cases;

//    cin >> cases;
    in >> cases;


    for (int i = 1; i <= cases; i++) {
        int snappers;
        unsigned long int snaps;
//        cin >> snappers;
//        cin >> snaps;
        in >> snappers;
        in >> snaps;

        vector< bool > state(snappers + 1, false);
        state[0] = true;
        for (unsigned long int j = 1; j <= snaps; j++) {
            for (int k = snappers; k >= 1; k--) {
                bool active = true;
                for (int l = k - 1; l >= 0; l--) {
                    if (!state[l]) {
                        active = false;
                        break;
                    }
                }
                if (active) state[k] = !state[k];
            }
        }

        bool active = true;
        for (int j = snappers - 1; j >= 0; j--) {
            if (!state[j]) {
                active = false;
                break;
            }
        }
//        cout << "Case #" << i << ": " << (state[snappers] && active ? "ON" : "OFF" ) << endl;
        out << "Case #" << i << ": " << (state[snappers] && active ? "ON" : "OFF" ) << endl;

    }

    if (in) in.close();
    if (out) out.close();

    return 0;
}

