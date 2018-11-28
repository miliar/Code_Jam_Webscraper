/**
 * Google Code Jam 2009, Round 1B, Problem B
 * Chris Kennelly (ckennelly@ugcs.caltech.edu)
 * California Institute of Technology
 *
 * Compliation Notes:  I compile my code with gcc, the only external library
 * dependency that you may need is Boost.
 *
 * Usage:  cin  - Test cases
 *         cout - Solution
 *         cerr - Debugging information
 */

#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define F(i,a,b) for(int i=a;i<b;i++)

using namespace std;

void do_testcase() {
    int input;
    cin >> input;

    int digits [10];
    memset(digits, 0, sizeof(digits));

    int tmp = input;
    while (tmp > 0) {
        int tmp2 = tmp % 10;
        if (tmp2 != 0) {
        digits [tmp2]++;
        }
        tmp /= 10;
    }

    input++;
    for ( ; ; input++) {
        int tmpd [10]; 
        memset(tmpd, 0, sizeof(tmpd));
        tmp = input;
        bool fail = false;
        while (tmp > 0) {
            int tmp2 = tmp % 10;
            if (tmp2 != 0) {
            tmpd [tmp2]++;
            if (tmpd [tmp2] > digits [tmp2]) {
                fail = true; break;
            }
            }
           
            tmp /= 10; 
        }

        if (fail) {
            continue;
        } else {
            if (memcmp(digits, tmpd, sizeof(digits)) == 0) {
                cout << input;
                return;
            }
        }
    }
}

int main(int argc, char **argv) {
    int buffer;
    cin >> buffer;
    buffer++;

    F(i,1,buffer) {
        cout << "Case #" << i << ": ";
        do_testcase();
        cout << endl;
    }
}
