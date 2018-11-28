#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <math.h>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

char buff[110];
int getInt(ifstream& in) {
    in.getline(buff, 110);
    istringstream ss(buff);
    int n;
    ss >> n;
    return n;
}

string getStr(ifstream& in) {
    in.getline(buff, 110);
    return string(buff);
    
}

int main(int argc, char* argv[]) {
    string name = argv[1];
    string outName = name + ".out";
    ifstream in(name.c_str());
    ofstream out(outName.c_str());

    int n;
    in >> n;
    char buff[101];

    in.getline(buff, 101);
    for (int i = 0; i < n ; i++) {
        int s;
        int q;

        if (i >= 1) {
            i = i;
        }
        
        buff[0] = 0;
        
        if (buff[0] != 0) {
            i = i;
        }
        //in.getline(buff, 101);
        s = getInt(in);
        string se[101];
        string qr[1001];
        
        for (int j = 0; j < s; ++j) {
        
            se[j] = getStr(in);
        }
    
        q = getInt(in);
        for (int j = 0; j < q; ++j) {
            qr[j] = getStr(in);
        }

        j = 0;
        int temp[111];
        
        memset(temp, 0, sizeof(temp) / sizeof(int));
        int t = 0;
        int count = 0;
        for (j = 0; j < q; ++j) {
            for (int k = 0; k < s; ++k) {
                if (se[k] == qr[j]) {
                    break;
                }
            }

            if (k < s && temp[k] == 0) {
                ++t;
                temp[k] = 1;
                if (t == s) {
                    count++;
                    memset(temp, 0, sizeof(temp) / sizeof(int));
                    t = 0;
                    j--;
                }
            }
        }

        out << "Case #" << i + 1 << ": " << count << endl;
    }
}

