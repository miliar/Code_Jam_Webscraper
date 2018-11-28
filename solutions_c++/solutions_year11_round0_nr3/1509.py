//
//  main.cpp
//  Candy Splitting
//
//  Created by Trung Dinh on 5/7/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include<fstream>
#define INPUTFILE "C-large.in"
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
        int f[1001], sum, min, xor_result;
        //initialize
        sum = 0;
        min = 50000000;
        xor_result = 0;
        //
        fi >> n;
        for (int i = 0; i < n; i++) {
            fi >> f[i];
            sum += f[i];
            if (min > f[i]) min = f[i];
            xor_result = xor_result xor f[i];
        }
        fo << "Case #" << test + 1 << ": ";
        if (xor_result != 0) 
            fo << "NO" << endl;
        else
            fo << sum - min << endl;
    }
    fi.close();
    fo.close();
    return 0;
}

