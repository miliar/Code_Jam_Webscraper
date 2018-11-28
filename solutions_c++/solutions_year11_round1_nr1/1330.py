// free_cell.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

int main() 
{
    fstream f_in("2.in", ios::in);
    fstream f_out("out2.txt", ios::out);

    int T;
    f_in >> T;
    for (int i = 0; i < T; ++i) {
        int N, P_d, P_g;
        f_in >> N >> P_d >> P_g;
        bool pos = false;
        if (P_d == 0) {
            if (P_g < 100) {
                pos = true;
            }
        } else if (P_d == 100) {
            if (P_g > 0) {
                pos = true;
            }
        } else if (P_g == 0) {
            if (P_d > 0) {
                pos = false;
            }
        } else if (P_g == 100) {
            if (P_d < 100) {
                pos = false;
            }
        } else {
            for (int j1 = 1; j1 < N; ++j1) {
                for (int j2 = 1; j2 + j1 <= N; ++j2) {
                    if  (double (j1) / P_d == double((j2)) / (100 - P_d)) {
                        pos = true;
                    }
                }
            }
        }
        if (pos) {
            f_out << "Case #" << i + 1 << ": Possible" << endl;
        } else {
            f_out << "Case #" << i + 1 << ": Broken" << endl;
        }
    }
    return 0;
}



