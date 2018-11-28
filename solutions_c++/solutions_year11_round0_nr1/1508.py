//
//  main.cpp
//  Bot Trust
//
//  Created by Trung Dinh on 5/7/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include<fstream>
#define INPUTFILE "A-large.in"
#define OUTPUTFILE "text.out"
using namespace std;

int main (int argc, const char * argv[])
{
    int nTest;
    ifstream fi(INPUTFILE);
    ofstream fo(OUTPUTFILE);
    fi >> nTest;
    for (int test = 0; test < nTest; test ++) {
        int n;
        char bot;
        int o, b, to, tb, t, button, delta;
        o = b = 1;
        to = tb = t = 0;
        fi >> n;
        for (int i = 0; i < n; i ++) {
            fi >> bot >> button;
            //cout << bot << " " << button << endl;
            if (bot == 'O') {
                delta = abs(o - button);
                if (to < t) {
                    if (t - to < delta)
                        t = to + delta;
                }
                else t = t + delta;
                to = t = t + 1;
                o = button;
            }
            else {
                delta = abs(b - button);
                if (tb < t) {
                    if (t - tb < delta)
                        t = tb + delta;
                }
                else t = t + delta;
                tb = t = t + 1;
                b = button;
            }
        }
        fo << "Case #" << test + 1 << ": " << t << endl;
    }
    return 0;
}

