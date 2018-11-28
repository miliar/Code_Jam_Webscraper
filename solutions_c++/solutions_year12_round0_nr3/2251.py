/* 
 * File:   main.cpp
 * Author: nickeveritt
 *
 * Created on April 14, 2012, 6:46 PM
 */

#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

string int2string(int x) {
    ostringstream oss;
    oss << x;
    return oss.str();
}

int recycle(string nnum, int i, int b) {
    int result = 0;
    int recycles[nnum.length()];
    int recyclescount = 0;
    for (int digrec=1; digrec < nnum.length(); digrec++) {
        string cyc1 = nnum.substr(0,digrec);
        string cyc2 = nnum.substr(digrec,nnum.length());
        string cyc3 = cyc2.append(cyc1);
        float res;
        stringstream(cyc3) >> res;
        int dejavu = 0;
        for (int c=0; c<recyclescount; c++) if (recycles[c] == res) dejavu = 1;
        if (dejavu == 0 && res > i && res <= b) {
            result++;
            recycles[recyclescount++] = res;
        }
    }
    return result;
}

/*
 * 
 */
int main(int argc, char** argv) {
    int totcases;
    cin >> totcases;
    for (int casenum=0; casenum<totcases; casenum++) {
        cout << "Case #" << casenum+1 << ": ";
        int a; cin >> a;
        int b; cin >> b;
        int totnums = 0;
        for (int i=a; i<b; i++) {
            string nnum = int2string(i);
            totnums += recycle(nnum,i,b);
        }
        cout << totnums << endl;
    }
    return 0;
}

