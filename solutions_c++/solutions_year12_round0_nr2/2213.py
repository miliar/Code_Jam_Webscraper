/* 
 * File:   main.cpp
 * Author: nickeveritt
 *
 * Created on April 14, 2012, 5:29 PM
 */

#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
#include <math.h>

using namespace std;

int meetsp(int p, int total) {
    int answer = 0;
    int a0 = floor(total / 3.0);
    int a1 = a0 + 1;
    if (a0 + a0 + a0 == total) {
        if (a0 >= p) answer = 1;
    }
    if (a0 + a0 + a1 == total) {
        if (a1 >= p) answer = 1;
    }
    if (a0 + a1 + a1 == total) {
        if (a1 >= p) answer = 1;
    }
    return answer;
}

int surprisep(int p, int total) {
    int answer = 0;
    int a0 = ceil(total / 3.0) - 1;
    if (a0 < 0) a0 = 0;
    int a1 = a0 + 1;
    int a2 = a0 + 2;
    if (a0 + a0 + a2 == total) {
        if (a2 >= p) answer = 1;
    }
    if (a0 + a1 + a2 == total) {
        if (a2 >= p) answer = 1;
    }
    if (a0 + a2 + a2 == total) {
        if (a2 >= p) answer = 1;
    }
    return answer;
}

/*
 * 
 */
int main(int argc, char** argv) {
    string instr;
    int totcases;
    getline(cin, instr);
    stringstream(instr) >> totcases;
    for (int casenum=0; casenum<totcases; casenum++) {
        cout << "Case #" << (casenum+1) << ": ";
        int result = 0;
        int n; cin >> n;
        int s; cin >> s;
        int p; cin >> p;
        for (int i=0; i<n; i++) {
            int j; cin >> j;
            if (meetsp(p,j) == 1) {
                result++;
            } else {
                if (surprisep(p,j) == 1 && s > 0) {
                    result++;
                    s--;
                } 
            }
        }
        cout << result << endl;
    }
    return 0;
}

